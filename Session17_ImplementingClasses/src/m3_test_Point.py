"""
Tests the   Point  class
that is defined in the imported   m3_Point   module.

Authors: David Mutchler, Mark Hays, Michael Wollowski, Amanda Stouder,
         Chandan Rupakheti, Katie Dion, Claude Anderson, Delvin Defoe,
         Curt Clifton, Matt Boutell, Dave Fisher, their colleagues,
         and PUT YOUR NAME HERE.  October 2014.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE

import m3_Point as pt


def main():
    """
    Tests the   Point   class defined in the imported   pt  module.
    """
    # TODO: Add code below (at the appropriate places)
    #       to test your   Point   class as you implement it.
    print('------------------------------------')
    print('Testing __init__:')
    test = pt.Point(20, 20)
    print(test.x, test.y)
    print('\n------------------------------------')
    print('Testing __repr__:')
    print(test)
    print('\n------------------------------------')
    print('Testing move_to:')
    test.move_to(50, 50)
    print(test.x, test.y)
    print(test)
    print('\n------------------------------------')
    print('Testing move_by:')
    test.move_by(20, 20)
    print(test.x, test.y)
    print(test)
    print('\n------------------------------------')
    print('Testing distance_from:')
    print(test.distance_from(pt.Point(0, 70)))
    print(str(70))
    print('\n------------------------------------')
    print('Testing closer_to:')
    print(test.closer_to(pt.Point(0, 0), pt.Point(50, 50)))
    print(pt.Point(50, 50))
    print('\n------------------------------------')
    print('Testing halfway_to:')
    print(test.halfway_to(pt.Point(0, 0)))
    print(pt.Point(35, 35))

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
