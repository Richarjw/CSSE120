"""
PRACTICE Test 1, problem 4.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Jack Richard.  December 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    test_problem4a()
    test_problem4b()


def test_problem4a():
    """ Tests the   problem4a   function. """
    # TODO: 2a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 2 tests, i.e., 2 calls to the function to test.
    # NOTE: Be sure to test the RETURNED VALUE from the function.
    window = rg.RoseWindow(800, 800)
    point = rg.Point(200, 200)
    point2 = rg.Point(600, 400)
    print(problem4a(window, point, 10))



def problem4a(window, point, n):
    """
    See   problem4a_picture.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws a sequence of  n  rg.Lines on the given rg.RoseWindow,
    as follows:
      -- There are the given number (n) of rg.Lines.
      -- Each rg.Line is vertical and has length 50.
            (All units are pixels.)
      -- The top of the first (leftmost) rg.Line
            is at the given rg.Point.
      -- Each successive rg.Line is 20 pixels to the right
            and 10 pixels down from the previous rg.Line.
      -- The first rg.Line has thickness 1.
      -- Each successive rg.Line has thickness 2 greater than
         the zg.Line to its left, but no greater than 13.
           (So once a rg.Line has thickness 13,
           it and all the rg.Lines to its right have thickness 13.)

    Returns the sum of the thicknesses of the rg.Line's.

    Preconditions:
        :type window: rg.RoseWindow
        :type point: rg.Point
      The third argument is a positive integer
      and the given point is inside the given window.
    """
    # TODO: 2b. Implement and test this function.
    sum = 1
    x = point.x
    y = point.y
    thickness = 1
    point2 = rg.Point(x, y + 50)
    for k in range(0, n):
        x = x + 20
        y = y + 10
        newPoint = rg.Point(x, y)
        newPoint2 = rg.Point(x, y + 50)
        newline = rg.Line(newPoint, newPoint2)
        if thickness < 12:
            thickness = thickness + 2
        sum = sum + thickness
        newline.thickness = thickness
        newline.attach_to(window.initial_canvas)
        window.render()
    window.close_on_mouse_click()
    return sum
def test_problem4b():
    """ Tests the   problem4b   function. """
    # Test 1 is ALREADY DONE (here).
    result = problem4b(4, rg.Point(100, 50))
    print('The value returned should be: 158')
    print('The value returned is in fact:', result)

    # Test 2 is ALREADY DONE (here).
    result = problem4b(7, rg.Point(30, 30))
    print('The value returned should be: ???')
    print('The value returned is in fact:', result)


def problem4b(m, point1):
    """
    See   problem4b_picture.pdf   in this project for pictures that may
    help you better understand the following specification:

    Constructs and displays an rg.RoseWindow
    that is 400 wide by 600 tall.
    Draws, on the rg.RoseWindow, m SETS of lines, where:
      -- Each SET of lines is drawn by a call to problem4a.
      -- The first set has 3 lines that start at point p
           (the given point).
      -- The second set has 5 lines that start 60 pixels
           directly below p.
      -- The third set has 7 lines that start 120 pixels
           directly below p.
      -- The fourth set has 9 lines that start 180 pixels
           directly below p.
      -- etc until m SETS of lines are drawn (where m is given)
    Each set of lines should have widths (thicknesses) per problem4a.

    Waits for the user to click the mouse (and displays an appropriate
    message prompting the user to do so), then closes the window.

    Returns the sum of the thicknesses of ALL of the lines drawn
    (over all m sets of lines).

    Preconditions:
        :type point1: rg.Point
    and the first argument is a positive integer.
    """
    # TODO: 3. Implement and test this function.
    #     The testing code is already written for you (above).
    # IMPLEMENTATION REQUIREMENT:
    #     This function must CALL problem4a appropriately.
    window = rg.RoseWindow(400, 600)
    result = 0
    x = point1.x
    y = point1.y
    for k in range(m):
        newPoint = rg.Point(x, y + k * 60)
        n = 3 + 2 * k
        total = problem4a(window, newPoint, n)
        result = result + total
    return result

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
