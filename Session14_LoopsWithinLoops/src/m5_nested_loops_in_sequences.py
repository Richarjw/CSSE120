"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of SEQUENCES OF SUB-SEQUENCES.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Jack Richard.  February 2014.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the other functions to test them. """
    test_sum_numbers()
    test_print_characters()
    test_print_characters_slanted()


def test_sum_numbers():
    """ Tests the    sum_numbers    function. """
    # TODO: 2a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    print()
    print('-------------------------------------')
    print('Testing the   SUM_NUMBERS   function:')
    print('-------------------------------------')
    seq = [(3, 1, 4), (10, 10), [1, 2, 3, 4]]
    print(sum_numbers(seq))
    print('Expected: 38')
    test2 = [(3, 1, 4), (10, 10), [1, 1, 1, 1]]
    print(sum_numbers(test2))
    print('Expected: 32')
def sum_numbers(seq_seq):
    """
    Returns the sum of the numbers in the given sequence
    of subsequences.  For example, if the given argument is:
        [(3, 1, 4), (10, 10), [1, 2, 3, 4]]
    then this function returns    38
    (which is 3 + 1 + 4 + 10 + 10 + 1 + 2 + 3 + 4).
    Preconditions:  the given argument is a sequences of sequences,
                    and each item in the subsequences is a number.
    """
    # TODO: 2b. Implement and test this function.
    sum = 0
    for k in range(len(seq_seq)):
        for j in range(len(seq_seq[k])):
            sum = sum + seq_seq[k][j]
    return sum
def test_print_characters():
    """ Tests the    print_characters    function. """
    # TODO: 3a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    print()
    print('------------------------------------------')
    print('Testing the   PRINT_CHARACTERS   function:')
    print('------------------------------------------')
    test1 = ['hi', 'bye', ' a tie!']
    print(print_characters(test1))
    test2 = ['hello there', 'My name is jack']
    print(print_characters(test2))
def print_characters(sequence_of_strings):
    """
    Prints all the characters in the sequence of strings,
    but each character on ITS OWN LINE.  For example,
    if the given argument is ['hi', 'bye', ' a tie!'],
    then this function prints:
       h
       i
       b
       y
       e
      
       a

       t
       i
       e
       !
    Precondition:  the given argument is a sequence of strings.
    """
    # TODO: 3b. Implement and test this function.
    for k in range(len(sequence_of_strings)):
        for j in range(len(sequence_of_strings[k])):
            print(sequence_of_strings[k][j])


def test_print_characters_slanted():
    """ Tests the    print_characters_slanted    function. """
    # TODO: 4a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    print()
    print('--------------------------------------------------')
    print('Testing the   PRINT_CHARACTERS_SLANTED   function:')
    print('--------------------------------------------------')
    test1 = ['hi', 'bye', 'a tie!']
    print(print_characters_slanted(test1))
    test2 = ['hey There', 'Neighbor']
    print(print_characters_slanted(test2))
def print_characters_slanted(sequence_of_strings):
    """
    Same as the previous problem, but each string 'slants'.
    For example, if the given argument is ['hi', 'bye', 'a tie!'],
    then this function prints:
       h
        i
       b
        y
         e
       a

         t
          i
           e
            !
    Precondition:  the given argument is a sequence of strings.
    """
    # TODO: 4b. Implement and test this function.
    slant = ' '
    for k in range(len(sequence_of_strings)):
        for j in range(len(sequence_of_strings[k])):
            print(slant * j, sequence_of_strings[k][j])


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
