import requests
import os
from dotenv import load_dotenv

load_dotenv()

app_key = os.getenv("APP_KEY")
app_id = os.getenv("APP_ID")


def get_recipes_data(product_name: str) -> dict:
    url = f"https://api.edamam.com/api/recipes/v2"

    params = {
        "app_id": app_id,
        "app_key": app_key,
        "q": product_name,
        "type": "public",
        "health": ("vegan","vegetarian"),
        "diet": ("low-sodium","low-fat"),
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200:
        return data
    else:
        return f"Error: {response.status_code}"


def split_response(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        split_messages = response.split("\n\n\n")
        return split_messages
    return wrapper

@split_response
def parse_recipes_data(data: dict) -> str:

    result = ""
    for hit in data.get('hits', []):
        recipe = hit.get('recipe', {})
        label = recipe.get("label")
        image = recipe.get("images", {}).get("REGULAR", {}).get("url")
        ingredient_lines = recipe.get("ingredientLines")
        cuisine_type = recipe.get("cuisineType")
        meal_type = recipe.get("mealType")
        dish_type = recipe.get("dishType")
        calories = recipe.get("calories")

        result += f"Meal: {label}\n\n"
        result += "Ingredients:\n"
        for ingredient in ingredient_lines:
            result += f"  - {ingredient}\n"
        result += f"\n"
        result += f"Cuisine Type:  {cuisine_type}\n"
        result += f"Meal Type:  {meal_type}\n"
        result += f"Dish Type:  {dish_type}\n"
        result += f"Calories:  {calories: .2f}\n"
        result += f"Image: {image}\n\n\n"

    return result

def get_next_message(recipes_data: dict):
    index = recipes_data["index"]
    messages = recipes_data["messages"]
    
    if index < len(messages):
        message = messages[index]
        recipes_data["index"] += 1
        return message if message else print("Error!")
    else:
        return None
















# split_messages = [
#     "**Meal: Chicken Curry**\n\nIngredients:\n  - 1 lb chicken breast\n  - 2 cups coconut milk\n  - 1 tbsp curry powder\n  - 1 tsp salt\n\nCuisine Type: Indian\nMeal Type: Dinner\nDish Type: Main course\nCalories: 500\n[Img](https://example.com/image1.jpg)",
#     "**Meal: Chicken Salad**\n\nIngredients:\n  - 2 cups mixed greens\n  - 1 cup grilled chicken\n  - 1/2 cup cherry tomatoes\n  - 1/4 cup feta cheese\n\nCuisine Type: Mediterranean\nMeal Type: Lunch\nDish Type: Salad\nCalories: 350\n[Img](https://example.com/image2.jpg)"
# ]

# recipes_index[message.chat.id] = {
#     "messages": split_messages,
#     "index": 0
# }