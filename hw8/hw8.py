"""
CMSC 14100
Autumn 2024
Homework #8

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

from file_system import Directory, File

# PART 1: General recursion

# Exercise 1
def first_down(directions):
    """
    Given a list of directions, where the directions can be "Up", "Down",
    "Left", or "Right", determine how many turns are made before a turn
    is made in the "Down" direction.

    Args:
        directions (List[str]): list of directions, where the directions
            can be "Up", "Down", "Left", or "Right"

    Returns (int): The number of steps before a step in the "Down" direction.
    """
    ### YOUR CODE HERE ###


# Exercise 2
def path_ends(start, directions):
    """
    Given a starting at a location and a list of directions, determine the
    final location in the grid after following the directions.

    Args:
        start (Tuple[int, int]): starting location
        directions (List[str]): list of directions, where the directions
            can be "Up", "Down", "Left", or "Right"

    Returns (Tuple[int, int]): The final location in the grid.
    """
    ### YOUR CODE HERE ###


# Exercise 3
def is_reachable(start, loc, directions):
    """
    Given a starting location and second location in a grid, as well as a list
    of directions, determine if it is possible to get from the starting
    location to the second location by following the directions.

    Args:
        start (Tuple[int, int]): starting location
        loc (Tuple[int, int]): second location
        directions (List[str]): list of directions, where the directions
            can be "Up", "Down", "Left", or "Right"

    Returns (bool): True if the second location can be reached from the starting
        location by following the directions, False otherwise.
        Note that not all of the directions need to be used.
    """
    ### YOUR CODE HERE ###


# Exercise 4
def same_location(start, directions):
    """
    Given a starting location and a list of directions, determine whether or
    not the path following the direction crosses the same location more
    than once.

    Args:
        start (Tuple[int, int]): starting location
        directions (List[str]): list of directions, where the directions
            can be "Up", "Down", "Left", or "Right"

    Returns (bool): True if the path crosses the same location,
        False otherwise.
    """
    ### YOUR CODE HERE ###


# PART 2: Tree recursion (file systems)

# Exericse 5
def num_python_files(file_system):
    """
    Count the number of Python files that are stored in a file system.
    A Python file is a file that ends in the characters "py".

    Args:
        file_system (Directory or File): an item in your file directory system

    Returns (int): The number of Python files in the file system.
    """
    ### YOUR CODE HERE ###


# Exericse 6
def num_files_of_type(file_system):
    """
    Create a dictionary that maps a file type to the number of files
    of that type stored in your file_system directory. The type of a file is
    the characters after the final dot (".") in the filename.
    E.g., the type of "hw1.py" is a "py" file and "midterm.notes.c" is a
    "c" file.

    Args:
        file_system (Directory or File): an item in your file directory system.

    Returns (Dict[str, int]): A dictionary that maps a type of file to the
        number of occurrences of that type.
    """
    ### YOUR CODE HERE ###


# Exercise 7
def remove_empty_directories(file_system):
    """
    Remove the empty directories from your file directory system.

    Args:
        file_system (Directory or File): an item in your file directory system

    Returns (None): Nothing, modifies directory system in-place.
    """
    ### YOUR CODE HERE ###



# Exercise 8
def get_text(file_system, path):
    """
    Find the contents of the file with the given path, if the file exists.

    Args:
        file_system (Directory or File): an item in your file directory system
        path (str): the path to a file where each step is separated by a
            "/" character

    Returns (str): The text stored in the file given by the path, or
        the empty str if the file does not exist.
    """
    ### YOUR CODE HERE ###
