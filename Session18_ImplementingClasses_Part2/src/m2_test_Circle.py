"""
Tests the   Circle  class
that is defined in the imported   m2_Circle   module.

Authors: David Mutchler, Mark Hays, Michael Wollowski, Amanda Stouder,
         Chandan Rupakheti, Katie Dion, Claude Anderson, Delvin Defoe,
         Curt Clifton, Matt Boutell, Dave Fisher, their colleagues,
         and Jack Richard.  October 2014.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE

import m1e_Point as pt
import m2_Circle as cir


def main():
    """
    Tests the   Circle   class defined in the imported   cir  module.
    """
    # TODO: Add code below (at the appropriate places)
    #       to test your   Circle   class as you implement it.
    #       Be sure that your tests print the EXPECTED results of the
    #       tests as well as the ACTUAL results from the function calls.
    print('------------------------------------')
    print('Testing __init__:')
    circle = cir.Circle()
    circle._init_(pt.Point(400, 400), 100)
    print(circle.center, circle.radius)
    print('\n------------------------------------')
    print('Testing __repr__:')
    print(circle._repr_())
    print('\n------------------------------------')
    print('Testing clone:')
    print(circle.clone())
    print('\n------------------------------------')
    print('Testing move_by:')
    circle.move_by(10, 10)
    print(circle.center)
    print('\n------------------------------------')
    print('Testing intersects:')
    circle2 = cir.Circle(pt.Point(400, 450), 100)
    print(circle.intersects(circle2))
    print('\n------------------------------------')
    print('Testing closer_to_origin:')
    print(circle.closer_to_origin(circle2))
    print('\n------------------------------------')
    print('Testing super_circle:')


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
