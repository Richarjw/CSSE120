."""
A simple   Rectangle   class.
NOTE: This is NOT rosegraphics -- it is your OWN Rectangle class.

Authors: David Mutchler, Mark Hays, Michael Wollowski, Amanda Stouder,
         Chandan Rupakheti, Katie Dion, Claude Anderson, Delvin Defoe,
         Curt Clifton, Matt Boutell, Dave Fisher and their colleagues,
         and PUT YOUR NAME HERE.  October 2014.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import m1e_Point as pt
import m2_Circle as cir


def main():
    """ Not used here, but could be used for informal testing. """
    # Put your tests in the   m3_test_Rectangle  module, NOT here.
    pass


# ----------------------------------------------------------------------
# TODO:  Define here a class called   Rectangle   that represents a
#        rectangle whose sides are parallel to the x and y axes.
#        It has:
#   Instance variables:
#     -- corner1 (stored as a Point)
#     -- corner2 (stored as a Point)
#          where corner2 is the corner of the Rectangle opposite corner1
#        Do NOT assume that corner1 is any particular corner -- allow
#        for it to be any of the 4 possible corners.
#   Methods:
#     __init__: Takes two required parameters, corner1 and corner2,
#               both of which must be Point objects.
#               Sets this Rectangle's opposite corners
#               to the given points.
#     __repr__: Returns a string that represents this Circle
#               as in this example:
#                 'Rectangle(corners = Point(100, 32.7), Point(50, 90))'
#     clone:    Returns a new Rectangle that is a copy of this Rectangle.
#     move_by:  Takes two arguments, dx and dy, both numbers.
#               Moves this Rectangle by dx and dy, respectively.
#     corners:  Returns a list of the 4 Point objects that are corners
#               of this Rectangle.
#     contains: Takes a Point p.
#               Returns True if this Rectangle contains p,
#               else returns False.  We will say that the Rectangle
#               DOES contain p if p is on the Rectangle's border.
#     intersects:  Takes another Rectange as an argument.
#                  Returns True if this Rectangle and the other
#                  Rectangle intersect, else returns False.
#                    -- Hint: they intersect if one of the Rectangles
#                       contains at least one of the corners
#                       of the other Rectangle.
#     sub_circle:  Returns the largest Circle that fits inside
#                  this Rectangle and is centered within this Rectangle.
#     super_rectangle: Takes a list of Rectangles as an argument.
#                      Returns a new Rectangle that is the smallest
#                      Rectangle that contains all the Rectangles in
#                      the given list.
#
# Include appropriate docstrings with the methods that you define
# (copy-and-paste from the above makes it easy to do so).
# Test your class definition using the   m2_test_Rectangle    module.
#   ** TEST EACH METHOD AS YOU DEFINE IT. **
#
# Wherever reasonable, CALL methods previously defined rather than
# copying the code of those methods.
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
class Rectangle(object):
    
    def __init__(self,corner1):
    