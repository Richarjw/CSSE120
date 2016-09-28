"""
Test 1, problem 2.

Authors: David Mutchler, Michael Wollowski, Mark Hays, their colleagues,
         and Jack Richard. September 2014.
"""  # TODO: PUT YOUR NAME IN THE ABOVE LINE.

import math


def main():
    """ Calls the   TEST   functions in this module. """
    test_problem2a()
    test_problem2b()


def test_problem2a():
    """ Tests the   problem2a   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem2a   function:')
    print('--------------------------------------------------')
    # TODO: Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #
    # IMPORTANT: Include  *** at least 4 tests ***.
    test1 = problem2a(3, 6)
    print('Expected: 870')
    print(test1)
    test2 = problem2a(12, 14)
    print('Expected: 93884313600')
    print(test2)
    test3 = problem2a(1, 3)
    print('Expected: 9')
    print(test3)
    test4 = problem2a(4, 8)
    print('Expected: 46224')
    print(test4)

def problem2a(m, n):
    """
    Returns the sum:
       m! + (m+1)! + (m+2)! + ... + n!
    where   m!   is "m factorial" and can be computed using a function
    from Python's   math   module.

    If you don't know what "m factorial" means, PLEASE ASK US!

    For example, when m is 3 and n is 6,
    the correct returned value is:
       3! + 4! + 5! + 6!
          which is   6 + 24 + 120 + 720
          which is 870.

    As another example, when m is 12 and n is 14,
    the correct returned value is:
       12! + 13! + 14!
          which is  479001600 + 6227020800 + 87178291200
          which is  93884313600.

    Preconditions: m and n are nonnegative integers and m <= n.
    """
    # TODO: Implement and test this function.
    sum = 0
    for k in range(m, n + 1):
        sum = sum + math.factorial(k)
    return sum

# ----------------------------------------------------------------------
# Students: Use this   largest_factor   function in your solution to
#      problem2b.  It is ALREADY DONE - no need to modify or add to it
#      or even understand HOW it works -- just understand and believe
#      the GREEN specification.
# ----------------------------------------------------------------------
def largest_factor(n):
    """
    Returns the largest non-trivial factor of the given argument,
    where:
      -- the largest non-trivial factor of an integer X is,
         by definition, the largest integer other than X itself
         that divides evenly into X.
    For example:
      -- the largest non-trivial factor of 12 is 6
      -- the largest non-trivial factor of 13 is 1
      -- the largest non-trivial factor of 15 is 5
      -- the largest non-trivial factor of 75 is 25
      -- the largest non-trivial factor of 120 is 60

    Note: The algorithm used here is simple and clear but slow.

    Precondition:  The given argument is a positive integer.
    """
    for k in range(2, (n // 2) + 1):
        if n % k == 0:
            return n // k

    return 1


def test_problem2b():
    """ Tests the   problem2b   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem2b   function:')
    print('--------------------------------------------------')
    # TODO: Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #
    # IMPORTANT: Include  *** at least 3 tests ***.
    print('Expected: 5')
    print(problem2b(2))
    print('Expected: 253')
    print(problem2b(7))
    print('Expected: 743')
    print(problem2b(10))


def problem2b(m):
    """
    *** IMPORTANT: ***
        SEE ABOVE for the definition of "LARGEST NON-TRIVIAL FACTOR"
        *** and *** the function that COMPUTES it!

    This function returns the number of integers
    from m to m cubed, inclusive,
    whose largest non-trivial factor is odd.

    For example, if m is 2, then this function should return 5
    because m cubed (i.e., 2 cubed) is 8 and:
      -- the largest non-trivial factor of 2 is 1 (which is ODD)
      -- the largest non-trivial factor of 3 is 1 (which is ODD)
      -- the largest non-trivial factor of 4 is 2 (which is EVEN)
      -- the largest non-trivial factor of 5 is 1 (which is ODD)
      -- the largest non-trivial factor of 6 is 3 (which is ODD)
      -- the largest non-trivial factor of 7 is 1 (which is ODD)
      -- the largest non-trivial factor of 8 is 4 (which is EVEN)
    and there are 5 ODDs in the above list.

    As other examples that you can (and should) use for testing:
      -- When m is 7, the correct returned value is 253.
      -- When m is 10, the correct returned value is 743.

    Precondition: m is a positive integer.
    """
    # TODO: Implement and test this function.
    #
    # IMPORTANT:
    #    Use (call) the   largest_factor   function (defined above)
    #    appropriately.
    count = 0
    for k in range(m, m ** 3 + 1):
        if largest_factor(k) % 2 == 1:
            count = count + 1
    return count

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
