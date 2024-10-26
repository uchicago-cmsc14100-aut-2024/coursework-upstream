"""
CMSC 14100
Autumn 2024

Functions for reading images from PPM P3 format.
"""

import os
import sys

from hw5 import Color

def load_image(filename, return_as_pixels=False):
    """
    Load a file that is formatted using PPM P3 format.

    Args:
        filename (str): the name of the file containing the image

    Returns (List[List[Color]]): the image. 
    """
    try:
        f = os.path.exists(filename)
    except OSError:
        print(f"Cannot open {filename}")
        sys.exit(1)

    f = open(filename, "r")

    ppm_type = f.readline().strip()
    if ppm_type != "P3":
        print("Wrong file type. This function only loads P3 PPMs\n",
              file=sys.stderr)
        sys.exit(1)

    width, height = (int(x) for x in f.readline().strip().split())
    # We have no use for the max color
    _ = int(f.readline())

    rgbs = [int(x) for x in f.read().split()]
    assert len(rgbs) == height*width*3

    img = []
    rgbs_index = 0
    for _ in range(height):
        row = []
        for _ in range(width):
            row.append(Color(*rgbs[rgbs_index:rgbs_index + 3]))
            rgbs_index += 3
        img.append(row)

    f.close()

    return img
