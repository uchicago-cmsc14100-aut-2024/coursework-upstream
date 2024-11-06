"""
CMSC 14100
Autumn 2024
Homework #6

We will be using anonymous grading, so please do NOT include your name
in this file.

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

#############################################################################
#                                                                           #
# Important note: some of the tasks in this assignment have task-specific   #
# requirements/restrictions concerning the language constructs that you are #
# allowed to use in your solution. See the assignment writeup for details.  #
#                                                                           #
#############################################################################


# Constants
MAX_NUM_INGREDIENTS = 5
MAX_NUM_INSTRUCTIONS = 6


# Exercise 1
def is_easy(recipe, max_num_ingredients, max_num_instructions):
    """
    Check whether a recipe is easy or not. A recipe is considered easy if its 
    ingredients do not exceed the maximum number of ingredients and its 
    instructions do not exceed the maximum number of instructions.

    Args:
        recipe (Dict[str, Any]): a recipe
        max_num_ingredients (int): the maximum number of ingredients allowed
        max_num_instructions (int): the maximum number of steps allowed

    Returns (bool): True if the recipe is easy, False otherwise
    """
    ### YOUR CODE HERE

    
# Exercise 2
def are_same(recipe1, recipe2):
    """
    Given two recipes, check whether the recipes have the same titles, the same 
    set of ingredients, and the same list of instructions.
    
    You should consider the recipes to be the same if they have the same set of
    ingredients, even if the order of the ingredients is different. For example,
    the ingredients lists ["sugar", "flour"] and ["flour", "sugar"] are 
    considered to be the same.

    Args:
        recipe1 (Dict[str, Any]): a recipe
        recipe2 (Dict[str, Any]): another recipe

    Returns (bool): True if the recipes are the same, False otherwise
    """
    ### YOUR CODE HERE


# Exercise 3
def add_metadata(recipes):
    """
    Given a list of recipes, add new key-value pairs to each recipe that
    indicates the number of instructions, the number of ingredients in the 
    recipe, and the difficulty of the recipe.
    
    Args:
        recipes (List[Dict[str, Any]]): a list of recipes
        
    Returns (None): Nothing, modifies input in-place

    """
    ### YOUR CODE HERE


# Exercise 4
def search_by_ingredients(recipes, favorite_ingredients):
    """
    Given a list of recipes and a list of favorite ingredients, return a list of 
    recipe titles that use all of the specified ingredients.

    Args:
        recipes (List[Dict[str, Any]]): a list of recipes
        favorite_ingredients (List[str]): a list of favorite ingredients

    Returns (List[str]): a list of recipe titles that use all
        specified ingredients
    """
    ### YOUR CODE HERE


# Helper function for testing count_ingredients
# Used for testing purposes only
def get_most_common_items(counts, k):
    """
    Given a dictionary of counts, return the k most common items that appear
    more than once.
    
    Args:
        counts (Dict[str, int]): a dictionary where the key is an item and the
            value is the count
        k (int): the number of most common items to return
        
    Returns (Dict[str, int]): a dictionary where the key is an item and the
        value is the count
    """
    most_common_items = sorted(counts.items(), key=lambda x: x[1],
                               reverse=True)[:k]
    
    # Filter out items that appear only once
    most_common_items = [(item, count) for item, count in most_common_items \
                              if count > 1]
    
    # Convert it to a dictionary
    most_common_items = dict(most_common_items)
    
    return most_common_items


# Exercise 5
def count_ingredients(recipes):
    """
    Given a list of recipes, count the number of occurrances of all ingredients 
    across the recipes.

    Args:
        recipes (List[Dict[str, Any]]): a list of recipes

    Returns (Dict[str, int]): a dictionary where the key is an ingredient and
        the value is the number of occurrances of that ingredient across all
        recipes
    """
    ### YOUR CODE HERE


# Exercise 6
def map_ingredients_to_recipes(recipes):
    """
    Given a list of recipes, create a dictionary where the key is an ingredient
    and the value is a list of recipes that contain that ingredient.

    Args:
        recipes (List[Dict[str, Any]]): a list of recipes

    Returns (Dict[str, List[str]): a dictionary where the key is an
        ingredient and the value is a list of recipe titles that contain
        that ingredient
    """
    ### YOUR CODE HERE


# Exercise 7
def create_custom_recipe_book(recipes, difficulty, favorite_ingredients):
    """
    Given a list of recipes, the desired difficulty level, and favorite 
    ingredients to include, return a subset of the recipes that meet the 
    constraints. The function returns a dictionary where the key is the recipe 
    title and the value is the recipe that satisfies the constraints along with 
    its metadata.
    
    Args:
        recipes (List[Dict[str, Any]]): a list of recipes
        difficulty (str): the difficulty level of the recipes
        favorite_ingredients (List[str]): a list of favorite ingredients to 
            be included in the recipes
        
    Returns Dict[str, Dict[str, Any]]: a dictionary where the key is the recipe 
        title and the value is the recipe that satisfies the constraints along 
        with its metadata
    """
    ### YOUR CODE HERE
