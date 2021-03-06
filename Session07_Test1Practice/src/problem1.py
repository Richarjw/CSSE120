"""
PRACTICE Test 1, problem 1.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Jack Richard.  December 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.
import math

def main():
    """ Calls the   TEST   functions in this module. """
    test_problem1()


def test_problem1():
    """ Tests the   problem1   function. """
    problem1()


def problem1():
    """
    Prompts the user for and inputs:
      -- A positive floating point number
      -- A positive integer
      -- A string
    in that order (via three separate inputs).
    Then prints, in this order, all on separate lines:
      -- The square root of the floating point number,
         repeated the input integer number of times
      -- The string, repeated the input integer number of times.
    No input validation is required.  Nothing else should be printed.

    Here is a sample run, where the user input is to the right
    of the colons:
         Enter a positive floating point number: 1.44
         Enter a positive integer: 4
         Enter a string: Peace & Love.
         1.2
         1.2
         1.2
         1.2
         Peace & Love.
         Peace & Love.
         Peace & Love.
         Peace & Love.
    """
    # TODO: 2. Implement and test this function.
    #     The testing code is already written for you (above).
    input1 = float(input("Enter a positive floating point number:"))
    input2 = int(input("Enter a positive integer:"))
    input3 = input("Enter a string:")
    for k in range(0, input2):
        print(math.sqrt(input1))
    for k in range(0, input2):
        print(input3)
# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
