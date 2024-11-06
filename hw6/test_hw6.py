"""
CMSC 14100
Updated Autumn 2024

Test code for Homework #6
"""
import hw6
import recipe_helpers as rh

import os
import sys
import pytest
import helpers

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position

MODULE = "hw6"

def get_test_data(filename):
    """
    Read the test data from a csv file
    """
    try:
        return rh.load_recipes(os.path.join("data", filename))
    except FileNotFoundError as e:
        print(f"Cannot open test file: {filename}", file=sys.stderr)
        sys.exit(1)
        

def check_unmodified(filename, idx, param_name, after):
    """
    Verify that a parameter has not been changed.
    """
    before = get_test_data(filename)
    if idx is not None:
        before = before[idx]

    msg = f'\n\nYou modified the parameter {param_name}, which is not allowed.\n'
    if len(str(before)) < 100 and len(str(after)) < 100:
        msg += f'  Value before your code: {before}\n'
        msg += f'  Value after your code:  {after}'

    if before != after:
        return msg
    else:
        return None

def check_list_of_recipes(actual, expected, checking_return_type):
    """
    Verify that the recipes in actual match the recipes in expected
    """
    err_msg = helpers.check_none(actual, expected)
    if expected is None or err_msg is not None:
        return err_msg

    err_msg = helpers.check_type(actual, expected, checking_return_type)
    if err_msg is not None:
        return err_msg

    # Check that the actual value is the correct length
    err_msg = helpers.__check_list_length(actual, expected)
    if err_msg is not None:
        return err_msg


    # Check the individual recipes
    for idx, actual_recipe in enumerate(actual):
        err_msg = helpers.check_dict(actual_recipe, expected[idx])
        if err_msg is not None:
            err_msg = f"Problem with recipe at index {idx}:" + \
                err_msg.replace("\n", "\n    ")
            return err_msg
    return None
    

@pytest.mark.parametrize("recipe_index, max_num_ingredients, max_num_instructions",
                         [(0, 0, 1),
                          (0, 3, 0),
                          (0, -100, 0),
                          (0, 100, -50),
                          (0, -100, -50),
                          (0, "recipe", 5),
                          (0, 6, 7.0),
                         ])
def test_is_easy_valid(recipe_index, max_num_ingredients, max_num_instructions):
    """ Test code for is_easy (test invalid inputs) """
    steps = [
        "import recipe_helpers as rh",
        "recipes = rh.load_recipes('data/recipes_3.json')",
        f"actual = hw6.is_easy(recipes[{recipe_index}], {max_num_ingredients}, {max_num_instructions})"
    ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    recipes = get_test_data("recipes_3.json")

    try:
        actual = hw6.is_easy(recipes[recipe_index], max_num_ingredients, max_num_instructions)
    except Exception as AssertionError:
        return # correct behavior
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = "\n\nis_easy called with invalid input."
    err_msg += "\n  Expected: AssertionError"
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("recipe_index, max_num_ingredients, max_num_instructions, expected",
                         [(0, 5, 6, True),
                          (0, 5, 5, False),
                          (0, 10, 20, True),
                          (1, 6, 6, False),
                          (1, 100, 100, True),
                          (2, 2, 2, False),
                          (2, 11, 3, True),])
def test_is_easy(recipe_index, max_num_ingredients, max_num_instructions, expected):
    """ Test code for is_easy """
    steps = [
        "import recipe_helpers as rh",
        "recipes = rh.load_recipes('data/recipes_3.json')",
        f"actual = hw6.is_easy(recipes[{recipe_index}], {max_num_ingredients}, {max_num_instructions})"
    ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    recipes = get_test_data("recipes_3.json")

    try:
        actual = hw6.is_easy(recipes[recipe_index], max_num_ingredients, max_num_instructions)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

    # verify that recipes argument was not modified
    err_msg = check_unmodified("recipes_3.json", recipe_index, "recipe", recipes[recipe_index])
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)        
        


@pytest.mark.parametrize("recipe_index1, recipe_index2, expected",
                         [(0, 0, True),
                          (0, 1, False),
                          (0, 2, True),
                          (0, 3, False),
                          (0, 4, False),
                          (0, 5, False),])
def test_are_same(recipe_index1, recipe_index2, expected):
    """ Test code for are_same """
    steps = [
        "import recipe_helpers as rh",
        "repeated_recipes = rh.load_recipes('data/repeated_recipes.json')",
        f"actual = hw6.are_same(repeated_recipes[{recipe_index1}], repeated_recipes[{recipe_index2}])"
    ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    repeated_recipes = get_test_data("repeated_recipes.json")

    try:
        actual = hw6.are_same(repeated_recipes[recipe_index1], repeated_recipes[recipe_index2])
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)
        
    # verify that recipe1 argument was not modified
    err_msg = check_unmodified("repeated_recipes.json", recipe_index1, "recipe1",
                               repeated_recipes[recipe_index1])
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)        

    # verify that recipe2 argument was not modified
    err_msg = check_unmodified("repeated_recipes.json", recipe_index2, "recipe2",
                               repeated_recipes[recipe_index2])
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)        


@pytest.mark.parametrize("original_filename",
                         [('recipes_1.json'),
                          ('recipes_3.json'),
                          ('recipes_5.json'),
                          ('recipes_10.json'),])
def test_add_metadata(original_filename):
    """ Test code for add_metadata """
    steps = [
        "import recipe_helpers as rh",
        f"recipes = rh.load_recipes('data/{original_filename}')",
        "hw6.add_metadata(recipes)",
        "actual = recipes"
    ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    recipes = get_test_data(original_filename)
    try:
        hw6.add_metadata(recipes)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    test_case_name = original_filename.replace(".json", "")
    expected = get_test_data("recipes_with_metadata.json")[test_case_name]

    # Check the individual recipes
    err_msg = check_list_of_recipes(recipes, expected, False)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("original_filename, ingredients",
                         [("recipes_1.json", ["crackers"]),
                          ("recipes_3.json", ["vanilla"]),
                          ("recipes_3.json", ["sugar"]),
                          ("recipes_3.json", ["pumpkin", "vanilla"]),
                          ("recipes_3.json", []),
                          ("recipes_10.json", ["eggs"]),
                          ("recipes_10.json", ["eggs", "margarine", "kidney beans"]),])
    
def test_search_by_ingredients(original_filename, ingredients):
    """ Test code for search_by_ingredients """
    
    steps = [
        "import recipe_helpers as rh",
        f"recipes = rh.load_recipes('data/{original_filename}')",
        f"actual = hw6.search_by_ingredients(recipes, {ingredients})"
    ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    
    recipes = get_test_data(original_filename)
    ingredients_copy = ingredients[:]

    try:
        actual = hw6.search_by_ingredients(recipes, ingredients)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    test_case_name = original_filename.replace(".json", "") + "_" + \
        ("_".join(ingredients) if ingredients else "none")
    expected = get_test_data("recipes_by_ingredients.json")[test_case_name]

    err_msg = helpers.check_1d_iterable(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)
        
    # verify that recipes argument was not modified
    err_msg = check_unmodified(original_filename, None, "recipes", recipes)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)        

    # verify that ingredients argument was not modified
    err_msg = helpers.check_list_unmodified("ingredients",
                                    ingredients_copy, ingredients)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)        



@pytest.mark.parametrize("original_filename",
                         [('recipes_1.json'),
                          ('recipes_3.json'),
                          ('recipes_5.json'),
                          ('recipes_10.json'),
                          ('recipes_100.json')])
def test_count_ingredients(original_filename):
    """ Test code for count_ingredients """
    steps = [
        "import recipe_helpers as rh",
        f"recipes = rh.load_recipes('data/{original_filename}')",
        f"actual = hw6.count_ingredients(recipes)"
    ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    recipes = get_test_data(original_filename)
    
    try:
        actual = hw6.count_ingredients(recipes)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    test_case_name = original_filename.replace(".json", "")
    expected = get_test_data("recipes_with_counts.json")[test_case_name]
    err_msg = helpers.check_dict(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)
        
    # verify that recipes argument was not modified
    err_msg = check_unmodified(original_filename, None, "recipes", recipes)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)        
        

@pytest.mark.parametrize("original_filename",
                         [('recipes_1.json'),
                          ('recipes_3.json'),
                          ('recipes_10.json'),
                          ('recipes_100.json')])
def test_map_ingredients_to_recipes(original_filename):
    """ Test code for map_ingredients_to_recipes """
    steps = [
        "import recipe_helpers as rh",
        f"recipes = rh.load_recipes('data/{original_filename}')",
        f"actual = hw6.map_ingredients_to_recipes(recipes)"
    ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    recipes = get_test_data(original_filename)
    try:
        actual = hw6.map_ingredients_to_recipes(recipes)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    test_case_name = original_filename.replace(".json", "")
    expected = get_test_data("ingredients_to_recipes.json")[test_case_name]
    err_msg = helpers.check_dict(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

    # verify that recipes argument was not modified
    err_msg = check_unmodified(original_filename, None, "recipes", recipes)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)        
        
        
        
@pytest.mark.parametrize("original_filename, difficulty, ingredients",
                         [("recipes_1.json", "", ["vanilla"]),
                          ("recipes_3.json", "easy", ["vanilla"]),
                          ("recipes_3.json", "easy", ["pumpkin"]),
                          ("recipes_10.json", "hard", []),
                          ("recipes_3.json", "medium", []),
                          ("repeated_recipes.json", "easy", ["vanilla"]),
                          ("recipes_100.json", "hard", ["eggs", "flour"]),
                          ("recipes_100.json", "hard", ["eggs", "flour", "milk", "salt", "love"])])
def test_create_custom_recipe_book(original_filename, difficulty, ingredients):
    """ Test code for create_custom_recipe_book """
    
    steps = [
        "import recipe_helpers as rh",
        f"recipes = rh.load_recipes('data/{original_filename}')",
        f"actual = hw6.create_custom_recipe_book(recipes, '{difficulty}', {ingredients})"
    ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    recipes = get_test_data(original_filename)
    ingredients_copy = ingredients[:]

    try:
        actual = hw6.create_custom_recipe_book(recipes, difficulty, ingredients)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    test_case_name = (
        original_filename.replace(".json", "") + 
        (f"_{difficulty}_" if difficulty else "_none_") + 
        ("_".join(ingredients) if ingredients else "none")
    )
    expected = get_test_data("custom_recipe_books.json")[test_case_name]
    err_msg = helpers.check_dict(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

    # verify that ingredients argument was not modified
    err_msg = helpers.check_list_unmodified("ingredients",
                                            ingredients_copy, ingredients)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)        
        
        
