from telebot import TeleBot, types
import os
from dotenv import load_dotenv
from recipes import get_recipes_data, parse_recipes_data, get_next_message

load_dotenv()

bot = TeleBot(token=os.getenv("TOKEN"))

recipe_by_index = {} # key=chat_id, value={messages: list, index: int}

@bot.message_handler(commands=["start"])
def greet_user(message):
    text = '''
Hello, this bot was designed to help you find delicious meal recipes!
Type the key-word, for example: 'chicken' to get some recipes with that.

Press 'next' button to get one-more recipe...   Good luck))
'''
    bot.send_message(chat_id=message.chat.id, text=text)


@bot.message_handler(func=lambda message: True)
def look_for_recipe(message):
    product_name = message.text

    data = get_recipes_data(product_name=product_name)
    split_messages = parse_recipes_data(data=data)

    if not split_messages:
        bot.send_message(chat_id=message.chat.id, text="No recipes found.")
        return

    recipe_by_index[message.chat.id] = {
        "messages": split_messages,
        "index": 0
    }

    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Next", callback_data="btn1")
    markup.add(btn1)

    answer = get_next_message(recipe_by_index[message.chat.id])
    bot.send_message(chat_id=message.chat.id, text=answer, reply_markup=markup, parse_mode='Markdown')


@bot.callback_query_handler(func=lambda call: True)
def next_recipe(call):
    if call.data == "btn1":
        recipes_data = recipe_by_index.get(call.message.chat.id)
        next_message = get_next_message(recipes_data)
        if next_message == None:
            bot.send_message(chat_id=call.message.chat.id, text="There are no more recipes :(")
        else:
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton("Next", callback_data="btn1")
            markup.add(btn1)
            bot.send_message(chat_id=call.message.chat.id, text=next_message, reply_markup=markup, parse_mode='Markdown')





