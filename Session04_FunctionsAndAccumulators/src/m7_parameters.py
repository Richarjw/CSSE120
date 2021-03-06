"""
This module lets you experience the POWER of FUNCTIONS and PARAMETERS.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Jack Richard.  December 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg
import math

# ----------------------------------------------------------------------
# TODO 2. READ THIS:
#   The goal of this exercise is for you to see the POWER
#   of functions with parameters.  To that end, you will:
#      a. Briefly study a function (four_dots) that displays
#            4 dots on a window.
#      b. Make a five_dots function by using COPY-AND-PASTE
#            on four_dots and making the obvious changes.
#      c. Repeat the previous step to make a six_dots function.
#
#      At that point, you will:
#         -- Notice that you could continue making functions
#              this way, using copy-and-paste
#         -- Realize that there has to be a better approach
#              that ABSTRACTS the 4_dots, 5_dots, 6_dots, etc.
#              to an   n_dots   function.
#         -- Notice the key is to have   n_dots   have a PARAMETER
#              that specifies the number of dots!
#
#      You will continue by doing this:
#
#      d. Implement n_dots.
#      e. See how   n_dots   and loops
#            can be used to make really cool designs in a window.
#            So, you will see the POWER of functions with PARAMETERs.
#
#   Examine (NOW) the dots.pdf document in this project to see
#   what the functions you will implement will produce.
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# TODO: 3. STUDY the next three functions:
#              main
#              test_four_dots
#              four_dots
#          asking questions as needed.
#          Do NOT proceed until you understand these three functions.
#          Do NOT modify these three functions.
# ----------------------------------------------------------------------
def main():
    """ Calls the   TEST   functions in this module. """
    test_four_dots()
    test_five_dots()
    test_six_dots()
    test_n_dots()
    test_one_to_n_dots()


def test_four_dots():
    """ Tests the   four_dots   function. """
    four_dots()


def four_dots():
    """
    1. Constructs a GraphWin with a reasonable title and size.
    2. Displays four blue dots, equally spaced around a center point.
    3. Displays a message, waits for the user to click,
          then closes the window.
    """
    window = rg.RoseWindow(300, 300)
    center = rg.Point(150, 150)
    radius = 75

    for k in range(4):  # 4 points, at 0, 90, 180, 270 degrees
        theta = k * 2 * math.pi / 4  # theta is the angle in radians
        x = center.x + radius * math.cos(theta)  # Polar coordinates
        y = center.y + radius * math.sin(theta)  # converted to x/y
        point = rg.Point(x, y)

        dot_size = 10
        dot = rg.Circle(point, dot_size)
        dot.fill_color = 'blue'
        dot.attach_to(window.initial_canvas)

    window.close_on_mouse_click()


def test_five_dots():
    """ Tests the   five_dots   function. """
    five_dots()


def five_dots():
    """ Same as four_dots, but 5 dots instead of 4. """
    # TODO: 4. Implement and test this function.
    #    NOTE: For now, just COPY-AND-PASTE from four_dots
    #          and modify as needed.  You'll see a better approach soon.
    window = rg.RoseWindow(300, 300)
    center = rg.Point(150, 150)
    radius = 75

    for k in range(5):  # 4 points, at 0, 90, 180, 270 degrees
        theta = k * 2 * math.pi / 5  # theta is the angle in radians
        x = center.x + radius * math.cos(theta)  # Polar coordinates
        y = center.y + radius * math.sin(theta)  # converted to x/y
        point = rg.Point(x, y)

        dot_size = 10
        dot = rg.Circle(point, dot_size)
        dot.fill_color = 'blue'
        dot.attach_to(window.initial_canvas)

    window.close_on_mouse_click()



def test_six_dots():
    """ Tests the   six_dots   function. """
    six_dots()


def six_dots():
    """ Same as four_dots, but 6 dots instead of 4. """
    # TODO: 5. Implement and test this function.
    #    NOTE: For now, just COPY-AND-PASTE from four_dots
    #          and modify as needed.  You'll see a better approach soon.
    window = rg.RoseWindow(300, 300)
    center = rg.Point(150, 150)
    radius = 75

    for k in range(6):  # 4 points, at 0, 90, 180, 270 degrees
        theta = k * 2 * math.pi / 6  # theta is the angle in radians
        x = center.x + radius * math.cos(theta)  # Polar coordinates
        y = center.y + radius * math.sin(theta)  # converted to x/y
        point = rg.Point(x, y)

        dot_size = 10
        dot = rg.Circle(point, dot_size)
        dot.fill_color = 'blue'
        dot.attach_to(window.initial_canvas)

    window.close_on_mouse_click()


def test_n_dots():
    """ Tests the   n_dots   function. """
    # TODO: 6a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 3 tests.
    n_dots(10)
    n_dots(8)
    n_dots(7)

def n_dots(n):
    """
    Same as six_dots, but n dots instead of 6,
    where n is the GIVEN PARAMETER.

    Pre-condition:  The given argument n is a non-negative integer.
    """
    # TODO: 6b. Implement and test this function.
    #    NOTE: One last time, just COPY-AND-PASTE from   six_dots
    #          and modify as needed.
    #          *** Be sure to USE THE PARAMETER n. ***
    #
    #    THINK ABOUT: Why is this function MUCH more powerful than
    #                 four_dots, five_dots, and six_dots?
    #                 (If you don't soon see the answer, ASK SOMEONE!)
    window = rg.RoseWindow(300, 300)
    center = rg.Point(150, 150)
    radius = 75

    for k in range(n):  # 4 points, at 0, 90, 180, 270 degrees
        theta = k * 2 * math.pi / n  # theta is the angle in radians
        x = center.x + radius * math.cos(theta)  # Polar coordinates
        y = center.y + radius * math.sin(theta)  # converted to x/y
        point = rg.Point(x, y)

        dot_size = 10
        dot = rg.Circle(point, dot_size)
        dot.fill_color = 'blue'
        dot.attach_to(window.initial_canvas)

    window.close_on_mouse_click()


def test_one_to_n_dots():
    """ Tests the   one_to_n_dots   function. """
    # TODO: 7a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 2 tests.
    one_to_n_dots(5)
def one_to_n_dots(n):
    """
    Draws 1 blue dot, then 2, then 3, ... then n, where each SET of dots
    (i.e., each set of n dots produced by a call to this function)
    is on its OWN window and each set of dots is equally spaced around
    a center point.  See   dots.pdf   in this project for an example.

    Pre-condition:  The given argument n is a non-negative integer.
    """
    # TODO: 8. Implement and test this function.
    #    NOTE: This function takes just  *** TWO ***  lines of code.
    #          No more than 2 lines allowed!
    #          Ask yourself: 1 dot, then 2, then 3, then ... what does
    #          that suggest you use?
    for k in range(1, n + 1):
        n_dots(k)
# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
