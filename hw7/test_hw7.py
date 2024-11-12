"""
CMSC 14100
Autumn 2024

Test code for Homework #7: Voter class
"""
import os
import sys
import pytest
import helpers

import hw7
import image_helpers as ih
from vector import Vector

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position

MODULE = "hw7"

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
MEDIUM_GRAY = (127, 127, 127)

####################################################################
#                                                                  #
#  Test code for the Color class                                   #
#                                                                  #
####################################################################

@pytest.mark.timeout(60)
@pytest.mark.parametrize("rgb, exception_expected",
                         [(BLACK, False),
                          ((1.1, 100, 200), True),
                          ((10, 2.1, 200), True),
                          ((10, 20, 200.7), True),
                          ((260, 50, 200), True),
                          ((10, 500, 200), True),
                          ((10, 50, 2000), True),
                          ])
def test_color_constructor(rgb, exception_expected):
    """ Test code for the required assertions in Color constuctor """
    red, green, blue = rgb
    steps = [f"c = hw7.Color({red}, {green}, {blue})"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        hw7.Color(red, green, blue)
    except AssertionError as exc:
        if exception_expected:
            return
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg,
                                                               exc)
    except Exception:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg,
                                                               exc)

    if exception_expected:
        err_msg = ("Your constructor did not raise an AssertionError as "
                   "expected for this test case.\n")
        pytest.fail(err_msg + recreate_msg)

    # Add an explicit return here, since there is a return in the try.
    return


@pytest.mark.timeout(60)
@pytest.mark.parametrize("rgb",
                         [BLACK,
                          RED,
                          GREEN,
                          BLUE,
                          MEDIUM_GRAY
                          ])
def test_get_as_vector(rgb):
    """ Test code for Color class get_as_vector method """
    red, green, blue = rgb
    steps = [f"c = hw7.Color({red}, {green}, {blue})",
              "v = c.get_as_vector()"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        color = hw7.Color(red, green, blue)
        vec = color.get_as_vector()
    except Exception as exc:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, exc)

    err_msg = helpers.check_result(vec, Vector(rgb))
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.timeout(60)
@pytest.mark.parametrize("rgb, expected",
                         [(BLACK, True),
                          (WHITE, True),
                          (MEDIUM_GRAY, True),
                          (RED, False),
                          (GREEN, False),
                          (BLUE, False)
                         ])
def test_color_is_grayscale(rgb, expected):
    """ Test code for Color class is_grayscale method """
    red, green, blue = rgb
    steps = [f"c = hw7.Color({red}, {green}, {blue})",
              "actual = c.is_grayscale()"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    try:
        color = hw7.Color(red, green, blue)
        actual = color.is_grayscale()
    except Exception as exc:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, exc)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.timeout(60)
@pytest.mark.parametrize("rgb, expected",
                         [(BLACK, "(0, 0, 0)"),
                          (RED, "(255, 0, 0)"),
                          (GREEN, "(0, 255, 0)"),
                          (BLUE, "(0, 0, 255)"),
                          (MEDIUM_GRAY, "(127, 127, 127)")
                          ])
def test_color_str(rgb, expected):
    """ Test code for Color __str__ method """
    red, green, blue = rgb
    steps = [f"c = hw7.Color({red}, {green}, {blue})",
              "actual = str(c)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    try:
        color = hw7.Color(red, green, blue)
        actual = str(color)
    except Exception as exc:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, exc)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.timeout(60)
@pytest.mark.parametrize("rgb, expected",
                         [(BLACK, "Color(0, 0, 0)"),
                          (RED, "Color(255, 0, 0)"),
                          (GREEN, "Color(0, 255, 0)"),
                          (BLUE, "Color(0, 0, 255)"),
                          (MEDIUM_GRAY, "Color(127, 127, 127)")
                          ])
def test_color_repr(rgb, expected):
    """ Test code for Color __repr__ method """
    red, green, blue = rgb
    steps = [f"c = hw7.Color({red}, {green}, {blue})",
              "actual = repr(c)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    try:
        color = hw7.Color(red, green, blue)
        actual = repr(color)
    except Exception as exc:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg,
                                                               exc)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.timeout(60)
@pytest.mark.parametrize("rgb1, rgb2",
                         [(RED, RED),
                          (GREEN, GREEN),
                          (BLUE, BLUE),
                          (RED, GREEN),
                          (RED, BLUE),
                          (BLUE, GREEN),
                          (WHITE, BLACK),
                          (BLACK, WHITE),
                          (WHITE, WHITE),
                          (BLACK, BLACK),
                          ((10, 20, 0), (10, 21, 30)),
                          ((100, 200, 10), (101, 200, 0)),
                          ((100, 200, 50), (101, 201, 50))
                          ])
def test_color_eq(rgb1, rgb2):
    """ Test code for Color __eq__ method """
    red1, green1, blue1 = rgb1
    red2, green2, blue2 = rgb2
    steps = [f"c1 = hw7.Color({red1}, {green1}, {blue1})",
             f"c2 = hw7.Color({red2}, {green2}, {blue2})",
              "actual = (c1 == c2)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    try:
        color1 = hw7.Color(red1, green1, blue1)
        color2 = hw7.Color(red2, green2, blue2)
        actual = (color1 == color2)
    except Exception as exc:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg,
                                                               exc)

    expected = (rgb1 == rgb2)
    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)



####################################################################
#                                                                  #
#  Test code for the Image class                                   #
#                                                                  #
####################################################################

def check_pixels(actual, expected):
    """
    Check whether the actual and expected pixels are the same.

    Args:
        actual (List[List[Color]]): the actual pixels to check
        expected (List[List[Color]]): the expected pixels

    Returns (str | None): returns None if the actual and expected
       pixels are the same or an error message, if they are different.
    """
    err_msg = helpers.check_2D_general(lambda v:isinstance(v, hw7.Color),
                                       "Color",
                                       lambda a, e: a == e,
                                       actual,
                                       expected)
    if err_msg is not None:
        # Hack to improve readability in the error message
        err_msg = err_msg.replace("value: ", "value: Color")
        return "\n\n" + err_msg

    return None


@pytest.mark.timeout(60)
@pytest.mark.parametrize("filename",
                          # square image
                         ["test_images/all_white_10_by_10.ppm",
                          # more rows than columns
                          "test_images/checkerboard_green.ppm",
                          # more columns than rows
                          "test_images/blue_ish_img.ppm",
                           # 1 x 1 image
                          "test_images/one_not_quite_yellow.ppm"
                          ])
def test_get_pixels(filename):
    """ Test code for Image get_pixels method """
    steps = [ "import image_helpers as ih",
             f"img = ih.load_image('{filename}')",
              "actual = img.get_pixels()"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)
    # get the image as pixels...
    expected = ih.load_image(filename, True)

    try:
        # load the image a second time to allow us to ensure that
        # a defensive copy was made.
        img = hw7.Image(expected)
        actual = img.get_pixels()
    except Exception as exc:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg,
                                                               exc)

    err_msg = check_pixels(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

    # Verify that a deep copy was done.
    if actual is expected:
        err_msg = ("The pixels returned from get_pixels refers to the\n"
                   "same list as the pixels passed into the Image constructor.\n"
                   "The Image constructor is required to make a deep copy\n"
                   "of the pixels.\n")
        pytest.fail(err_msg + recreate_msg)

    for i, row in enumerate(expected):
        if actual[i] is row:
            err_msg = ( "The pixels returned from get_pixels appears to be a shallow copy\n"
                        "of the pixels that were passed to the Image consructor.  For example,\n"
                       f"Row {i} of the actual pixels refers to the the same list as row {i}\n"
                        "of pixels that were passed to the Image constructor")
            pytest.fail(err_msg + recreate_msg)

@pytest.mark.timeout(60)
@pytest.mark.parametrize("filename, expected",
                          # square image
                         [("test_images/all_white_10_by_10.ppm", (10, 10)),
                          # more rows than columns
                          ("test_images/checkerboard_green.ppm", (6, 5)),
                          # more columns than rows
                          ("test_images/blue_ish_img.ppm", (5, 6)),
                          # 1 x 1 image
                          ("test_images/one_not_quite_yellow.ppm", (1, 1))
                          ])
def test_get_shape(filename, expected):
    """ Test code for Image get_shape method """
    steps = [ "import image_helpers as ih",
             f"img = ih.load_image('{filename}')",
              "actual = img.get_shape()"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        img = ih.load_image(filename)
        actual = img.get_shape()
    except Exception as exc:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg,
                                                               exc)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.timeout(60)
@pytest.mark.parametrize("filename, expected",
                         [("test_images/all_white_10_by_10.ppm", True),
                          ("test_images/random_gray_8_by_8.ppm", True),
                          ("test_images/random_gray_8_by_7.ppm", True),
                          ("test_images/random_gray_7_by_10.ppm", True),
                          ("test_images/nearly_all_gray_0.ppm", False),
                          ("test_images/nearly_all_gray_1.ppm", False),
                          ("test_images/nearly_all_gray_2.ppm", False),
                          ("test_images/one_not_quite_yellow.ppm", False),
                          ])
def test_is_grayscale_image(filename, expected):
    """ Test code for Image is_grayscale method """
    steps = [ "import image_helpers as ih",
             f"img = ih.load_image('{filename}')",
              "actual = img.is_grayscale()"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        img = ih.load_image(filename)
        actual = img.is_grayscale()
    except Exception as exc:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg,
                                                               exc)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.timeout(60)
@pytest.mark.parametrize("input_filename, loc, height, width",
                         [("test_images/checkerboard_green.ppm", (0, 0), 6, 5),
                          ("test_images/checkerboard_green.ppm", (0, 0), 1, 2),
                          ("test_images/checkerboard_green.ppm", (1, 1), 4, 3),
                          ("test_images/checkerboard_green.ppm", (1, 1), 10, 10),
                          ("test_images/checkerboard_green.ppm", (5, 4), 2, 2),
                          ("test_images/blue_ish_img.ppm", (4, 0), 1, 6),
                          ("test_images/blue_ish_img.ppm", (0, 5), 10, 10)
                          ])
def test_crop(input_filename, loc, height, width):
    """ Test code for Image crop method """
    row, col = loc
    output_filename = input_filename[:-len(".ppm")] \
        + f"_cropped_{row}_{col}_{height}_{width}.ppm"

    steps = [ "import image_helpers as ih",
             f"img = ih.load_image('{input_filename}')",
             f"img.crop({loc}, {height}, {width})",
              "actual_pixels = img.get_pixels()",
             f"expected_pixels = ih.load_image('{output_filename}', True)"]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    try:
        img = ih.load_image(input_filename)
        img.crop(loc, height, width)
    except Exception as exc:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg,
                                                               exc)


    expected_pixels = ih.load_image(output_filename, True)
    actual_pixels = img.get_pixels()
    if actual_pixels is None:
        err_msg = ("The test code for the crop method relies on the get_pixels "
                   "method.\nIt appears that you have not implemented it yet.")
        pytest.fail(err_msg + recreate_msg)

    err_msg = check_pixels(actual_pixels, expected_pixels)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.timeout(60)
@pytest.mark.parametrize("input_filename, size",
                         [("test_images/two_by_two.ppm", 1),
                          ("test_images/two_by_two.ppm", 2),
                          ("test_images/three_by_three.ppm", 3),
                          ("test_images/two_by_three.ppm", 2),
                          ("test_images/three_by_two.ppm", 2),
                          ("test_images/random_gray_7_by_10.ppm", 4),
                          ("test_images/random_gray_8_by_7.ppm", 4),
                          ("test_images/random_gray_8_by_8.ppm", 4),
                          ("test_images/checkerboard_green.ppm", 1),
                          ("test_images/checkerboard_green.ppm", 2),
                          ("test_images/checkerboard_green.ppm", 5),
                          ("test_images/checkerboard_green.ppm", 6),
                          ])

def test_down_sample(input_filename, size):
    """ Test code for Image downsample method """
    output_filename = input_filename[:-len(".ppm")] + f"_ds_{size}.ppm"

    steps = [ "import image_helpers as ih",
             f"img = ih.load_image('{input_filename}')",
             f"actual_img = img.down_sample({size})",
             f"expected_img = ih.load_image('{output_filename}', False)",
              "# Rememember that you can use the get_pixels method to see the",
              "# pixels from the two different images."]             
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    expected_pixels = ih.load_image(output_filename, True)
    expected_img = hw7.Image(expected_pixels)

    try:
        img = ih.load_image(input_filename)
        actual_img = img.down_sample(size)
    except Exception as exc:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, exc)

    # verify that the value that was returned from down_sample
    # was not None.
    err_msg = helpers.check_none(actual_img, expected_img)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

    # verify that the value returned from down_sample has the
    # right type.
    err_msg = helpers.check_type(actual_img, expected_img)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)        

    actual_pixels = actual_img.get_pixels()
    if actual_pixels is None:
        err_msg = ("The test code for the downsample method relies on the "
                   "get_pixels method.\nIt appears that you have not "
                   "implemented it yet.")
        pytest.fail(err_msg + recreate_msg)
    expected_pixels = ih.load_image(output_filename, True)

    err_msg = check_pixels(actual_pixels, expected_pixels)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)
