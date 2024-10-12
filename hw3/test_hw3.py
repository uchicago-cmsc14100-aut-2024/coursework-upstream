"""
CMSC 14100
Updated Spring 2024

Test code for Homework #3
"""
import os
import sys

import pytest

import hw3
import helpers

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position

MODULE = "hw3"

# Some useful constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
MEDIUM_GRAY = (127, 127, 127)
PURPLE = (160, 32, 240)

@pytest.mark.parametrize("r, g, b, expected",
                         [(0, 0, 0, True),
                          (10, 10, 10, True),
                          (255, 255, 255, True),
                          (0, 0, 10, False),
                          (10, 0, 0, False),
                          (10, 0, 10, False)])
def test_is_grayscale(r, g, b, expected):
    """ Test code for is_grayscale """
    steps = [f"actual = hw3.is_grayscale({r}, {g}, {b})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw3.is_grayscale(r, g, b)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("r, g, b, expected",
                         [(0, 0, 0, True),
                          (255, 0, 0, False),
                          (0, 255, 0, False),
                          (0, 255, 255, False),
                          (10, 10, 10, False),
                          (255, 255, 255, True),
                          (0, 0, 255, False),
                          (255, 0, 255, False),
                          (255, 255, 0, False),
                          (10, 255, 0, False)])
def test_is_black_or_white(r, g, b, expected):
    """ Test code for is_black_or_white """
    steps = [f"actual = hw3.is_black_or_white(({r}, {g}, {b}))"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw3.is_black_or_white((r, g, b))
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("lst, expected",
                         [([], 0),
                          ([WHITE], 0),
                          ([BLACK], 0),
                          ([PURPLE], 1),
                          ([WHITE, BLACK, BLACK, WHITE, RED], 1),
                          ([GREEN, BLACK, BLACK, WHITE, BLACK], 1),
                          ([GREEN, BLACK, BLACK, WHITE, BLUE], 2),
                          ([PURPLE, MEDIUM_GRAY, RED, BLUE, GREEN], 5)])
def test_count_not_black_or_white(lst, expected):
    """ Test code for count_not_black_or_white """
    steps = [f"lst = {lst}",
             f"actual = hw3.count_not_black_or_white(lst)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw3.count_not_black_or_white(lst)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


first_tests = [([], -10, 10, hw3.NEITHER),
               ([-21], -20, 10, hw3.LOWER),
               ([-20], -20, 10, hw3.NEITHER),
               ([10], -10, 10, hw3.NEITHER),
               ([20], -10, 10, hw3.UPPER),
               ([10, 20, 15, 0, -1, 1, 12, 13], 0, 21, hw3.LOWER),
               ([10, 20, 15, 0, -1, -1, -12, -13], 0, 21, hw3.LOWER),
               ([10, 20, 15, 0, -1, -1, -12, -13], -12, 21, hw3.LOWER),
               ([10, 20, 15, 0, -1, 1, 12, 13], 0, 19, hw3.UPPER),
               ([0, 19, 19, 19, 100, 0, 19, 0, 1000], 0, 19, hw3.UPPER),
               ([0, 19, 19, 19, 0, 0, 19, 0, 1000], 0, 19, hw3.UPPER),
               ([10, 20, 15, 0, -1, 1, 12, 13], -2, 100, hw3.NEITHER),
               ([12, 13, 5, 16, 25, 0], 10, 20, hw3.LOWER),
               ([12, 13, 25, 5, 16, 0], 10, 20, hw3.UPPER),
               ([12, 13, 14], 10, 20, hw3.NEITHER),
               ([-14, -15, -25, 5], -20, -5, hw3.LOWER),
               ([-14, -4, 10], -20, -5, hw3.UPPER),
               ([-12, -13, -14], -20, -5, hw3.NEITHER)
               ]
@pytest.mark.parametrize("lst, lower, upper, expected", first_tests)
def test_which_comes_first_break(lst, lower, upper, expected):
    """ Test code for which_comes_first_break """
    steps = [f"lst = {lst}",
             f"actual = hw3.which_comes_first_break(lst, {lower}, {upper})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw3.which_comes_first_break(lst, lower, upper)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("lst, lower, upper, expected", first_tests)
def test_which_comes_first_return(lst, lower, upper, expected):
    """ Test code for which_comes_first_return """
    steps = [f"lst = {lst}",
             f"actual = hw3.which_comes_first_return(lst, {lower}, {upper})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw3.which_comes_first_return(lst, lower, upper)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


last_tests = [([], -10, 10, hw3.NEITHER),
              ([-21], -20, 10, hw3.LOWER),
              ([-20], -20, 10, hw3.NEITHER),
              ([10], -10, 10, hw3.NEITHER),
              ([20], -10, 10, hw3.UPPER),
              ([10, 20, 15, 0, -1, 1, 12, 13], 0, 21, hw3.LOWER),
              ([10, 20, 15, 0, -1, -1, -12, -13], 0, 21, hw3.LOWER),
              ([-21, 20, 15, 0, -1, -1, -12, -13], -20, 21, hw3.LOWER),
              ([10, 20, 15, 0, 1, 1, 12, 13], 0, 19, hw3.UPPER),
              ([0, 19, 19, 19, 100, -10, 19, -20, 1000], 0, 19, hw3.UPPER),
              ([20, 19, 19, 19, 0, 0, 19, 0, 19], 0, 19, hw3.UPPER),
              ([10, 20, 15, 0, -1, 1, 12, 13], -2, 100, hw3.NEITHER)
              ]
@pytest.mark.parametrize("lst, lower, upper, expected", last_tests)
def test_which_comes_last(lst, lower, upper, expected):
    """ Test code for which_comes_last """
    steps = [f"lst = {lst}",
             f"actual = hw3.which_comes_last(lst, {lower}, {upper})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw3.which_comes_last(lst, lower, upper)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("lst, expected",
                         [([], True),
                          ([50], True),
                          ([50, 100], False),
                          ([100]*10, True),
                          ([50]*5 + [10], False),
                          ([50]*3 + [10] + [50]*3, False),
                          ([10] + [200]*5, False),
                          ])
def test_are_all_same(lst, expected):
    """ Test code for are_all_same """
    steps = [f"lst = {lst}",
             f"actual = hw3.are_all_same(lst)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw3.are_all_same(lst)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)



score_tests = [([], -10, 10, 5, False),

               # 1 less than lower
               ([-21], -20, 10, 10, False),
               # 1 equal to lower
               ([-20], -20, 10, 10, False),
               # 1 equal to upper
               ([10], -10, 10, 5, False),
               # 1 greater than upper
               ([20], -10, 10, 20, True),

               # 1 less than lower, 1 greater than upper
               ([-10, 10], 0, 9, 5, False),
               # 0 less than lower, 1 greater than upper
               ([-10, 10], -11, 9, 5, True),
               # 1 less than lower, 0 greater than upper
               ([-10, 10], -9, 10, 5, False),

               # 0 less than lower, 1 greater than upper
               ([10, 20, 15, 0, -1, -1, -12, -13], -1, 9, 3, True),
               # 1 less than lower (first one), 0 greater than upper
               ([-21, 20, 15, 0, -1, -1, -12, -13], -20, 21, 4, False),
               # 1 less than lower, 3 greater than upper
               ([20, 20, 15, 0, 1, -1, 12, 20], 0, 19, 5, True),
               # 2 less than lower, 2 greater than upper
               ([0, 19, 19, 19, 100, -10, 19, -20, 1000], 0, 19, 10, False),
               # 0 less than lower, 1 greater than upper (first one)
               ([20, 19, 19, 19, 0, 0, 19, 0, 19], 0, 19, 3, True),
               # 0 less than lower, 0 less than upper
               ([10, 20, 15, 0, -1, 1, 12, 13], -2, 100, 3, False),
               # all greater than upper
               ([10, 20, 30, 40, 50], 0, 9, 10, True),
               # all less than lower
               ([-1, -2, -3], 0, 10, 10, False)
              ]
@pytest.mark.parametrize("lst, lower, upper, bonus, bonus_expected",
                         score_tests)
def test_compute_final_score(lst, lower, upper, bonus, bonus_expected):
    """ Test code for compute_final_score """
    steps = \
        [f"lst = {lst}",
         f"actual = hw3.compute_final_score(lst, {lower}, {upper}, {bonus})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw3.compute_final_score(lst, lower, upper, bonus)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    expected = sum(lst) + (bonus if bonus_expected else 0)
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("lst, expected",
                         [([], None),
                          ([WHITE], 0),
                          ([BLACK], 0),
                          ([RED], None),
                          ([RED, BLACK, WHITE], 1),
                          ([BLUE, BLUE, BLUE, WHITE, BLUE, BLUE], 3),
                          ([GREEN] + [WHITE]*5, 1),
                          ([BLUE, GREEN, BLUE, BLUE, BLACK, GREEN, MEDIUM_GRAY,
                            WHITE, BLACK], 4),
                          ([GREEN]*10 + [WHITE], 10),
                          ([BLACK]*5, 0),
                          ([RED]*3, None)
                         ])
def test_get_first_bw_idx(lst, expected):
    """ Test code for get_first_bw_idx """
    steps = [f"lst = {lst}",
             f"actual = hw3.get_first_bw_idx(lst)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw3.get_first_bw_idx(lst)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)
