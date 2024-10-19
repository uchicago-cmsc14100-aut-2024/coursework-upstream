CMSC 14100
Autumn 2024
Homework #4

hw4.py: You will do your work in this Python file

Do NOT modify these files:

    test_hw4.py: Test code for HW #4.  Do NOT modify this file
    test_helpers.py: Helper functions for the test code.  Do NOT modify this file.
    tests/: a directory with files used by the test code.  Do NOT modify
    the files in this directory.

    grader.py: script for computing an S/N/U completeness score.
    pytest.ini: grader configuration file.

    .pylintrc: pylint configuration file

    ellsworth-blanton.txt: a text file with one color per line, where the colors were chosen from a photograph of
      Ellsworth Kelly's Spectrum Colors Arranged by Chance IX (1953) from the Blanton Museum website
      (https://blantonmuseum.org/exhibition/form-into-spirit-ellsworth-kellys-austin).  This file was included to
      allow students to run their code from the command line.

    README.md: this file

To run hw4.py to produce a ppm image:

    $ python3 hw4.py --help
    Usage: hw4.py [OPTIONS]

      Generate an image and print it out in PPM format.

    Options:
      -c, --colors-filename TEXT      The name of the file with colors.
                                      [required]
      -f, --output-filename TEXT      The name of the file to use for output.
                                      [required]
      -s, --stripes                   Generate a stripes image
      -a, --alternating-stripes       Generate an alternating stripes image
      -g, --grid                      Generate a grid image
      -r, --randomize                 Randomize the order of the colors
      -n, --number-of-color-sections INTEGER
                                      The number of color sections to include in
                                      the output. Default: 1
      --help                          Show this message and exit.

For example, running:

   $ python3 hw4.py -c ellsworth-blanton.txt -n 10 -g -r -f eb-random-10.ppm

will produce a grid image with 10 color sections with colors randomly
chosen from the colors listed in the file ellsworth-blanton.txt.

   
