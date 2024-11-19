"""
CMSC 14100
Autumn 2024

Test code for Homework #8
"""

import json
import os
import sys
import traceback
import pytest
import copy
import helpers

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position
import file_system
import hw8

MODULE = "hw8"

##### PART 1 TESTS #####

DIRECTIONS0 = []
DIRECTIONS1 = ["Down"]
DIRECTIONS2 = ["Right", "Down"]
DIRECTIONS3 = ["Right", "Right", "Right", "Down", "Down"]
# One direction:
DIRECTIONS4 = ["Up", "Up", "Up", "Up"]
DIRECTIONS5 = ["Down", "Down", "Down", "Down"]
DIRECTIONS6 = ["Left", "Left", "Left", "Left"]
DIRECTIONS7 = ["Right", "Right", "Right", "Right"]
# Stationary:
DIRECTIONS8 = ["Left", "Right", "Down", "Up"]
DIRECTIONS9 = ["Up", "Right", "Left", "Down"]
DIRECTIONS10 = ["Right", "Left"]
DIRECTIONS11 = ["Up", "Down", "Up", "Down"]
# Long path:
DIRECTIONS12 = ["Down", "Right", "Up", "Up", "Left", "Down", "Left", "Down"]


@pytest.mark.timeout(60)
@pytest.mark.parametrize("directions, expected",
                         [(DIRECTIONS1, 0),
                          (DIRECTIONS2, 1),
                          (DIRECTIONS3, 3),
                          (DIRECTIONS5, 0),
                          (DIRECTIONS8, 2),
                          (DIRECTIONS11, 1)
                          ])
def test_first_down(directions, expected):
    """  
    Test code for Exercise 1: first_down
    """
    steps = [
        f"actual = hw8.first_down({directions})"
        ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    directions_copy = copy.deepcopy(directions)

    try:
        actual = hw8.first_down(directions)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

    err_msg = helpers.check_list_unmodified("directions", directions_copy, directions)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.timeout(60)
@pytest.mark.parametrize("start, directions, expected",
                         [((2, 2), DIRECTIONS0, (2, 2)),
                          ((2, 2), DIRECTIONS1, (3, 2)),
                          ((2, 2), DIRECTIONS3, (4, 5)),
                          ((2, 2), DIRECTIONS1, (3, 2)),
                          ((2, 2), DIRECTIONS2, (3, 3)),
                          ((4, 1), DIRECTIONS1, (5, 1)),
                          ((4, 1), DIRECTIONS2, (5, 2)),
                          ((2, 1), DIRECTIONS3, (4, 4)),
                          ((8, 1), DIRECTIONS4, (4, 1)),
                          ((4, 6), DIRECTIONS6, (4, 2)),
                          ((4, 1), DIRECTIONS8, (4, 1)),
                          ((4, 1), DIRECTIONS11, (4, 1)),
                          ((2, 2), DIRECTIONS12, (3, 1))
                          ])
def test_path_ends(start, directions, expected):
    """
    Test code for Exercise 2: path_ends
    """
    steps = [
        f"actual = hw8.path_ends({start}, {directions})"
        ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    directions_copy = copy.deepcopy(directions)

    try:
        actual = hw8.path_ends(start, directions)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

    err_msg = helpers.check_list_unmodified("directions", directions_copy, directions)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.timeout(60)
@pytest.mark.parametrize("start, end, directions, expected",
                         [((2, 2), (2, 2), DIRECTIONS0, True),
                          ((2, 2), (2, 3), DIRECTIONS3, True),
                          ((2, 2), (2, 5), DIRECTIONS3, True),
                          ((2, 2), (2, 6), DIRECTIONS3, False),
                          ((2, 2), (3, 5), DIRECTIONS3, True),
                          ((2, 2), (4, 5), DIRECTIONS3, True),
                          ((2, 2), (5, 5), DIRECTIONS3, False),
                          ((2, 2), (5, 6), DIRECTIONS3, False),
                          ((2, 2), (2, 3), DIRECTIONS4, False),
                          ((2, 2), (3, 2), DIRECTIONS4, False),
                          ((2, 2), (2, 1), DIRECTIONS4, False),
                          ((2, 2), (1, 2), DIRECTIONS4, True),
                          ((2, 2), (1, 2), DIRECTIONS4, True),
                          ((2, 2), (2, 3), DIRECTIONS7, True),
                          ((2, 2), (2, 4), DIRECTIONS7, True),
                          ((2, 2), (2, 6), DIRECTIONS7, True),
                          ((2, 2), (2, 7), DIRECTIONS7, False),
                          ((2, 2), (1, 3), DIRECTIONS12, True),
                          ((2, 2), (1, 2), DIRECTIONS12, True)
                          ])
def test_is_reachable(start, end, directions, expected):
    """
    Test code for Exercise 3: is_reachable
    """
    steps = [
        f"actual = hw8.is_reachable({start}, {end}, {directions})"
        ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    directions_copy = copy.deepcopy(directions)

    try:
        actual = hw8.is_reachable(start, end, directions)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

    err_msg = helpers.check_list_unmodified("directions", directions_copy, directions)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.timeout(60)
@pytest.mark.parametrize("start, directions, expected",
                         [((2, 2), DIRECTIONS0, False),
                          ((2, 2), DIRECTIONS1, False),
                          ((2, 2), DIRECTIONS2, False),
                          ((2, 2), DIRECTIONS3, False),
                          ((2, 2), DIRECTIONS4, False),
                          ((2, 2), DIRECTIONS6, False),
                          ((2, 2), DIRECTIONS9, True),
                          ((2, 2), DIRECTIONS10, True),
                          ((2, 2), DIRECTIONS11, True),
                          ((2, 2), DIRECTIONS12, True)
                          ])
def test_same_location(start, directions, expected):
    """
    Test code for Exercise 4: same_location
    """
    steps = [
        f"actual = hw8.same_location({start}, {directions})"
        ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    directions_copy = copy.deepcopy(directions)

    try:
        actual = hw8.same_location(start, directions)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)

    err_msg = helpers.check_list_unmodified("directions", directions_copy, directions)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


##### PART 2 TESTS #####

SYSTEM1 = "file_systems/file_system1.json"
SYSTEM2 = "file_systems/file_system2.json"
SYSTEM3 = "file_systems/file_system3.json"
SYSTEM4 = "file_systems/file_system4.json"
SYSTEM5 = "file_systems/file_system5.json"
SYSTEM6 = "file_systems/file_system6.json"
SYSTEM7 = "file_systems/file_system7.json"
SYSTEM8 = "file_systems/file_system8.json"
SYSTEM9 = "file_systems/file_system9.json"
SYSTEM10 = "file_systems/file_system10.json"


@pytest.mark.timeout(60)
@pytest.mark.parametrize("input_filename, expected", 
                         [(SYSTEM1, 2),
                          (SYSTEM2, 1),
                          (SYSTEM4, 3),
                          (SYSTEM5, 0),
                          (SYSTEM6, 4),
                          (SYSTEM9, 4),
                          (SYSTEM10, 1)
                          ])
def test_num_python_files(input_filename, expected):
    """
    Test code for Exercise 5: num_python_files
    """
    steps = [
        f"import file_system",
        f"coursework = file_system.load_file_system('{input_filename}')",
        f"actual = hw8.num_python_files(coursework)"
        ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    coursework = file_system.load_file_system(input_filename)

    try:
        actual = hw8.num_python_files(coursework)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.timeout(60)
@pytest.mark.parametrize("input_filename, path, expected", 
                         [(SYSTEM1, "cs141/hw1.py", "print(5 + 2)"),
                          (SYSTEM1, "cs141/notes.txt", "Python is fun!"),
                          (SYSTEM1, "cs253/page_rank.py", "simulate_surfer()"),
                          (SYSTEM1, "cs141/program.py", ""),
                          (SYSTEM6, "cs253/Project/ML.py", "def learn_model():"),
                          (SYSTEM6, "cs253/Project/MLL.py", ""),
                          (SYSTEM10, "cs141/midterm/Practice.docx", "types, logic operators,"),
                          (SYSTEM10, "cs141/midterm", "")
                          ])
def test_get_text(input_filename, path, expected):
    """
    Test code for Exercise 6: get_text
    """
    steps = [
        f"import file_system",
        f"coursework = file_system.load_file_system('{input_filename}')",
        f"actual = hw8.get_text(coursework, '{path}')"
        ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    coursework = file_system.load_file_system(input_filename)
    
    try:
        actual = hw8.get_text(coursework, path)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.timeout(60)
@pytest.mark.parametrize("input_filename, expected_filename", 
                         [(SYSTEM2, SYSTEM3),
                          (SYSTEM7, SYSTEM8), 
                          ("file_systems/file_system11.json", "file_systems/file_system12.json"), 
                          ("file_systems/file_system13.json", "file_systems/file_system14.json"),
                          ("file_systems/file_system15.json", "file_systems/file_system16.json")
                          ])
def test_remove_empty_directories(input_filename, expected_filename):
    """
    Test code for Exercise 7: remove_empty_directories
    """
    steps = [
        f"import file_system",
        f"coursework = file_system.load_file_system('{input_filename}')",
        f"hw8.remove_empty_directories(coursework)"
        ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    actual = file_system.load_file_system(input_filename)
    expected = file_system.load_file_system(expected_filename)
    
    try:
        hw8.remove_empty_directories(actual)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    if not file_system.file_systems_equal(actual, expected):
        err_msg = "\nThe actual and expected values do not match"
        pytest.fail(err_msg + recreate_msg)


@pytest.mark.timeout(60)
@pytest.mark.parametrize("input_filename, expected", 
                         [(SYSTEM1, {"py": 2, "txt": 1}),
                          (SYSTEM2, {"py": 1, "txt": 1}),
                          (SYSTEM4, {"py": 3, "txt": 1, "pdf": 1}),
                          (SYSTEM6, {"py": 4, "pdf": 2}),
                          (SYSTEM7, {"py": 1}),
                          (SYSTEM9, {"py": 4, "txt": 2, "pdf": 1}),
                          (SYSTEM10, {"py": 1, "txt": 1, "ppm": 1, "docx": 1, "json": 1, "c": 1, "pdf": 1})
                          ])
def test_num_files_of_type(input_filename, expected):
    """
    Test code for Exercise 8: num_files_of_type
    """
    steps = [
        f"import file_system",
        f"coursework = file_system.load_file_system('{input_filename}')",
        f"actual = hw8.num_files_of_type(coursework)"
        ]
    recreate_msg = helpers.gen_recreate_commands(MODULE, steps)

    coursework = file_system.load_file_system(input_filename)

    try:
        actual = hw8.num_files_of_type(coursework)
    except Exception as e:
        helpers.fail_and_augment_recreate_unexpected_exception(recreate_msg, e)

    err_msg = helpers.check_result(actual, expected)
    if err_msg is not None:
        pytest.fail(err_msg + recreate_msg)
