"""
CMSC 14100
Autumn 2024

Test code for Homework #2
"""
import hw2
import os
import sys

import pytest
import helpers

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position

MODULE = "hw2"

@pytest.mark.parametrize("a, x, expected",
                         [(0, 0, 0),
                          (5, 2, 12),
                          (5, 0, 0),
                          (9, 1, 10),
                          (9, -2, -20),
                          (-11, 2, -20)])
def test_add_one_and_multiply(a, x, expected):
    """
    Do a single test for Exercise 1: add_one_and_multiply
    """
    steps = [f"actual = hw2.add_one_and_multiply({a}, {x})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw2.add_one_and_multiply(a, x)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("x, expected",
                         [(11, True),
                          (22, True),
                          (44, True),
                          (99, True),
                          (12, False),
                          (21, False),
                          (58, False),
                          (85, False)])
def test_have_same_value(x, expected):
    """
    Do a single test for Exercise 2: have_same_value
    """
    steps = [f"actual = hw2.have_same_value({x})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw2.have_same_value(x)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("x, expected",
                         [(11, 11),
                          (22, 22),
                          (44, 44),
                          (99, 99),
                          (12, 21),
                          (21, 12),
                          (58, 85),
                          (85, 58)])
def test_swap_digits(x, expected):
    """
    Do a single test for Exercise 3: swap_digits
    """
    steps = [f"actual = hw2.swap_digits({x})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw2.swap_digits(x)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("x, expected",
                         [(11, 11),
                          (122, 122),
                          (1244, 1244),
                          (76599, 76599),
                          (12, 21),
                          (121, 112),
                          (4558, 4585),
                          (45685, 45658)])
def test_swap_last_two_digits(x, expected):
    """
    Do a single test for Exercise 4: swap_last_two_digits
    """
    steps = [f"actual = hw2.swap_last_two_digits({x})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw2.swap_last_two_digits(x)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("r, g, b, expected",
                         [(0, 0, 0, True),
                          (255, 255, 0, True),
                          (0, 255, 0, True),
                          (125, 125, 125, True),
                          ("H", 10, 0, False),
                          (255, -10, 0, False),
                          (0, 255, 256, False),
                          (0.5, 0, 0, False)])
def test_is_valid_color(r, g, b, expected):
    """
    Do a single test for Exercise 5: is_valid_color
    """
    steps = [f"actual = hw2.is_valid_color({r}, {g}, {b})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw2.is_valid_color(r, g, b)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("r, g, b, expected",
                         [(0, 0, 0, True),
                          (255, 255, 0, False),
                          (0, 255, 0, False),
                          (0, 255, 255, False),
                          (10, 10, 10, True),
                          (101, 101, 101, True)])
def test_is_grayscale(r, g, b, expected):
    """
    Do a single test for Exercise 6: is_grayscale
    """
    steps = [f"actual = hw2.is_grayscale({r}, {g}, {b})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw2.is_grayscale(r, g, b)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("r, g, b, expected",
                         [(0, 0, 0, False),
                          (255, 255, 0, True),
                          (0, 255, 0, True),
                          (255, 255, 255, False),
                          (10, 10, 10, True),
                          (101, 101, 101, True)])
def test_is_not_black_or_white(r, g, b, expected):
    """
    Do a single test for Exercise 7: is_not_black_or_white
    """
    steps = [f"actual = hw2.is_not_black_or_white({r}, {g}, {b})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw2.is_not_black_or_white(r, g, b)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("r1, g1, b1, r2, g2, b2, expected",
                         [(0, 0, 0, 0, 0, 1, 1.0),
                          (0, 0, 0, 255, 255, 255, 441.6729559300637),
                          (10, 10, 10, 12, 12, 12, 3.4641016151377544),
                          (255, 255, 0, 255, 254, 0, 1.0),
                          (201, 201, 199, 201, 201, 202, 3.0)])
def test_compute_similarity_v1(r1, g1, b1, r2, g2, b2, expected):
    """
    Do a single test for Exercise 8: compute_similarity_v1
    """
    steps = [f"actual = hw2.compute_similarity_v1({r1}, {g1}, {b1}, {r2}, {g2}, {b2})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw2.compute_similarity_v1(r1, g1, b1, r2, g2, b2)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.parametrize("r1, g1, b1, r2, g2, b2, expected",
                         [(0, 0, 0, 0, 0, 1, 0.33166247903553997),
                          (0, 0, 0, 255, 255, 255, 255.0),
                          (10, 10, 10, 12, 12, 12, 2.0),
                          (255, 255, 0, 255, 254, 0, 0.7681145747868608),
                          (201, 201, 199, 201, 201, 202, 0.99498743710662)])
def test_compute_similarity_v2(r1, g1, b1, r2, g2, b2, expected):
    """
    Do a single test for Exercise 9: compute_similarity_v2
    """
    steps = [f"actual = hw2.compute_similarity_v2({r1}, {g1}, {b1}, {r2}, {g2}, {b2})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        actual = hw2.compute_similarity_v2(r1, g1, b1, r2, g2, b2)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)
    
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)