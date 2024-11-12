"""
CMSC 14100
Winter 2023

Functions for reading and writing images in PPM P3 format.
"""

import os
import sys

from hw7 import Color, Image

def load_image(filename, return_as_pixels=False):
    """
    Load a file that is formatted using PPM P3 format.

    Args:
        filename (str): the name of the file containing the image

    Returns (Image): the image
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
    # The return_as_pixels option is used in the test code.
    if return_as_pixels:
        return img
    return Image(img)


def write_image(filename, img):
    """
    Write an image to a file in P3 PPM format

    Args:
        filename (string): the name of the file to write
        img (Image | List[List[Color]]): the image to write to the file either
        as an Image or as a list of list of Colors.
    """
    try:
        f = open(filename, "w")
    except OSError:
        print(f"Cannot open {filename}")
        sys.exit(1)

    if isinstance(img, Image):
        pixels = img.get_pixels()
    else:
        pixels = img
        
    print("P3", file=f)
    # output width height
    print(f"{len(pixels[0])} {len(pixels)}", file=f)
    print("255", file=f)
    for row in pixels:
        flatten = []
        for color in row:
            flatten.extend([str(c) for c in color.get_as_vector().get_elements()])
        print(" ".join(flatten), file=f)
    f.close()


    
