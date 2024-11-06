"""
CMSC 14100
Autumn 2024

Functions for reading from a json file. 
"""
import sys
import json


def load_recipes(filename):
    """
    Load json data from a file.

    Args:
        filename (str): name of the json file

    Returns (List[Dict]): A list of dictionaries, where each row
        in the json file is stored in a dictionary.
    """
    assert filename.endswith(".json")

    try:
        with open(filename) as f:
            data = json.load(f)
    except OSError:
        print(f"Cannot open {filename}")
        sys.exit(1)
    
    return data


def print_recipe(recipe):
    """
    Print the recipe.

    Args:
        recipe (Dict): a recipe
    """
    print(json.dumps(recipe, indent=4))