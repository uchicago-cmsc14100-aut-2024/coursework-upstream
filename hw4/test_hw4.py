"""
CMSC 14100
Updated Spring 2024

Test code for Homework #4
"""

import hw4
import json
import os
import random
import sys
import pytest
import helpers
import copy


# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position

MODULE = "hw4"

# Some useful constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
MEDIUM_GRAY = (127, 127, 127)
PURPLE = (160, 32, 240)

def get_test_data(filename):
    """
    Read the test data from a json file
    """
    try:
        with open(filename) as f:
            return json.load(f)
    except FileNotFoundError as e:
        print(f"Cannot open test file: {filename}", file=sys.stderr)
        sys.exit(1)


@pytest.mark.parametrize("color, expected",
                         [(WHITE, "255 255 255"),
                          (PURPLE, "160 32 240")])
def test_color_to_str(color, expected):
    """ Test code for color_to_str """
    steps = [f"actual = hw4.color_to_str({color})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw4.color_to_str(color)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

@pytest.mark.parametrize("colors, expected",
                         [([], ""),
                          ([WHITE], "255 255 255"),
                          ([PURPLE], "160 32 240"),
                          ([BLUE, RED, GREEN, PURPLE],
                           '0 0 255 255 0 0 0 255 0 160 32 240')])
def test_convert_color_list_to_str(colors, expected):
    """ Test code for convert_color_list_to_str """
    steps = [f"actual = hw4.convert_color_list_to_str({colors})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    colors_copy = colors[:]

    try:
        actual = hw4.convert_color_list_to_str(colors)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

    err_msg = helpers.check_list_unmodified("colors",
                                            colors_copy,
                                            colors)
    if err_msg:
        pytest.fail(err_msg + recreate_msg)



@pytest.mark.parametrize("colors, rep_count, expected",
                         [([], 3, []),
                          ([WHITE], 1, [WHITE]),
                          ([PURPLE], 4,  [PURPLE, PURPLE, PURPLE, PURPLE]),
                          ([GREEN, GREEN], 3, [GREEN]*6),
                          ([BLUE, RED, GREEN, PURPLE], 2,
                           [BLUE, BLUE, RED, RED, GREEN, GREEN, PURPLE, PURPLE])])
def test_replicate_colors_in_list(colors, rep_count, expected):
    """ Test code for replicate_colors_in_list """
    steps = [f"colors = {colors}",
             f"actual = hw4.replicate_colors_in_list(colors, {rep_count})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    colors_copy = colors[:]
    
    try:
        actual = hw4.replicate_colors_in_list(colors, rep_count)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_1d_iterable(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

    err_msg = helpers.check_list_unmodified("colors",
                                            colors_copy,
                                            colors)
    if err_msg:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("colors, expected",
                         [([WHITE], [hw4.FILL_COLOR, WHITE, hw4.FILL_COLOR]),
                          ([PURPLE], [hw4.FILL_COLOR, PURPLE, hw4.FILL_COLOR]),
                          ([GREEN, GREEN], [hw4.FILL_COLOR, GREEN, hw4.FILL_COLOR, GREEN, hw4.FILL_COLOR]),
                          ([BLUE, RED, GREEN, PURPLE],
                           [hw4.FILL_COLOR, BLUE, hw4.FILL_COLOR, RED, hw4.FILL_COLOR, GREEN,
                            hw4.FILL_COLOR, PURPLE, hw4.FILL_COLOR]),
                         ([hw4.FILL_COLOR, BLUE, GREEN, hw4.FILL_COLOR],
                          [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 255), (0, 0, 0), (0, 255, 0),
                           (0, 0, 0), (0, 0, 0), (0, 0, 0)])]
                         )
def test_alternate_colors_with_fill(colors, expected):
    """ Test code for alternate_colors_with_fill """
    steps = [f"colors = {colors}",
             f"actual = hw4.alternate_colors_with_fill(colors)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    colors_copy = colors[:]

    try:
        actual = hw4.alternate_colors_with_fill(colors)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_1d_iterable(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


    err_msg = helpers.check_list_unmodified("colors",
                                            colors_copy,
                                            colors)
    if err_msg:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("colors, k, seed, expected",
                         [([WHITE], 1, 14003, [WHITE]),
                          ([PURPLE], 4, 14003, [PURPLE]*4),
                          ([GREEN, GREEN], 3, 14003, [GREEN]*3),
                          ([BLUE, RED, GREEN, PURPLE], 1, 14003, [(160, 32, 240)]),
                          ([BLUE, RED, GREEN, PURPLE], 3, 14003,
                           [(160, 32, 240), (255, 0, 0), (255, 0, 0)]),
                          ([BLUE, RED, GREEN, PURPLE], 7, 14003,
                           [(160, 32, 240), (255, 0, 0), (255, 0, 0),
                            (0, 0, 255), (255, 0, 0), (255, 0, 0), (160, 32, 240)]),
                          ([BLUE, RED, GREEN, PURPLE], 1, 27, [(160, 32, 240)]),
                          ([BLUE, RED, GREEN, PURPLE], 4, 27,
                            [(160, 32, 240), (0, 255, 0), (0, 255, 0), (255, 0, 0)]),
                          ([BLUE, RED, GREEN, PURPLE], 7, 27,
                           [(160, 32, 240), (0, 255, 0), (0, 255, 0),  (255, 0, 0),
                            (0, 0, 255), (0, 0, 255), (0, 255, 0)])
                           ])
def test_choose_colors(colors, k, seed, expected):
    """ Test code for choose_colors """
    steps = [f"import random",
             f"random.seed({seed})",
             f"colors = {colors}",
             f"actual = hw4.choose_colors(colors, {k})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    colors_copy = colors[:]

    try:
        random.seed(seed)
        actual = hw4.choose_colors(colors, k)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_1d_iterable(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)



@pytest.mark.parametrize("colors, block_width, section_height, add_fill, expected",
                         get_test_data("tests/make_section_no_randomize_tests.json"))
def test_section_no_randomize(colors, block_width, section_height, add_fill, expected):
    """ Test code for make_color_section with a value of False for the randomize parameter """
    steps = [f"colors = {colors}",
             f"actual = hw4.make_section(colors, {block_width}, {section_height}, {add_fill}, False)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    colors_copy = colors[:]

    try:
        actual = hw4.make_section(colors, block_width, section_height, add_fill, False)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_1d_iterable(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


    err_msg = helpers.check_list_unmodified("colors",
                                            colors_copy,
                                            colors)
    if err_msg:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("colors, block_width, section_height, add_fill, seed, expected",
                         get_test_data("tests/make_section_randomize_tests.json"))
def test_section_randomize(colors, block_width, section_height, add_fill, seed, expected):
    """ Test code for make_color_section with a value of True for the randomize parameter """
    steps = [f"colors = {colors}",
             f"random.seed({seed})"
             f"actual = hw4.make_section(colors, {block_width}, {section_height}, {add_fill}, True)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    colors_copy = colors[:]

    try:
        random.seed(seed)
        actual = hw4.make_section(colors, block_width, section_height, add_fill, True)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_1d_iterable(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

    err_msg = helpers.check_list_unmodified("colors",
                                            colors_copy,
                                            colors)
    if err_msg:
        pytest.fail(err_msg + recreate_msg)
        



@pytest.mark.parametrize("colors, block_size, num_sections, choose, seed, expected",
                         get_test_data("tests/make_grid_tests.json"))
def test_make_grid(colors, block_size, num_sections, choose, seed, expected):
    """ Test code for make_grid """
    steps = []
    if choose:
        steps.extend([f"import random",
                      f"random.seed({seed})"])
    steps.extend([f"colors = {colors}",
                  f"actual = hw4.make_grid(colors, {block_size}, {num_sections}, {choose})"])
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    colors_copy = colors[:]

    try:
        if choose:
            random.seed(seed)
        actual = hw4.make_grid(colors, block_size, num_sections, choose)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_1d_iterable(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

    err_msg = helpers.check_list_unmodified("colors",
                                            colors_copy,
                                            colors)
    if err_msg:
        pytest.fail(err_msg + recreate_msg)
        
