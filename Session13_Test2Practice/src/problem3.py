"""
PRACTICE Test 2, problem 3.

Authors: David Mutchler, Chandan Rupakheti, Matt Boutell, Dave Fisher,
         Claude Anderson, and Jack Richard.  September 2013.
"""  # TODO: PUT YOUR NAME IN THE ABOVE LINE.

import simple_testing as st
import math


def main():
    """ Calls the   TEST   functions in this module. """
    test_problem3()


# ----------------------------------------------------------------------
# Students: Some of the testing code below uses SimpleTestCase objects,
#           from the imported   simple_testing (st)   module.
# ----------------------------------------------------------------------

def test_problem3():
    """ Tests the   problem23  function. """
    # Some tests.
    tests = [st.SimpleTestCase(problem3,
                               [-5, 3, 0.25],
                               [-5, 0, 1]),
             st.SimpleTestCase(problem3,
                               [-5, 4, 0.25],
                               [-5, 0, 1, 2]),
             st.SimpleTestCase(problem3,
                               [-5, 5, 0.25],
                               [-5, 0, 1, 2, 6]),
             st.SimpleTestCase(problem3,
                               [-5, 6, 0.25],
                               [-5, 0, 1, 2, 6, 7]),
             st.SimpleTestCase(problem3,
                               [-5, 7, 0.25],
                               [-5, 0, 1, 2, 6, 7, 8]),
             st.SimpleTestCase(problem3,
                               [-3, 3, -1.0],
                               [-1, 0, 1]),
             st.SimpleTestCase(problem3,
                               [-3, 4, -1.0],
                               [-1, 0, 1, 2]),
             st.SimpleTestCase(problem3,
                               [-3, 5, -1.0],
                               [-1, 0, 1, 2, 3]),
             st.SimpleTestCase(problem3,
                               [-3, 6, -1.0],
                               [-1, 0, 1, 2, 3, 5]),
             st.SimpleTestCase(problem3,
                               [30, 0, -1000],
                               []),
             st.SimpleTestCase(problem3,
                               [100, 5, 1.414],
                               [139, 183, 516, 560, 849]),
             st.SimpleTestCase(problem3,
                               [0, 1, 1.414213562373],
                               [286602]),
             st.SimpleTestCase(problem3,
                               [-2, 3, -1.0],
                               [-1, 0, 1]),
             st.SimpleTestCase(problem3,
                               [-1, 4, -1.0],
                               [-1, 0, 1, 2])
             ]

    st.SimpleTestCase.run_tests('problem3', tests)

    # ------------------------------------------------------------------
    # TODO: Add at least 2 more tests to the above list of tests.
    #       Try to choose tests that might expose errors in your code!
    # CONSIDER: Ask an assistant to CHECK your tests to confirm
    #           that they are adequate tests!
    # ------------------------------------------------------------------


def problem3(start, n, threshold):
    """
    Returns a list of the first n integers, starting at start, for which
    the sum of their sine and cosine are bigger than the given threshold.

    Here (below) are several examples.  For these examples, the following
    (and more) numbers are relevant:  (All numbers in this example
    are rounded to 2 decimal  places for the sake of brevity.)
        -5:  sin =  0.96,  cos =  0.28,  sum =  1.24
        -4:  sin =  0.76,  cos = -0.65,  sum =  0.10
        -3:  sin = -0.14,  cos = -0.99,  sum = -1.13
        -2:  sin = -0.91,  cos = -0.42,  sum = -1.33
        -1:  sin = -0.84,  cos =  0.54,  sum = -0.30
         0:  sin =  0.00,  cos =  1.00,  sum =  1.00
         1:  sin =  0.84,  cos =  0.54,  sum =  1.38
         2:  sin =  0.91,  cos = -0.42,  sum =  0.49
         3:  sin =  0.14,  cos = -0.99,  sum = -0.85
         4:  sin = -0.76,  cos = -0.65,  sum = -1.41
         5:  sin = -0.96,  cos =  0.28,  sum = -0.68
         6:  sin = -0.28,  cos =  0.96,  sum =  0.68
         7:  sin =  0.66,  cos =  0.75,  sum =  1.41
         8:  sin =  0.99,  cos = -0.15,  sum =  0.84
         9:  sin =  0.41,  cos = -0.91,  sum = -0.50
        10:  sin = -0.54,  cos = -0.84,  sum = -1.38
        11:  sin = -1.00,  cos =  0.00,  sum = -1.00
        12:  sin = -0.54,  cos =  0.84,  sum =  0.31
        13:  sin =  0.42,  cos =  0.91,  sum =  1.33

    So if start is -5 and threshold is 0.25 and:
       -- n is 3, then this function returns [-5, 0, 1]
       -- n is 4, then this function returns [-5, 0, 1, 2]
       -- n is 5, then this function returns [-5, 0, 1, 2, 6]
       -- n is 6, then this function returns [-5, 0, 1, 2, 6, 7]
       -- n is 7, then this function returns [-5, 0, 1, 2, 6, 7, 8]

    while if start is -3 and the threshold is -1.0 and:
       -- n is 3, then this function returns [-1, 0, 1]
       -- n is 4, then this function returns [-1, 0, 1, 2]
       -- n is 5, then this function returns [-1, 0, 1, 2, 3]
       -- n is 6, then this function returns [-1, 0, 1, 2, 3, 5]

    and if n is 0 (regardless of what start is), the function returns []

    Preconditions:
      :type start: int
      :type n: int
      :type threshold: (int, float)
    and n is nonnegative
    and threshold is no more than the square root of 2.
    """
    list = []
    while len(list) < n:
        if math.cos(start) + math.sin(start) > threshold:
            list.append(start)
        start = start + 1
    return list

    # ------------------------------------------------------------------
    # TODO: Implement and test this function.
    #       Some tests are already written for you (above),
    #       but you are required to write ADDITIONAL tests (above).
    # ------------------------------------------------------------------

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
