"""
CMSC 14100
Autumn 2024
Homework #3

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

# Exercise 1
def is_grayscale(r, g, b):
    """
    Determine whether or not an RGB color is a grayscale color.

    Args:
        r (int): red component
        g (int): green component
        b (int): blue component

    Returns (bool): True if the color is grey, False otherwise.
    """
    assert isinstance(r, int)
    assert isinstance(g, int)
    assert isinstance(b, int)
    assert 0 <= r < 256
    assert 0 <= g < 256
    assert 0 <= b < 256

    ### YOUR CODE HERE


# Exercise 2
def is_black_or_white(rgb):
    """ docstring here """
    ### YOUR CODE HERE


# Exercise 3
def count_not_black_or_white(lst):
    """ docstring here """
    ### YOUR CODE HERE


# Constants used in Exercises 4-6
# Do not remove these definitions.
LOWER = -1
UPPER = 1
NEITHER = 0

# Exercise 4
def which_comes_first_break(lst, lower, upper):
    """ docstring here """
    ### YOUR CODE HERE


# Exercise 5
def which_comes_first_return(lst, lower, upper):
    """ docstring here """
    ### YOUR CODE HERE


# Exercise 6
def which_comes_last(lst, lower, upper):
    """ docstring here """
    ### YOUR CODE HERE


# Exercise 7
def are_all_same(lst):
    """ docstring here """
    ### YOUR CODE HERE


# Exercise 8
def compute_final_score(lst, lower, upper, bonus):
    """ docstring here """
    ### YOUR CODE HERE


# Exercise 9
def get_first_bw_idx(lst):
    """ docstring here """
    ### YOUR CODE HERE
