"""
PRACTICE Test 3, problem 2.

Authors: David Mutchler, Mark Hays, Michael Wollowski,
         Chandan Rupakheti, Matt Boutell, Dave Fisher,
         Claude Anderson, and Jack Richard.  October 2014.
"""  # TODO: PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    test_integers()


def test_integers():
    """ Tests the    integers    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   integers   function:')
    print('--------------------------------------------------')

    # ------------------------------------------------------------------
    # TODO: Implement this function, using it to test the NEXT function.
    #       Write the two functions in whichever order you prefer.
    #
    # IMPORTANT: Include  *** at least 3 REASONABLY GOOD tests ***.
    #            Indicate EXPECTED answers for each test.
    # ------------------------------------------------------------------
    test1 = [(3, 1, 4),
         (10, 'hi', 10),
         [1, 2.5, 3, 4],
         'hello',
         [],
         ['oops'],
         [[55], [44]],
         [30, -4]
        ]
    print(integers(test1))

def integers(sequence_of_sequences):
    """
    Returns a new list that contains all the integers
    in the subsequences of the given sequence, in the order that they
    appear in the subsequences.
    For example, if the argument is:
        [(3, 1, 4),
         (10, 'hi', 10),
         [1, 2.5, 3, 4],
         'hello',
         [],
         ['oops'],
         [[55], [44]],
         [30, -4]
        ]
    then this function returns:
        [3, 1, 4, 10, 10, 1, 3, 4, 30, -4]

    Precondition:  the given argument is a sequence of sequences.
    """

    # ------------------------------------------------------------------
    # TODO: Implement and test this function.
    # HINT: The   type   function indicates whether or not its argument
    #       is an integer.  For example:
    #         -- type(34) is True
    #         -- type(4.6) is False
    #         -- type('three') is False
    #         -- type([1, 2, 3]) is False
    # ------------------------------------------------------------------
    sequence = []
    for k in range(len(sequence_of_sequences)):
        for j in range(len(sequence_of_sequences[k])):
            if type(sequence_of_sequences[k]):
                sequence.append(sequence_of_sequences[k][j])
    return sequence

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
