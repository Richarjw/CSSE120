"""
Changers change.

Authors: David Mutchler, Mark Hays, Michael Wollowski, Amanda Stouder,
         Chandan Rupakheti, Katie Dion, Claude Anderson, Delvin Defoe,
         Curt Clifton, Matt Boutell, Dave Fisher, their colleagues,
         and PUT YOUR NAME HERE.  October 2014.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg
import random


def main():
    """ Not used here, but could be used for informal testing. """
    pass


class Changer(object):
    """
    A Changer has one instance variable:
      -- shape:  Must be an rg._Shape
                   (Circle, Square, Ellipse, Rectangle, Text, etc).
                 The Simulator draws this shape at every frame refresh.
    A Changer has two methods:
      -- change: Can do whatever it wants (including nothing).
                   This method is called by the Simulator just before
                   each frame refresh.
                   NOTE: If this method hangs, the simulator will hang!
      -- better: Takes another Changer and returns whichever Changer
                   is "better" -- this Changer or the given one.
                   The Simulator tries to draw Changers so that the
                   better Changers are on top of the less good Changers.
    """
    def __init__(self, shape):
        """
        Saves the given shape as this Changer's shape.

        Precondition:
          :type shape: rg._Shape
        """
        # --------------------------------------------------------------
        # TODO: With your instructor, implement and test this method.
        # --------------------------------------------------------------

    def change(self):
        """
        Does nothing.  Subclasses may override this method to obtain
        more interesting behaviors.
        """

    def better(self, another_Changer):  # @UnusedVariable
        """
        Returns whichever Changer is "better" -- this Changer or the
        given Changer.  Subclasses must override this method.

        Precondistion:
          :type another_Changer: Changer
        """
        assert False, 'Subclasses must OVERRIDE this method.'


# ----------------------------------------------------------------------
# TODO: With your instructor, implement the following   Dud   class.
# ----------------------------------------------------------------------
class Dud(Changer):
    """
    A Changer whose shape is a black circle at the given point
    with radius 10.  It does nothing (just sits still).
    """

    def __init__(self, point):
        """
        Stores the   shape   as a black circle at the given point
        with radius 10.

        Precondition:
          :type point: rg.Point
        """

    def change(self):
        """ Does nothing (a Dud just sits still). """

    def better(self, another_Changer):  # @UnusedVariable
        """
        Returns the given Changer -- Duds are never better than other
        types of Changers (they are "duds", after all!).

        Precondition:
          :type another_Changer: Changer
        """


# ----------------------------------------------------------------------
# TODO: With your instructor, implement the following   Mover   class.
# ----------------------------------------------------------------------
class Mover(Changer):
    """
    A Changer with a velocity.  At each call to the  change  method,
    a Mover moves the distance specified by its velocity.
    Movers are better than Duds, but worse than all other Changers.
    """

    def __init__(self, shape, velocity_x=1, velocity_y=1):
        """
        Saves the given shape and velocity.

        Precondition:
          :type shape: rg._Shape
        """

    def change(self):
        """ Moves this Mover per its velocity. """

    def better(self, another_Changer):
        """
        Returns the given Changer unless that Changer is a Dud,
        in which case returns this Mover.
        """


# ----------------------------------------------------------------------
# TODO: Implement and test the classes below.
#       Add additional  Changer  classes if you wish!
#       Test each class as you implement it!
# ----------------------------------------------------------------------
class Randomizer(Changer):
    """
    A Changer that moves randomly: at each call to the  change  method,
    a Randomizer moves to a random point in a portion of the
    simulation's window.

    When it is constructed, a Randomizer takes arguments that specify
    the portion of the window in which it should move randomly.
    For example:
      -- One Randomizer might move randomly inside the upper-left
           quadrant of the window, i.e., inside the region of the window
           bounded by the points (0, 0) and (600, 400).
           [This assumes the default window size of 1200 x 800.]
      -- Another Randomizer might move inside the "center" part of the
           window, i.e, inside the region of the window bounded by
           the points (300, 200) and (900, 600).

    Your __init__ arguments can specify the region of the window
    in which the Randomizer should move in whatever way you choose.

    Randomizers are better than Duds and Movers, worse than all others.
    """


class Jiggler(Changer):
    """
    A Changer that "jiggles":  At each opportunity to change,
    it moves its shape a small random distance.

    The range from which the distances (in the x and y direction) are
    chosen should be specified by the arguments to the __init__ method.
    For example:
      -- One Jiggler might have a greater tendency to choose a downward
           jiggle than an upward jiggle (thus "drifting").
      -- Another Jiggler might have just as much a chance to drift
           up as down, and right as left, but with a big range
           (so "violent" jiggling), while:
      -- Yet another Jiggler might have just as much a chance to drift
           up as down, and right as left, but with a small range
           (so "gentle" jiggling).

    Your __init__ arguments can specify the magnitude ("violence")
    and drift (if any) of the jiggling in whatever want you choose.

    in which the Randomizer should move in whatever way you choose.

    Jigglers are better than Duds, Movers and Randomizers,
    worse than all others.
    """


class Follower(Changer):
    """
    A Changer that follows another Changer that it is given when it
    is constructed.  It follows after a delay that it is given.
    """


class Grower(Changer):
    """
    A Changer that grows (increases its radius) at a constant rate.
    Its shape must be a rg.Circle.
    It stops growing when it gets a radius that reaches a given maximum.
    """


class MoverGrower(Changer):
    """
    A Changer that combines the effects of a Mover and a Grower.
    """


class Exploder:
    """
    A Changer is like a MoverGrower, but when it reaches a certain
    radius, it "explodes":
      -- It changes its rg.Circle to be tiny (so almost invisible)
           and no longer moving.
      -- It constructs two new Exploders, with random initial properties,
           and adds them to the Simulation.
    """


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
