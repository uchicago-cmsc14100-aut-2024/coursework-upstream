"""
CMSC 14100
Autumn 2024
Homework #4

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

import random
import os
import sys

import click

# These constants have been included to simplify testing;
# they will not be used in your code.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
MEDIUM_GRAY = (127, 127, 127)
PURPLE = (160, 32, 240)

# This constant WILL be used in your code.
FILL_COLOR = (0, 0, 0)

# Exercise 1:
def color_to_str(color):
    """
    Convert an RGB color tuple into a string with the channels in RGB order
    separated by spaces.

    Args:
        color (Tuple[int, int, int]): the color tuple to convert

    Returns (str): the red, green, and blue channels of the color separated
        by spaces.
    """
    ### YOUR CODE HERE


# Exercise 2
def convert_color_list_to_str(colors):
    """
    Given a list of colors, create a string representing the colors in the list
    in the order that they appear separated by spaces.

    Args:
        colors: (List[Tuple[int, int, int]]): a list of colors

    Returns (str): a string with the RGB values of the colors separated by
        spaces.

    Sample use:
        convert_color_list_to_str([(10, 20, 30), (40, 50, 60), (70, 80, 90)])
        would yield '10 20 30 40 50 60 70 80 90'.
    """
    ### YOUR CODE HERE


# Exercise 3
def alternate_colors_with_fill(colors):
    """
    Given a list of colors, create a new list that interleaves
    the defined contstant FILL_COLOR with colors from the colors list,
    starting and ending with FILL_COLOR.

    Args:
        colors (List[Tuple[int, int, int]]): a non-empty list of colors

    Returns (List[Tuple[int, int, int]]): a list with colors from the input
        color list alternating with FILL_COLOR.
    """
    ### YOUR CODE HERE


# Exercise 4
def replicate_colors_in_list(colors, block_width):
    """
    Given a list of colors and the number of times each color should be
    repeated, generate a new list in which each color in the original list
    appears block_width times in the result.

    Args:
        colors (List[Tuple[int, int, int]]): the list of colors
        block_width (int): the number of times each color should appear

    Returns (List[Tuple[int, int, int]]): a new list of colors

    Sample use:
        replicate_colors_in_list([(100, 100, 100), (200, 200, 200)], 3)
        would yield the list: [(100, 100, 100), (100, 100, 100),
            (100, 100, 100), (200, 200, 200), (200, 200, 200), (200, 200, 200)].
    """
    ### YOUR CODE HERE


# Exercise 5
def make_section(colors, block_width, section_height, add_fill, randomize):
    """
    Make a section of the image.

    Args:
        colors (List[Tuple[int, int, int]]): the list of colors
        block_width (int): the number of times each color should be replicated
           when constructing a row in the image.
        section_height (int): the number of rows in the section
        add_fill (bool): add alternating fill if True, do nothing if False.
        randomize (bool): randomly choose the colors for the section if True,
            use the colors in the order they are provided if False.

    Returns (List[str]): the section image represents as a list of strings.
    """
    ### YOUR CODE HERE


# Exercise 6
def choose_colors(colors, k):
    """
    Given a list of colors, construct a new list of colors by choosing k
    colors randomly (as described in the writeup).

    Args:
        colors (List[Tuple[int, int, int]]): a non-empty list of colors to use
            as the color palette
        k (int): the number of colors to choose

    Returns (List[Tuple[int, int, int]]): a list of k colors chosen using
        uniform sampling with replacement.
    """
    ### YOUR CODE HERE


# Exercise 7
def make_grid(colors, block_size, number_of_color_sections, randomize):
    """
    Construct a grid image.

    Args:
        colors (List[Tuple[int, int, int]]): a non-empty list of colors to use
            as the color palette
        block_size (int): value to use for both the block width and the
            section height for the sections in the grid
        number_of_color_sections (int): the number of color sections to
            include in the grid
        randomize (bool): True, if the colors for each section should be chosen
            randomly.  False, if the original order should be used for
            every section.

    Returns (List[str]): the grid image represented as a list of strings.
    """
    ### YOUR CODE HERE


########################################################
### Do not modify any of the code below                #
########################################################

def write_image_ppm(image, filename):
    """
    Write an image in PPM format to a file.

    Args:
        image (List[str]): the image as a list of strings, where each
           element is a string of integers representing RGB values.
        filename (str): the name of the file to write

    Returns (None): no return value
    """
    try:
        with open(filename, "w") as file_ptr:
            # print PPM header
            print("P3", file=file_ptr)
            width = len(image[0].split()) // 3
            height = len(image)
            print(width, height, file=file_ptr)
            print(255, file=file_ptr)

            for row in image:
                print(row, file=file_ptr)
    except IOError:
        print("Could not open {filename}")


@click.command()
@click.option("-c", "--colors-filename", required=True, type=str,
              help="The name of the file with colors.")
@click.option("-f", "--output-filename", type=str, required=True,
              help="The name of the file to use for output.")
@click.option("-s", "--stripes", is_flag=True, default=False,
              help="Generate a stripes image.")
@click.option("-a", "--alternating-stripes", is_flag=True, default=False,
              help="Generate an alternating stripes image.")
@click.option("-g", "--grid", is_flag=True, default=False,
              help="Generate a grid image.")
@click.option("-r", "--randomize", is_flag=True, default=False,
              help="Randomize the order of the colors.")
@click.option("-n", "--number-of-color-sections", type=int, default=1,
              help=("The number of color sections to include "
                    "in the output. Default: 1"))
def cmd(colors_filename, output_filename, stripes, alternating_stripes, grid,
        randomize, number_of_color_sections):
    """
    Generate an image and print it out in PPM format.  The arguments
    are parsed using the Click library.

    Args:
        colors_filename (str): the name of the file contains the colors to use
        output_filename (str): the name of the output file
        stripes (bool): will be True, if the users wants to construct a
            stripes image (default: False)
        alternating_stripes (bool): will be True, if the users wants to
            construct a stripe image (default: False)
        grid (bool): will be True, if the user wants to construct a grid image
            (default: False)
        randomize (bool): will be True if the user wants to use randomization
            in a grid image (default: False)
        number_of_sections (int): the number of color sections the user wants
            in the final image  (default: 1)

    Returns: None
    """
    if os.path.isfile(colors_filename):
        with open(colors_filename) as file_ptr:
            colors = [tuple([int(x) for x in l.split()]) for l in file_ptr]
    else:
        print("Error: Cannot open file:", output_filename, file=sys.stderr)
        sys.exit(1)

    if ((stripes and (alternating_stripes or grid)) or
        (alternating_stripes and grid)):
        print("Error:Only one of -s, -a, and -g can be used.", file=sys.stderr)
        sys.exit(2)

    # hardcode the block size for simplicity
    block_size = 25
    if stripes or alternating_stripes:
        image = make_section(colors,
                             block_size,
                             number_of_color_sections * block_size,
                             alternating_stripes,
                             randomize)
    elif grid:
        image = make_grid(colors, block_size, number_of_color_sections,
                          randomize)
    else:
        print(("Error: One of stripes (-a), alternating stripes (-s), "
               "or grid (-g) must be specified."), file=sys.stderr)
        sys.exit(3)

    if image:
        write_image_ppm(image, output_filename)
    else:
        print("Error:make_grid returned None", file=sys.stderr)

if __name__ == "__main__":
    cmd()
