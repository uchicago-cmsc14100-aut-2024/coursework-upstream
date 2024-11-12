"""
CMSC 14100
Autumn 2024
Homework #7

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

from vector import Vector

class Color:
    """
    A (very) minimal class for representing (immutable) colors.
    """

    def __init__(self, red, green, blue):
        """
        Constructor for Color

        Args:
           red (int): red channel for the color.
           green (int): green channel for the color.
           blue (int): blue channel for the color
        """
        ### YOUR CODE HERE
        pass

    def get_as_vector(self):
        """
        Return the channels of the color as an instance of the Vector class
        """
        ### YOUR CODE HERE
        pass

    def is_grayscale(self):
        """
        Is the color a grayscale color, that is, do all the channels
        have the same value?

        Returns (bool): True, if the channels have the same value,
            False otherwise.
        """
        ### YOUR CODE HERE
        pass

    def __str__(self):
        """
        Returns (str): a client-facing string for this instance of the
        Color class.
        """
        ### YOUR CODE HERE
        pass

    def __repr__(self):
        """
        Returns (str): a developer-facing string for this instance of the
        Color class.
        """
        ### YOUR CODE HERE
        pass

    def __eq__(self, other):
        """
        Are the two colors the same?

        Returns (bool): True if the two colors are the same,
            and False otherwise
        """
        ### YOUR CODE HERE
        pass


class Image:
    """
    Class to represent an image
    """

    def __init__(self, pixels):
        """
        Constructor

        Args:
            pixels (List[List[Color]]): color values for each pixel in the image
        """
        # You may assume that the list of pixels is well-formed.
        # That is, pixels is a list with at least one element and all the
        # elements are lists of the same length and that they all hold
        # instances/objects of the Color class.

        ### YOUR CODE HERE
        pass

    def get_pixels(self):
        """ Returns (List[List[Color]]): the pixels """
        ### YOUR CODE HERE
        pass

    def get_shape(self):
        """
        Returns (Tuple[int, int]): a tuple with the height and
            width of the image
        """
        ### YOUR CODE HERE
        pass

    def is_grayscale(self):
        """
        Is the image a gray scale image?

        Returns (bool): True, if all the colors in the image
            are grayscale colors and False, otherwise.
        """
        ### YOUR CODE HERE
        pass

    def crop(self, loc, height, width):
        """
        Crop the image in-place to contain only the pixels in the
        specified region.

        Args:
            loc (Tuple[int, int]): the location of the top-left corner of
                the region
            height (int): the height of the region in pixels
            width (int): the width of the region in pixels
        """
        ### YOUR CODE HERE
        pass

    def down_sample(self, size):
        """
        Computes a down-sampled verion of the image by averaging the colors
        in tiles of the specified size. The tiles on the bottom and right edge
        of the image may have fewer than size x size colors.

        Args:
            size (int): the size of the tiles

        Returns (Image): the downsampled image.
        """
        assert size >= 1
        ### YOUR CODE HERE
        pass


    # Recommended but not required
    def __str__(self):
        """
        Returns a client-facing string for the Image. Our implementation
        returns a string that lists the shape of the image and then each
        row in the image on its own line, with the colors represented using
        tuples and separated by spaces.
        """
        pass
