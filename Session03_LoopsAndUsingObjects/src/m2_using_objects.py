"""
This module lets you practice  ** using objects **,
including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA
       -- via INSTANCE VARIABLES (aka FIELDS) and GETTERS.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Jack Richard.  December 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # TODO: 2. Implement and test this function.
    olympic_rings()

def two_circles():
    """
    -- Constructs a window, i.e., a rg.RoseWindow.
    -- Constructs and draws two rg.Circles on the window such that:
         -- They fit in the window and are easily visible.
         -- They have different radii.
         -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # TODO: 3. Implement and test this function.
    #       ANY two rg.Circle objects that meet the criteria are fine.
    #       If you wish, see the list of colors in the attached file:
    #           Named_Colors.pdf
    window = rg.RoseWindow(600, 600)
    center1 = rg.Point(200, 200)
    radius1 = 50
    center2 = rg.Point(400, 400)
    radius2 = 60
    circle1 = rg.Circle(center1, radius1)
    circle2 = rg.Circle(center2, radius2)
    circle1.fill_color = 'blue'
    circle2.fill_color = 'green'
    circle1.attach_to(window.main_canvas)
    circle2.attach_to(window.main_canvas)
    window.render(3)
    window.close_on_mouse_click()


def circle_and_rectangle():
    """
    -- Constructs a window, i.e., a rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
          -- The rg.Rectangle is outlined with 'red'.
    -- Prints (on the console) the following data associated
         with your rg.Rectangle:
          -- Its outline thickness.
          -- Its outline color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.

       Here is an example of the output on the console,
       for one particular rectangle:
           1
           black
           Point(225.0,150.0)
           225.0
           150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # TODO: 4. Implement and test this function.
    #            -- ANY objects that meet the criteria are fine.
    # HINT:    Use the DOT TRICK to figure out how to
    #          construct a Rectangle and do stuff with it.

    window = rg.RoseWindow(600, 600)
    center = rg.Point(200, 200)
    radius = 30
    circle = rg.Circle(center, radius)
    circle.fill_color = 'blue'
    point1 = rg.Point(400, 400)
    point2 = rg.Point(500, 550)
    rect = rg.Rectangle(point1, point2)
    rect.fill_color = 'red'
    rect.outline_color = 'black'
    rect.outline_thickness = 1
    circle.attach_to(window.main_canvas)
    rect.attach_to(window.main_canvas)
    window.render(3)
    window.close_on_mouse_click()
    centerPoint = rect.find_center()

    print(rect.outline_thickness)
    print(rect.outline_color)
    print(centerPoint)
    print(centerPoint.x)
    print(centerPoint.y)


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5,150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # TODO: 5. Implement and test this function.
    window = rg.RoseWindow(600, 600)
    point1 = rg.Point(200, 200)
    point2 = rg.Point(300, 300)
    point3 = rg.Point(100, 100)
    point4 = rg.Point(100, 500)
    line1 = rg.Line(point1, point2)
    line2 = rg.Line(point3, point4)
    line2.thickness = 10
    line1.attach_to(window.main_canvas)
    line2.attach_to(window.main_canvas)
    window.render(2)
    center2 = line2.find_midpoint()
    print(center2)
    print(center2.x)
    print(center2.y)
    window.close_on_mouse_click()


def olympic_rings():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window a simplified version of
       the Olympic rings, colored per the (approximate) Olympic colors.
    -- Waits for the user to press the mouse, then closes the window.

    See    m2_olympic_rings.pdf   in this project for a picture
    of the drawing that you should produce.  Colors need not be exact.

    This problem is taken from page 83 of Python for Everyone,
      by Horstmann and Necaise.
    """
    # TODO: 6. Implement and test this function.
    # HINTs:
    #   -- See    Named_Colors.pdf  in this project
    #        for a list of named colors that you can use as strings
    #        in    setOutline    and    setFill   (and other methods).
    #   -- For swatches showing those colors, visit the Graphics
    #        resources on the course home page.
    #   -- Work an example BY HAND to figure out the GEOMETRY
    #        required for a solution to this problem.
    window = rg.RoseWindow(600, 600)
    radius = 100
    centerB = rg.Point(100, 100)
    centerBl = rg.Point(250, 100)
    centerR = rg.Point(400, 100)
    centerY = rg.Point(180, 200)
    centerG = rg.Point(330, 200)
    blue = rg.Circle(centerB, radius)
    black = rg.Circle(centerBl, radius)
    red = rg.Circle(centerR, radius)
    yellow = rg.Circle(centerY, radius)
    green = rg.Circle(centerG, radius)
    blue.outline_color = 'blue'
    black.outline_color = 'black'
    red.outline_color = 'red'
    yellow.outline_color = 'yellow'
    green.outline_color = 'green'
    blue.outline_thickness = 4
    black.outline_thickness = 4
    red.outline_thickness = 4
    yellow.outline_thickness = 4
    green.outline_thickness = 4
    blue.attach_to(window.main_canvas)
    black.attach_to(window.main_canvas)
    red.attach_to(window.main_canvas)
    yellow.attach_to(window.main_canvas)
    green.attach_to(window.main_canvas)
    window.render(1)
    window.close_on_mouse_click()

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
