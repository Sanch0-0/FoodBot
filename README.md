# FoodBot

FoodBot is a bot that sends you recipes of food based on an entered keyword. For example, typing 'chicken' will return various chicken recipes.

## Project Structure

- **main.py**: This file runs the code to start the bot.
- **.env.example**: Rename this file to `.env` and fill in the necessary environment variables.
- **bot.py**: Contains the logic of the bot.
- **recipes.py**: Parses recipes from the Edamam API.
- **requirements.txt**: Contains the list of required libraries.

## Getting Started

### Prerequisites

Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/FoodBot.git
   cd FoodBot

2. **Create a virtual environment:**
    ```bash
    python -m venv venv

3. **Activate the virtual environment:**
    ```bash
    venv\Scripts\activate  #On Windows

    source venv/bin/activate #On macOs/Linux

4. **Install the required libraries:**
    ```bash
    pip install -r requirements.txt

5. **Rename .env.example to .env and fill in the required environment variables.**

## Running the Bot 

**Run the following command to start the bot:**

    python main.py

