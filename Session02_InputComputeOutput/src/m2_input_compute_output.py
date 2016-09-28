"""
This module lets you practice the INPUT-COMPUTE-OUTPUT pattern,
including:
  -- INPUT numbers (using input and float and int)
  -- COMPUTE (using variables and arithmetic operators)
  -- OUTPUT (using print)
  -- CALLING a function from main.

See the     m0e_input_compute_output    module for an example,
or the  m1e_input_compute_output_in_functions   module
for a more elaborate (and commented) example.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Jack Richard.  December 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import math


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # TODO: 2. Implement and test this function.
    cylinder_volume()
    rectangle_area()
    raise_to_power()


def rectangle_area():
    """
    Prompts for and inputs the width and height of a rectangle
    (as floating point numbers) and prints the area of the rectangle.

    Here is a sample run (where the inputs are to the right of the
    colon signs):
        Enter the width of the rectangle: 4.5
        Enter the height of the rectangle: 8
        36.0
    """
    # TODO: 3. Implement and test this function.
    input_string = input('Enter the width of the rectangle:')
    width = float(input_string)
    input_string = input('Enter the height of the rectangle:')
    height = float(input_string)
    print(width * height)


def raise_to_power():
    """
    Prompts for and inputs:
      -- a floating point number X
      -- an integer N
    Prints X raised to the Nth power.

    Here is a sample run (where the inputs are to the right of the
    colon signs):
        Enter a number: 3.8
        Enter an integer: 6
        3010.936383999999
    """
    # TODO: 4. Implement and test this function.
    # Hints:
    #  -- Use  float  to convert to a floating point number
    #     but  int    to convert to an integer
    #  -- Use   **  for raising to a power
    x = float(input('Enter a number:'))
    n = int(input('Enter an integer:'))
    print(x ** n)


def cylinder_volume():
    """
    Prompts for and inputs the diameter and height of a cylinder
    (as floating point numbers) and prints the volume of the cylinder.

    Here is a sample run (where the inputs are to the right of the
    colon signs):
        Enter the diameter of the cylinder: 8.55
        Enter the height of the cylinder: 4.2
        241.14119080700027
    """
    # TODO: 5. Implement and test this function.
    # Hint: You need PI in this formula.  For PI, type:
    #    math,
    #    then a dot,
    #    then pause, then look for what to select/type.
    radius = float(input('Enter the Diameter of the cylinder:')) / 2
    height = float(input('Enter the height of the cylinder:')) / 2
    print(math.pi * (radius ** 2) * height)
#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
