"""
PRACTICE Test 1, problem 2.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Jack Richard.  December 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import math
def main():
    """ Calls the   TEST   functions in this module. """
    test_problem2a()
    test_problem2b()
    test_problem2c()


def test_problem2a():
    """ Tests the   problem2a   function. """
    # TODO: 2a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 3 tests, i.e., 3 calls to the function to test.
    print("expected: -1.601 1.135 -1.380")
    print(problem2a(3, 5), problem2a(1, -2), problem2a(3, 7))

def problem2a(m, n):
    """
    Returns the sum of the sines of the integers from m squared
    to n squared, inclusive, where m and n are the given arguments.

    For example, if m is 3 and n is 5, this function returns:
       sine(9) + sine(10) + sine(11) +  ...  + sine(24) + sine(25)

    Preconditions: m and n are integers and the absolute value of m
                   is less than the absolute value of n.

    Examples that you can (AND SHOULD) use for testing include:
      When m is 3 and n is 5, the correct answer is about -1.601.
      When m is 1 and n is -2, the correct answer is about 1.135.
    """
    # TODO: 2b. Implement and test this function.
    sum = 0
    for k in range(m ** 2, n ** 2 + 1):
        sum = sum + math.sin(k)
    return sum

# ----------------------------------------------------------------------
# Students: Use the following  is_prime  function
#           in your solution to problem2c that appears below.
#           This   sum_of_digits   function is ALREADY DONE - there is
#           no need to modify or add to it
# ---------------------------------------------------------------------
def is_prime(n):
    """
    Returns True if the given integer is prime, else returns False.

    Note: The algorithm used here is simple and clear but slow.

    Precondition:  The given argument is an integer that is at least 2.
    """
    for k in range(2, (n // 2) + 1):
        if n % k == 0:
            return False

    return True


def test_problem2b():
    """ Tests the   problem2b   function. """
    # TODO: 3a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 3 tests, i.e., 3 calls to the function to test.
    print("expected: 5 1 44")
    print(problem2b(3, 5), problem2b(2, 1), problem2b(5, 40))

def problem2b(m, f):
    """
    Returns the number of integers from m to (f * m), inclusive,
    that are prime.

    For example, if m is 3 and f is 5, this function returns 5,
       since 3, 5, 7, 11, and 13 are the integers between 3 and 15,
       inclusive, that are prime.

    Preconditions: m and f are positive integers and m is at least 2.

    Examples that you can (AND SHOULD) use for testing include:
      When m is 3 and f is 5, the correct answer is 5.
      When m is 2 and f is 1, the correct answer is 1
        (since 2 is the only prime between 2 and 2, inclusive).
      When m is 5 and f is 40, the correct answer is 44.
    """
    # TODO: 3b. Implement and test this function.
    # IMPLEMENTATION REQUIREMENT:
    #    Use (call) the   is_prime   function above appropriately.
    count = 0
    for k in range(m, f * m + 1):
        if is_prime(k):
            count = count + 1
    return count

# ----------------------------------------------------------------------
# Students: Use the following  sum_of_digits  function,
#           along with the   is_prime   function that appears above,
#           in your solution to problem2c that appears below.
#           This   sum_of_digits   function is ALREADY DONE - there is
#           no need to modify or add to it.
# ----------------------------------------------------------------------
def sum_of_digits(number):
    """
    Returns the sum of the digits in the given integer.
    For example, if the number is 83135, this function returns 20.

    Precondition: the given argument is an integer.
    """
    # Students: While you are welcome to try to understand this
    #           function definition, all you have to do is trust
    #           that the green doc-string is correct (it is!).
    if number < 0:
        number = -number

    digit_sum = 0
    while True:
        if number == 0:
            break
        digit = number % 10  # Get the digit
        digit_sum = digit_sum + digit  # Accumulate it into the sum
        number = number // 10  # Get ready for the next digit

    return digit_sum


def test_problem2c():
    """ Tests the   problem2c   function. """
    # TODO: 4a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 3 tests, i.e., 3 calls to the function to test.
    print("expected: 13 16 22")
    print(problem2c(20, 50), problem2c(30, 60), problem2c(0, 40))

def problem2c(m, n):
    """
    Let's say that an integer X is PRIME-OR-SUM_OF_DIGITS-IS-ODD
    ("POSODIO" for short) if and only if:
      1. X is prime, OR
      2. the sum of the digits of X is odd,
    BUT NOT BOTH.

    For example, the following are POSODIOs:
       31 (IS prime, and sum of digits is NOT odd)
       32 (NOT prime and sum of digits IS odd)
    while the following are NOT POSODIOs:
       33 (neither prime nor sum of digits is odd)
       41 (prime AND sum of digits is odd)

    This function returns the number of integers from m to n,
    inclusive, that are POSODIOs.

    To assist your testing, here are all the POSODIOs between 20 and 50,
    inclusive:   21  25  27  30  31  32  34  36  37  38  45  49  50

    Preconditions: m and n are positive integers, m is at least 2
                   and m <= n.
    """
    # TODO: 4b. Implement and test this function.
    # IMPLEMENTATION REQUIREMENT:
    #    Use (call) the  is_prime  AND the  sum_of_digits  functions,
    #    both defined above.
    count = 0
    for k in range(m, n + 1):
        if (is_prime(k)) ^ (sum_of_digits(k) % 2 == 1):
            count = count + 1
    return count

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
