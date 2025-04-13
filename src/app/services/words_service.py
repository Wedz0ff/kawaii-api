import json
import random
from src.data import JP_FILE_PATH, DE_FILE_PATH


def get_random_jp_word(level: int = None):
    """
    Reads the JSON file and returns a random word.
    If a level is provided, filters the words by the given level.
    """
    try:
        # Open and load the JSON file
        with open(JP_FILE_PATH, "r", encoding="utf-8") as file:
            words = json.load(file)

        # Filter words by level if a level is provided
        if level is not None:
            words = [word for word in words if word.get("level") == level]

        # If no words match the level, raise an exception
        if not words:
            raise ValueError(f"No words found for level {level}")

        # Return a random word from the filtered list
        return random.choice(words)
    except FileNotFoundError:
        raise Exception(f"Data file not found at {JP_FILE_PATH}")
    except json.JSONDecodeError:
        raise Exception("Error decoding JSON file")


def get_random_de_word(level: str = None):
    """
    Reads the German JSON file and returns a random word.
    If a level is provided, filters the words by the given level.
    """
    try:
        # Open and load the JSON file
        with open(DE_FILE_PATH, "r", encoding="utf-8") as file:
            words = json.load(file)

        # Filter words by level if a level is provided
        if level is not None:
            words = [word for word in words if word.get("level") == level]

        # If no words match the level, raise an exception
        if not words:
            raise ValueError(f"No words found for level {level}")

        # Return a random word from the filtered list
        return random.choice(words)
    except FileNotFoundError:
        raise Exception(f"Data file not found at {DE_FILE_PATH}")
    except json.JSONDecodeError:
        raise Exception("Error decoding JSON file")
