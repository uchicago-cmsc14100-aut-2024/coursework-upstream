"""
CMSC 14100
Autumn 2024

Test code for Homework #5
"""

import copy
import json
import os
import sys
import traceback
import pytest
import helpers as helpers
import image_helpers as ih


# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position
import hw5
from hw5 import Color

MODULE = "hw5"

# Color constants
RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)
YELLOW = Color(255, 255, 0)
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)


# Stolen from helpers.py. This is a hack because Color has no __eq__ method.
# The str trick is explicitly disallowed for students in the writeup.
def check_2D_list_unmodified_str(param_name, before, after):
    """
    Generate an error if a list of lists was modified when modifications
    are disallowed.
    """
    return helpers.check_2D_list_unmodified(param_name, before, after,
                                            lambda x, y: str(x) != str(y))


@pytest.mark.parametrize("r, g, b, expected",
                         [(0, 0, 0, float(0)),
                          (255, 255, 255, 254.99999999999997),
                          (0, 255, 0, 183.6),
                          (10, 10, 10, 9.999999999999998),
                          (0, 100, 255, 89.85),
                          (200, 200, 10, 186.7),
                          (200, 200, 255, 203.85),
                          (201, 201, 199, 200.86),
                          (201, 255, 100, 232.81)])
def test_get_brightness(r, g, b, expected):
    """
    Test code for Exercise 1: get_brightness
    """
    steps = [f"color = hw5.Color({r}, {g}, {b})",
             f"actual = hw5.get_brightness(color)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        color = hw5.Color(r, g, b)
        actual = hw5.get_brightness(color)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


IMAGE1 = 5
IMAGE2 = []
IMAGE3 = [10, 20, 30]
IMAGE4 = [[1, 2, 3], [4, 5, 6]]
IMAGE5 = [[WHITE, 5], [BLACK, 10], [WHITE, 15]]
IMAGE6 = [[WHITE, BLACK], [BLACK, WHITE], [WHITE, 5]]
IMAGE7 = [[(255, 0, 0), (255, 0, 0)], [(0, 0, 255), (0, 0, 255)]]
IMAGE8 = [[WHITE, BLACK], [WHITE, BLACK], 10, [WHITE, BLACK]]
IMAGE9 = [[WHITE, BLACK, WHITE], [BLACK, WHITE], [WHITE, BLACK, WHITE]]
IMAGE10 = [[WHITE, BLACK], [WHITE, BLACK, WHITE], [WHITE, BLACK, WHITE]]
IMAGE11 = [[WHITE, BLACK, WHITE], [WHITE, BLACK, WHITE], [WHITE, BLACK, WHITE]]
IMAGE12 = [[WHITE, BLACK], [BLACK, WHITE], [WHITE, BLACK]]
IMAGE13 = ih.load_image("tests/checkerboard_green.ppm")
IMAGE14 = ih.load_image("tests/checkerboard_black.ppm")
IMAGE15 = ih.load_image("tests/stripes.ppm")
IMAGE16 = ih.load_image("tests/pseudo_stripes.ppm")
IMAGE17 = ih.load_image("tests/one_pixel.ppm") # one pixel
IMAGE18 = ih.load_image("tests/horizontal_stripe5.ppm") # one pixel tall
IMAGE19 = ih.load_image("tests/portrait2.ppm") # one pixel wide

@pytest.mark.timeout(60)
@pytest.mark.parametrize("in_image, expected",
                         [(IMAGE1, False),
                          (IMAGE2, False),
                          (IMAGE3, False),
                          (IMAGE4, False),
                          (IMAGE5, False),
                          (IMAGE6, False),
                          (IMAGE7, False),
                          (IMAGE8, False),
                          (IMAGE9, False),
                          (IMAGE10, False),
                          (IMAGE11, True),
                          (IMAGE12, True),
                          (IMAGE13, True),
                          (IMAGE14, True),
                          (IMAGE15, True),
                          (IMAGE16, True),
                          (IMAGE17, True),
                          (IMAGE18, True),
                          (IMAGE19, True)]
                         )
def test_is_valid_image(in_image, expected):
    """
    Test code for Exercise 2: is_valid_image
    """
    steps = [f"image = {in_image}",
             f"actual = hw5.is_valid_image(image)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    image = in_image

    try:
        actual = hw5.is_valid_image(image)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.timeout(60)
@pytest.mark.parametrize("filename, expected",
    [("tests/square1.ppm", "Neither"),
     ("tests/square2.ppm", "Neither"),
     ("tests/square3.ppm", "Neither"),
     ("tests/one_pixel.ppm", "Neither"),
     ("tests/portrait1.ppm", "Portrait"),
     ("tests/portrait2.ppm", "Portrait"),
     ("tests/portrait3.ppm", "Portrait"),
     ("tests/portrait4.ppm", "Portrait"),
     ("tests/landscape1.ppm", "Landscape"),
     ("tests/landscape2.ppm", "Landscape"),
     ("tests/landscape3.ppm", "Landscape"),
     ("tests/horizontal_stripe5.ppm", "Landscape")]
     )
def test_is_portrait_or_landscape(filename, expected):
    """
    Test code for Exercise 3: is_portrait_or_landscape
    """
    steps = [f"import image_helpers as ih",
             f"image = ih.load_image('{filename}')",
             f"actual = hw5.is_portrait_or_landscape(image)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    image = ih.load_image(filename)
    image_copy = copy.deepcopy(image) # check that the image wasn't modified

    try:
        actual = hw5.is_portrait_or_landscape(image)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

    err_msg = check_2D_list_unmodified_str("image", image_copy, image)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

@pytest.mark.parametrize("image",
                         [(IMAGE9), (IMAGE10)])
def test_is_portrait_or_landscape_valid(image):
    """
    Test for: assert is_valid_image(image)
    """
    steps = [f"import image_helpers as ih",
             f"image = {image}",
             f"actual = hw5.is_portrait_or_landscape(image)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    
    try:
        actual = hw5.is_portrait_or_landscape(image)
    except Exception as AssertionError:
        return # correct
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = "\n\nInput image is invalid."
    err_msg += "\n  Expected: AssertionError"

    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.timeout(60)
@pytest.mark.parametrize("filename, expected",
    [("tests/horizontal_stripe1.ppm", True),
     ("tests/horizontal_stripe2.ppm", True),
     ("tests/horizontal_stripe3.ppm", True),
     ("tests/horizontal_stripe4.ppm", True),
     ("tests/horizontal_stripe5.ppm", False),
     ("tests/horizontal_stripe6.ppm", False),
     ("tests/horizontal_stripe7.ppm", False),
     ("tests/horizontal_stripe8.ppm", False),
     ("tests/horizontal_stripe9.ppm", False),
     ("tests/one_pixel.ppm", True),
     ("tests/portrait2.ppm", True)]
     )
def test_is_horizontally_striped(filename, expected):
    """
    Test code for Exercise 4: is_horizontally_striped
    """
    steps = [f"import image_helpers as ih",
             f"image = ih.load_image('{filename}')",
             f"actual = hw5.is_horizontally_striped(image)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    image = ih.load_image(filename)
    image_copy = copy.deepcopy(image) # check that the image wasn't modified

    try:
        actual = hw5.is_horizontally_striped(image)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

    err_msg = check_2D_list_unmodified_str("image", image_copy, image)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

@pytest.mark.parametrize("image",
                         [(IMAGE9), (IMAGE10)])
def test_is_horizontally_striped_valid(image):
    """
    Test for: assert is_valid_image(image)
    """
    steps = [f"import image_helpers as ih",
             f"image = {image}",
             f"actual = hw5.is_horizontally_striped(image)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    
    try:
        actual = hw5.is_horizontally_striped(image)
    except Exception as AssertionError:
        return # correct
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = "\n\nInput image is invalid."
    err_msg += "\n  Expected: AssertionError"

    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.timeout(60)
@pytest.mark.parametrize("filename, expected",
    [("tests/horizontal_stripe1.ppm", [0, 1, 2]),
     ("tests/horizontal_stripe4.ppm", []),
     ("tests/horizontal_stripe5.ppm", [0, 1, 2, 3, 4, 5, 6]),
     ("tests/square3.ppm", [0, 5]),
     ("tests/vertical_stripe1.ppm", [1, 3]),
     ("tests/vertical_stripe2.ppm", [0, 2]),
     ("tests/one_pixel.ppm", [0]),
     ("tests/portrait2.ppm", [])]
     )
def test_find_vertical_stripes(filename, expected):
    """
    Test code for Exercise 5: find_vertical_stripes
    """
    steps = [f"import image_helpers as ih",
             f"image = ih.load_image('{filename}')",
             f"actual = hw5.find_vertical_stripes(image)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    image = ih.load_image(filename)
    image_copy = copy.deepcopy(image) # check that the image wasn't modified

    try:
        actual = hw5.find_vertical_stripes(image)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

    err_msg = check_2D_list_unmodified_str("image", image_copy, image)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

@pytest.mark.parametrize("image",
                         [(IMAGE9), (IMAGE10)])
def test_find_vertical_stripes_valid(image):
    """
    Test for: assert is_valid_image(image)
    """
    steps = [f"import image_helpers as ih",
             f"image = {image}",
             f"actual = hw5.find_vertical_stripes(image)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    
    try:
        actual = hw5.find_vertical_stripes(image)
    except Exception as AssertionError:
        return # correct
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = "\n\nInput image is invalid."
    err_msg += "\n  Expected: AssertionError"

    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.timeout(60)
@pytest.mark.parametrize("filename, expected",
    [("tests/square1.ppm", [[53.55, 237.14999999999998], [183.6, 17.85]]),
     ("tests/brightness1.ppm", [[50.0, 100.0, 200.0], [1.0, 4.999999999999999, 9.999999999999998], [55.0, 65.0, 75.0]]),
     ("tests/brightness2.ppm", [[53.55, 17.85, 53.55], [201.45, 237.14999999999998, 71.4], [129.45, 216.14999999999998, 50.4], [194.45, 165.14999999999998, 64.4]]),
     ("tests/brightness3.ppm", [[53.55, 17.85, 53.55, 17.85, 53.55], [201.45, 237.14999999999998, 201.45, 237.14999999999998, 201.45], [53.55, 17.85, 53.55, 17.85, 53.55], [201.45, 237.14999999999998, 201.45, 237.14999999999998, 201.45]]),
     ("tests/one_pixel.ppm", [[53.55]]),
     ("tests/horizontal_stripe5.ppm", [[53.55, 17.85, 53.55, 17.85, 53.55, 17.85, 53.55]]),
     ("tests/portrait2.ppm", [[53.55], [17.85], [53.55], [17.85], [53.55], [17.85], [53.55]])]
     )
def test_get_pixel_brightness(filename, expected):
    """
    Test code for Exercise 6: get_pixel_brightness
    """
    steps = [f"import image_helpers as ih",
             f"image = ih.load_image('{filename}')",
             f"actual = hw5.get_pixel_brightness(image)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    image = ih.load_image(filename)
    image_copy = copy.deepcopy(image) # check that the image wasn't modified

    try:
        actual = hw5.get_pixel_brightness(image)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_2D_general(lambda v: isinstance(v, float),
                                       "float",
                                       lambda v1, v2: pytest.approx(v1) == v2,
                                       actual,
                                       expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

    err_msg = check_2D_list_unmodified_str("image", image_copy, image)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

@pytest.mark.parametrize("image",
                         [(IMAGE9), (IMAGE10)])
def test_get_pixel_brightness_valid(image):
    """
    Test for: assert is_valid_image(image)
    """
    steps = [f"import image_helpers as ih",
             f"image = {image}",
             f"actual = hw5.get_pixel_brightness(image)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    
    try:
        actual = hw5.get_pixel_brightness(image)
    except Exception as AssertionError:
        return # correct
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = "\n\nInput image is invalid."
    err_msg += "\n  Expected: AssertionError"

    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.timeout(60)
@pytest.mark.parametrize("filename, expected",
    [("tests/square1.ppm", [[Color(25, 25, 25), Color(75, 75, 75)], [Color(49, 49, 49), Color(9, 9, 9)]]),
     ("tests/brightness1.ppm", [[Color(16, 16, 16), Color(33, 33, 33), Color(66, 66, 66)], [Color(0, 0, 0), Color(1, 1, 1), Color(3, 3, 3)], [Color(18, 18, 18), Color(21, 21, 21), Color(25, 25, 25)]]),
     ("tests/brightness2.ppm", [[Color(25, 25, 25), Color(9, 9, 9), Color(25, 25, 25)], [Color(59, 59, 59), Color(75, 75, 75), Color(35, 35, 35)], [Color(40, 40, 40), Color(65, 65, 65), Color(25, 25, 25)], [Color(55, 55, 55), Color(55, 55, 55), Color(31, 31, 31)]]),
     ("tests/brightness3.ppm", [[Color(25, 25, 25), Color(9, 9, 9), Color(25, 25, 25), Color(9, 9, 9), Color(25, 25, 25)], [Color(59, 59, 59), Color(75, 75, 75), Color(59, 59, 59), Color(75, 75, 75), Color(59, 59, 59)], [Color(25, 25, 25), Color(9, 9, 9), Color(25, 25, 25), Color(9, 9, 9), Color(25, 25, 25)], [Color(59, 59, 59), Color(75, 75, 75), Color(59, 59, 59), Color(75, 75, 75), Color(59, 59, 59)]]),
     ("tests/one_pixel.ppm", [[Color(25, 25, 25)]]),
     ("tests/horizontal_stripe5.ppm", [[Color(25, 25, 25), Color(9, 9, 9), Color(25, 25, 25), Color(9, 9, 9), Color(25, 25, 25), Color(9, 9, 9), Color(25, 25, 25)]]),
     ("tests/portrait2.ppm", [[Color(25, 25, 25)], [Color(9, 9, 9)], [Color(25, 25, 25)], [Color(9, 9, 9)], [Color(25, 25, 25)], [Color(9, 9, 9)], [Color(25, 25, 25)]])]
     )
def test_make_image_gray(filename, expected):
    """
    Test code for Exercise 7: make_image_gray
    """
    steps = [f"import image_helpers as ih",
             f"image = ih.load_image('{filename}')",
             f"hw5.make_image_gray(image)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    image = ih.load_image(filename)
    
    try:
        hw5.make_image_gray(image)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)


    err_msg = helpers.check_2D_general(lambda e: isinstance(e, hw5.Color),
                                       "Color",
                                       lambda c1, c2: str(c1) == str(c2),
                                       image,
                                       expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)
        
    """
    # Now check that the updated image has the right value
    # This is a hack. Color does not have a __eq__ method.
    err_msg = helpers.__check_2D_vals(lambda c1, c2: str(c1) == str(c2), image, expected)
    """

@pytest.mark.parametrize("image",
                         [(IMAGE9), (IMAGE10)])
def test_make_image_gray_valid(image):
    """
    Test for: assert is_valid_image(image)
    """
    steps = [f"import image_helpers as ih",
             f"image = {image}",
             f"actual = hw5.make_image_gray(image)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    
    try:
        actual = hw5.make_image_gray(image)
    except Exception as AssertionError:
        return # correct
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = "\n\nInput image is invalid."
    err_msg += "\n  Expected: AssertionError"

    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

@pytest.mark.timeout(60)
@pytest.mark.parametrize("filename, upper_left, width, expected",
                         [("tests/brightness1.ppm", (0, 0), 1, (0, 0)),
                          ("tests/brightness1.ppm", (0, 0), 2, (0, 1)),
                          ("tests/brightness1.ppm", (0, 0), 3, (0, 2)),
                          ("tests/brightness1.ppm", (1, 0), 2, (2, 1)),
                          ("tests/brightness1.ppm", (1, 1), 2, (2, 2)),
                          ("tests/brightness2.ppm", (0, 0), 3, (1, 1)),
                          ("tests/brightness2.ppm", (0, 0), 4, (1, 1)), # off on the right
                          ("tests/brightness2.ppm", (1, -1), 3, (1, 1)), # off on the left
                          ("tests/brightness1.ppm", (-2, 1), 3, (0, 2)), # off on the top
                          ("tests/brightness2.ppm", (3, 1), 2, (3, 1)), # off on the bottom
                          ("tests/brightness2.ppm", (2, 1), 3, (2, 1)), # combination
                          ("tests/brightness2.ppm", (-1, -3), 10, (1, 1)), # all
                          ("tests/checkerboard_black.ppm", (0, 0), 3, (1, 2))]) # tie
def test_find_brightest_location_in_region(filename, upper_left, width, expected):
    """
    Test code for Exercise 8: find_brightest_location_in_region
    """
    steps = [f"import image_helpers as ih",
             f"image = ih.load_image('{filename}')",
             f"hw5.find_brightest_location_in_region(image, {upper_left}, {width})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    image = ih.load_image(filename)
    image_copy = copy.deepcopy(image) # check that the image wasn't modified

    try:
        actual = hw5.find_brightest_location_in_region(image, upper_left, width)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

    err_msg = check_2D_list_unmodified_str("image", image_copy, image)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

@pytest.mark.parametrize("image",
                         [(IMAGE9), (IMAGE10)])
def test_find_brightest_location_in_region_valid(image):
    """
    Test for: assert is_valid_image(image)
    """
    steps = [f"import image_helpers as ih",
             f"image = {image}",
             f"actual = hw5.find_brightest_location_in_region(image)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    
    try:
        actual = hw5.find_brightest_location_in_region(image)
    except Exception as AssertionError:
        return # correct
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = "\n\nInput image is invalid."
    err_msg += "\n  Expected: AssertionError"

    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)
