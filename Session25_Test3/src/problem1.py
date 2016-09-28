"""
Test 3, problem 1.

Authors: David Mutchler, Mark Hays, Michael Wollowski,
         Chandan Rupakheti, Matt Boutell, Dave Fisher,
         Claude Anderson, and Jack Richard.  November 2014.
"""  # TODO: PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    test_shape()


def test_shape():
    """ Tests the    shape    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   SHAPE   function:')
    print('--------------------------------------------------')

    print()
    print('Test 1 of shape: r=7')
    shape(7)

    print()
    print('Test 2 of shape: r=4')
    shape(4)

    print()
    print('Test 3 of shape: r=2')
    shape(2)


def shape(r):
    """
    Prints a Z shape with r rows that looks like this example where r=7:
    1234567
         6
        5
       4
      3
     2
    1234567

    Another example, where r=4:
    1234
      3
     2
    1234

    One more example, where r=2:
    12
    12

    Preconditions:  r is an integer that is at least 2.
    For purposes of "lining up", assume r is a single digit.
    """
    # ------------------------------------------------------------------
    # TODO: Implement and test this function.
    #          Some tests are already written for you (above).
    #
    # IMPLEMENTATION RESTRICTION:
    #   You may NOT use string multiplication in this problem.
    # ------------------------------------------------------------------
    s = ''
    for k in range(r):
        if k == 0 or k == r - 1:
            for j in range(1, r + 1):
                s = s + str(j)
        else:
            for j in range(0, r - (k + 1)):
                s = s + ' '
            s = s + str(r - k)
        print(s)
        s = ''

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
