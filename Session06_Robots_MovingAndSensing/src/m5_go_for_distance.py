"""
This module lets you practice using Create MOVEMENT and SENSORS,
in particular the DISTANCE and ANGLE sensors.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Dave Fisher, Matt Boutell, Curt Clifton,
         their colleagues, and PUT YOUR NAME HERE.  December 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import new_create
import time


def main():
    """ Tests the   go_by_time  function. """
    # TODO: 2a. Implement and test this function.
    # CAUTION:  Be sure to construct a SINGLE robot
    #           and do a robot.shutdown() at the end of main.

    port = 3
    robot = new_create.Create(port)

    go_by_time(robot, -50, 10)
    robot.shutdown()

def go_by_time(robot, centimeters, centimeters_per_second):
    """
    Makes the given robot go straight the given number of centimeters
    at the given speed (in centimeters per second), then stop.
      Positive centimeters means go forward;
      negative centimeters means go backwards.

    Returns the number of centimeters that the robot reports
    that it went (positive if it went forward, negative otherwise).

    IMPLEMENTATION REQUIREMENT:  Use this algorithm
       (which we'll call the   "time"   algorithm):
         0. Compute the TIME the robot must move to achieve the
              requested DISTANCE at the requested SPEED.
         1. Start the robot moving at the requested speed.
         2. Sleep the computed time.
         3. Stop the robot.

    Preconditions: The arguments satisfy:
      :type robot: new_create.Create
      :type centimeters: float
      :type centimeters_per_second: float
          with centimeters_per_second being positive.
    """
    # TODO: 2b. Implement and test this function.
    #
    # NOTE: Use the REQUIRED ALGORITHM TO IMPLEMENT,
    #       per the specification, with the required restrictions on
    #       the arguments (in particular, centimeters_per_second > 0).
    #
    # HINT: ** First solve this problem BY HAND on an example! **

    assert(isinstance(robot, new_create.Create))
    assert(isinstance(centimeters, (int, float)))
    assert(isinstance(centimeters_per_second, (int, float)))
    assert(centimeters_per_second > 0)
    sensor1 = new_create.Sensors.distance
    distance = robot.getSensor(sensor1)
    robot.go(centimeters_per_second, 0)
    time.sleep((centimeters_per_second / centimeters) ** -1)
    robot.stop()
    print(distance)


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
