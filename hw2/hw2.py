"""
CMSC 14100
Autumn 2024
Homework #2

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

#############################################################################
#                                                                           #
# Important note: some of the tasks in this assignment have task-specific   #
# requirements/restrictions concerning the language constructs that you are #
# allowed to use in your solution. See the assignment writeup for details.  #
#                                                                           #
#############################################################################


def add_one_and_multiply(a, x):
    """
    Add 1 to a, and multiply by x.

    Args:
        a (int): an integer value
        x (int): an integer value

    Returns (int): The result of adding 1 to a and then multiplying by x.
    """
    ### EXERCISE 1 -- YOUR CODE GOES HERE
    ### Replace "None" with the correct expression
    return None


def have_same_value(x):
    """
    Determine whether or not the digits in an integer with two positive digits
    have the same value.

    Note: You can assume the input integer has exactly two positive digits.

    Args:
        x (int): an integer with two positive digits

    Returns (boolean): True if the two digits in x have the same value,
        False otherwise.
    """
    ### EXERCISE 2 -- YOUR CODE GOES HERE
    ### Replace "None" with the correct expression
    result = None

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return result


def swap_digits(x):
    """
    Swap the digits of an integer with two positive digits.

    Note: You can assume the input integer has exactly two positive digits.

    Args:
        x (int): an integer with two positive digits

    Returns (int): The input integer x with its digits swapped.
    """
    ### EXERCISE 3 -- YOUR CODE GOES HERE
    ### Replace "None" with the correct expression
    result = None

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return result


def swap_last_two_digits(x):
    """
    Swap the last two digits in an integer with at least two positive digits.

    Note: You can assume the input integer has at least two positive digits.

    Args:
        x (int): an integer with at least two positive digits

    Returns (int): The input integer x with its last two digits swapped.
    """
    ### EXERCISE 4 -- YOUR CODE GOES HERE
    ### Replace "None" with the correct expression
    result = None

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return result


def is_valid_color(r, g, b):
    """
    Determine whether or not an RGB color is valid. A color is valid if
    each R, G, B channel is an integer value between 0 and 255 (inclusive).

    Args:
        r (value): red channel
        g (value): green channel
        b (value): blue channel

    Returns (boolean): True if the color is valid, False otherwise.
    """
    ### EXERCISE 5 -- YOUR CODE GOES HERE
    ### Replace "None" with the correct expression
    result = None

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return result


def is_grayscale(r, g, b):
    """
    Determine whether or not an RGB color is gray.
    An RGB color is gray if all R, G, B values are equal.

    Args:
        r (int): red channel
        g (int): green channel
        b (int): blue channel

    Returns (boolean): True if the color is gray, False otherwise.
    """
    assert is_valid_color(r, g, b)

    ### EXERCISE 6 -- YOUR CODE GOES HERE
    ### Replace "None" with the correct expression
    result = None

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return result


def is_not_black_or_white(r, g, b):
    """
    Determine whether or not an RGB color is not black or white.
    An RGB color is black if all R, G, B values are zero. An RGB color is
    white if all R, G, B values are 255.

    Args:
        r (int): red channel
        g (int): green channel
        b (int): blue channel

    Returns (boolean): True if the color is not black or white,
        False otherwise.
    """
    assert is_valid_color(r, g, b)

    ### EXERCISE 7 -- YOUR CODE GOES HERE
    ### Replace "None" with the correct expression
    result = None

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return result


def compute_similarity_v1(r1, g1, b1, r2, g2, b2):
    """
    Compute the similarity between two colors using the Euclidean distance
    formula (see homework writeup for the formula).

    Args:
        r1 (int): red channel of color 1
        g1 (int): green channel of color 1
        b1 (int): blue channel of color 1
        r2 (int): red channel of color 2
        g2 (int): green channel of color 2
        b2 (int): blue channel of color 2

    Returns (float): The similarity between color 1 and color 2.
    """
    assert is_valid_color(r1, g1, b1)
    assert is_valid_color(r2, g2, b2)

    ### EXERCISE 8 -- YOUR CODE GOES HERE
    ### Replace "None" with the correct expression
    result = None

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return result


def compute_similarity_v2(r1, g1, b1, r2, g2, b2):
    """
    Compute the similarity between two colors using the weighted average
    distance formula (see homework writeup for the formula).

    Args:
        r1 (int): red channel of color 1
        g1 (int): green channel of color 1
        b1 (int): blue channel of color 1
        r2 (int): red channel of color 2
        g2 (int): green channel of color 2
        b2 (int): blue channel of color 2

    Returns (float): The similarity between color 1 and color 2.
    """
    assert is_valid_color(r1, g1, b1)
    assert is_valid_color(r2, g2, b2)

    ### EXERCISE 9 -- YOUR CODE GOES HERE
    ### Replace "None" with the correct expression
    result = None

    ### DO NOT MODIFY THE FOLLOWING LINE!
    return result
