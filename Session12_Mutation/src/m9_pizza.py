"""
This module lets you practice:
  -- ITERATING (i.e. LOOPING) thru a SEQUENCE
  -- Using OBJECTS
  -- DEFINING functions
  -- CALLING functions

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Jack Richard.  January 2014.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg
import math


def main():
    """ Calls the   TEST   functions in this module. """
    test_draw_points_on_circle()
    test_pizza()
    test_polygon()
    test_fancy_polygon()


# ----------------------------------------------------------------------
# Students: You MUST use this   generate_points_on_circle   function
#           in the exercises that follow.
#           It is ALREADY DONE - you must NOT modify it or add to it.
# ----------------------------------------------------------------------
def generate_points_on_circle(circle, number_of_points_to_generate):
    """
    Returns a list containing the given number of rg.Points,
    where the rg.Points:
      -- all lie on the circumference of the given rg.Circle,
      -- are equally distant from each other, and
      -- go clockwise around the circumference of the given rg.Circle,
            starting at the rightmost point on the rg.Circle.

    See the 'draw_points_on_circle' pictures  in the   pizza.pdf
    file attached, with the points shown on those pictures.

    Preconditions:
      :type circle: rg.Circle
      :type number_of_points_to_generate: int
    where number_of_points_to_generate is nonnegative.
    """
    radius = circle.radius
    center_x = circle.center.x
    center_y = circle.center.y

    # ------------------------------------------------------------------
    # Each point is   delta_degrees   from the previous point,
    # along the circumference of the given circle.
    # ------------------------------------------------------------------
    delta_degrees = 360 / number_of_points_to_generate

    points = []
    degrees = 0
    for _ in range(number_of_points_to_generate):

        # --------------------------------------------------------------
        # Compute x and y of the point on the circumference of the
        # circle by using a polar representation.
        # --------------------------------------------------------------
        angle = math.radians(degrees)
        x = radius * math.cos(angle) + center_x
        y = radius * math.sin(angle) + center_y

        # --------------------------------------------------------------
        # Construct the point and append it to the list.
        # --------------------------------------------------------------
        point_on_circumference = rg.Point(x, y)
        points.append(point_on_circumference)

        # --------------------------------------------------------------
        # The next point will be    delta_degrees    from this point,
        # along the circumference of the given circle.
        # --------------------------------------------------------------
        degrees = degrees + delta_degrees

    return points


def test_draw_points_on_circle():
    """ Tests the   draw_points_on_circle   function. """
    # TODO: 2a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 2 tests, i.e., 2 calls to the function to test.
    window = rg.RoseWindow(800, 800)
    circle = rg.Circle(rg.Point(400, 400), 100)
    circle2 = rg.Circle(rg.Point(400, 400), 200)
    number = 6
    color = 'blue'
    draw_points_on_circle(window, circle, number, color)
    number = 8
    color = 'green'
    draw_points_on_circle(window, circle2, number, color)
    window.close_on_mouse_click()

def draw_points_on_circle(window, circle, number_of_points, color):
    """
    See the 'draw_points_on_circle' pictures in   pizza.pdf   in this
    project; they may help you better understand the following
    specification:

    1. Attaches the given rg.Circle to the initial_canvas
         of the given rg.RoseWindow.
    2. Constructs the given number of rg.Point objects on the given
          rg.Circle's circumference, spaced equally from each other.
    3. For each of those rg.Point objects:
       a. Constructs an rg.Circle centered at that point,
            filled with the given color and with a radius of 10.
       b. Attaches the new rg.Circle to the initial_canvas
            of the given rg.RoseWindow.
       c. Attaches the rg.Point object to the initial_canvas
            of the given rg.RoseWindow.
    4. Renders the given rg.RoseWindow.

    Note that the rg.Point objects will generally be visible
    since they are on TOP of the zg.Circle objects.

    Pre-conditions:
      :type window: rg.RoseWindow
      :type circle: rg.Circle
      :type number_of_points: int
      :type color: (str, rg.Color)
    where the number_of_points is nonnegative and the color is either
    a string that Rosegraphics understands or a rg.Color object.
    """
    # TODO: 2b. With your instructor:
    #   -- READ and UNDERSTAND the   generate_points_on_circle  function
    #         (defined above).
    #   -- Implement and test this function.
    #
    # IMPLEMENTATION REQUIREMENT:
    #    You MUST USE (call) the   generate_points_on_circle
    #    (defined above) to generate the points to draw.
    list = generate_points_on_circle(circle, number_of_points)
    circle.attach_to(window.initial_canvas)
    for k in range(len(list)):
        newCircle = rg.Circle(list[k], 10)
        newCircle.fill_color = color
        newCircle.attach_to(window.initial_canvas)
        list[k].attach_to(window.initial_canvas)
        window.render()

def test_pizza():
    """ Tests the   pizza   function. """
    # TODO: 3a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 2 tests, i.e., 2 calls to the function to test.
    window = rg.RoseWindow(800, 800)
    circle = rg.Circle(rg.Point(400, 400), 100)
    number = 5
    color = 'blue'
    pizza(window, circle, number, color)
    number = 10
    color = 'black'
    circle2 = rg.Circle(rg.Point(600, 600), 20)
    pizza(window, circle2, number, color)
    window.close_on_mouse_click()

def pizza(window, circle, number_of_slices, color):
    """
    See the 'pizza' pictures in   pizza.pdf   in this project;
    they may help you better understand the following specification:

    1. Draws the given rg.Circle in the given rg.RoseWindow.
    2. Constructs and draws rg.Line objects to make the picture
         look like a 'pizza pie' cut into the given number of 'slices'.
         Each line has the given color and width (thickness) 3.

     Pre-conditions:
      :type window: rg.RoseWindow
      :type circle: rg.Circle
      :type number_of_slices: int
      :type color: (str, rg.Color)
    where the number_of_slices is at least 2 and the color is either
    a string that Rosegraphics understands or a rg.Color object.
    """
    # TODO: 3b. Implement and test this function.
    #
    # IMPLEMENTATION REQUIREMENT:
    #    You MUST USE (call) the   generate_points_on_circle
    #    (defined above) to generate points on the circle,
    #    then draw lines based in part on those points.
    circle.attach_to(window.initial_canvas)
    list = generate_points_on_circle(circle, number_of_slices)
    for k in range(len(list)):
        newLine = rg.Line(circle.center, list[k])
        newLine.thickness = 3
        newLine.color = color
        newLine.attach_to(window.initial_canvas)
        window.render()


def test_polygon():
    """ Tests the   polygon   function. """
    # TODO: 4a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 2 tests, i.e., 2 calls to the function to test.
    window = rg.RoseWindow(800, 800)
    circle = rg.Circle(rg.Point(200, 200), 50)
    number = 4
    color = 'yellow'
    polygon(window, circle, number, color)
    number = 8
    color = 'blue'
    circle2 = rg.Circle(rg.Point(600, 400), 200)
    polygon(window, circle2, number, color)
    window.close_on_mouse_click()
def polygon(window, circle, number_of_segments, color):
    """
    See the 'polygon' pictures in   pizza.pdf   in this project;
    they may help you better understand the following specification:

    1. Draws the given rg.Circle in the given rg.RoseWindow.
    2. Constructs and draws rg.Line objects to make the picture
         look like an inscribed regular polygon with the given
         number of segments.
         Each line has the given color and width (thickness) 3.

     Pre-conditions:
      :type window: rg.RoseWindow
      :type circle: rg.Circle
      :type number_of_segments: int
      :type color: (str, rg.Color)
    where the number_of_segments is at least 3 and the color is either
    a string that Rosegraphics understands or a rg.Color object.
    """
    # TODO: 4b. Implement and test this function.
    #
    # IMPLEMENTATION REQUIREMENT:
    #    You MUST USE (call) the   generate_points_on_circle
    #    (defined above) to generate points on the circle,
    #    then draw lines based in part on those points.
    circle.attach_to(window.initial_canvas)
    list = generate_points_on_circle(circle, number_of_segments)
    for k in range(len(list)):
        if k != len(list) - 1:
            newLine = rg.Line(list[k], list[k + 1])
            newLine.thickness = 3
            newLine.color = color
            newLine.attach_to(window.initial_canvas)
        else:
            newLine = rg.Line(list[k], list[0])
            newLine.thickness = 3
            newLine.color = color
            newLine.attach_to(window.initial_canvas)
        window.render()

def test_fancy_polygon():
    """ Tests the   polygon   function. """
    # TODO: 5a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 2 tests, i.e., 2 calls to the function to test.
    # Indeed, try a variety of tests to get some really cool pictures.
    # Some that I especially like are:
    #    -- 20 segments, hops of length 7
    #    -- 50 segments, hops of length 25
    #    -- 100 segments, hops of length 30
    window = rg.RoseWindow(800, 800)
    circle = rg.Circle(rg.Point(400, 400), 150)
    segments = 5
    nextPoint = 2
    color = 'blue'
    fancy_polygon(window, circle, segments, nextPoint, color)
    window.close_on_mouse_click()
    window = rg.RoseWindow(800, 800)
    segments = 20
    nextPoint = 7
    color = 'green'
    fancy_polygon(window, circle, segments, nextPoint, color)

def fancy_polygon(window, circle, number_of_segments,
                  hops_to_next_point, color):
    """
    See the 'fancy_polygon' pictures in   pizza.pdf   in this project;
    they may help you better understand the following specification:

    1. Draws the given rg.Circle in the given rg.RoseWindow.
    2. Constructs and draws rg.Line objects to make the picture
         look like an inscribed regular polygon with the given
         number of segments, but with each rg.Line going from one point
         on the given zg.Circle to the point on the given zg.Circle
         that is the given number of 'hops' away (wrapping as needed).
         Each line has the given color and width (thickness) 3.

         For example, if hops_to_next_point is 1,
            then the picture is a regular polygon.
         Or, if hops_to_next_point is 2, the lines go:
           -- from point 0 to point 2
           -- from point 1 to point 3
           -- from point 2 to point 4
           -- etc.
         One more example:
           if  hops_to_next_point  is 3 and  number_of_segments  is 5,
           then the lines go:
           -- from point 0 to point 3
           -- from point 1 to point 4
           -- from point 2 to point 0 (note the 'wrap' effect)
           -- from point 3 to point 1
           -- from point 4 to point 2

     Pre-conditions:
      :type window: rg.RoseWindow
      :type circle: rg.Circle
      :type number_of_segments: int
      :type hops_to_next_point: int
      :type color: (str, rg.Color)
    where the number_of_segments is at least 3,
    the hops_to_next_point is at least 1
    and less than number_of_segments, and the color is either
    a string that Rosegraphics understands or a rg.Color object.
    """
    # TODO: 5b. Implement and test this function.
    #
    # IMPLEMENTATION REQUIREMENT:
    #    You MUST USE (call) the   generate_points_on_circle
    #    (defined above) to generate points on the circle,
    #    then draw lines based in part on those points.
    #
    # HINT: One way to do "wrapping" is to use the  %  operator
    #       appropriately.  THIS REQUIRES SOME THOUGHT - ask as needed.
    circle.attach_to(window.initial_canvas)
    list = generate_points_on_circle(circle, number_of_segments)
    num = 0
    for k in range(len(list)):
        num = k - 1
        if num + hops_to_next_point >= number_of_segments:
            next = number_of_segments - num - 1
            newLine = rg.Line(list[num], list[next])
            num = next
            newLine.thickness = 3
            newLine.color = color
            newLine.attach_to(window.initial_canvas)
            window.render(.5)
        else:
            newLine = rg.Line(list[num], list[num + hops_to_next_point])
            newLine.thickness = 3
            newLine.color = color
            newLine.attach_to(window.initial_canvas)
            window.render(0.5)
        window.render()



# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
