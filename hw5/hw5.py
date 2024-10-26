"""
CMSC 14100
Autumn 2024
Homework #5

We will be using anonymous grading, so please do NOT include your name
in this file

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URL of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

class Color:
    """
    Class for representing colors using the RGB color model.

    Do not modify this class.
    """

    def __init__(self, r, g, b):
        """
        Construct an instance of Color

        Args:
            r (int): the value for the red channel
            g (int): the value for the green channel
            b (int): the value for the blue channel
        """
        assert isinstance(r, int) and (0 <= r <= 255)
        assert isinstance(g, int) and (0 <= g <= 255)
        assert isinstance(b, int) and (0 <= b <= 255)
        self.r = r
        self.g = g
        self.b = b

    def __repr__(self):
        """
        Create a developer-facing string for the instance.
        """
        return f"Color({self.r}, {self.g}, {self.b})"


# Exercise 1
def get_brightness(color):
    """
    Calculate the perceived brightness of an RGB color using the
    formula: (0.21 x R) + (0.72 x G) + (0.07 x B).

    Args:
        color (Color): a color

    Returns (float): The brightness of a color.
    """
    ### YOUR CODE HERE
    return None


# Exercise 2
def is_valid_image(image):
    """
    Determine whether or not an image is valid. A valid image is a rectangular
    list of lists of Colors.

    Args:
        image (Any): an image that may or may not be valid

    Returns (bool): True if image is valid, False otherwise.
    """
    ### YOUR CODE HERE
    return None


# Exercise 3
def is_portrait_or_landscape(image):
    """
    Determine whether or not an image is a portrait (taller than it is wide)
    or a landscape (wider than it is tall).

    Args:
        image (List[List[Color]]): an image

    Returns (string): "Portrait" if the image is a portrait, "Landscape" if
        the image is a landscape. Return "Neither" if the image is neither
        portrait or landscape.
    """
    ### YOUR CODE HERE
    return None


# Exercise 4
def is_horizontally_striped(image):
    """
    Determine whether or not an image is horizontally striped.

    Args:
        image (List[List[Color]]): an image

    Returns (bool): True if the image is horizontally striped, False otherwise.
    """
    ### YOUR CODE HERE
    return None


# Exercise 5
def find_vertical_stripes(image):
    """
    Create a list of integers where each integer in the output list is
    a column number that is a vertical stripe.

    Args:
        image (List[List[Color]]): an image

    Returns (List[int]): The column numbers for solid stripes.
    """
    ### YOUR CODE HERE
    return None


# Exercise 6
def get_pixel_brightness(image):
    """
    Create a list of lists of floats, where each float is the brightness
    of the corresponding pixel in the image.

    Args:
        image (List[List[Color]]): an image

    Returns (List[List[float]]): The brightness of each pixel in an image.
    """
    ### YOUR CODE HERE
    return None


# Exercise 7 helper function
# Do not modify this function.
def make_gray(color):
    """
    Create the gray version of a color. A color is gray if all R, G, and
    B components are equal. To create a grayscale version of a non-gray color,
    average the R, G, and B components using NTSC weights.

    Args:
        color (Color): a color

    Returns (Color): The gray version of a color.
    """
    ntsc = (0.299 * color.r) + (0.587 * color.g) + (0.114 * color.b)
    gray = int(ntsc//3)
    return Color(gray, gray, gray)


# Exercise 7
def make_image_gray(image):
    """
    Create the grayscale version of an image. That is, for each pixel
    in the image, modify its value so that it is a gray color.

    Args:
        image (List[List[Color]]): an image

    Returns (None): Nothing, modifies image in-place.
    """
    ### YOUR CODE HERE
    return None


# Exercise 8
def find_brightest_location_in_region(image, upper_left, width):
    """
    Given an image and a description of a region, find the location of the
    brightest location in each region.

    Args:
        image (List[List[Color]]): an image
        upper_left (Tuple[int, int]): upper left corner of a region
        width (int): width of a region

    Returns (Tuple[int, int]): The location of the brightest pixel in
        the region.
    """
    ### YOUR CODE HERE
    return None
