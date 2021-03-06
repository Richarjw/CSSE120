"""
Practice Test 3, problem 4 (Elevator class).

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Jack Richard.  October 2014.
"""  # TODO: PUT YOUR NAME IN THE ABOVE LINE.


# ----------------------------------------------------------------------
# TODO: Implement the Elevator class below
#       (i.e., replace each "pass" by relevant code).
#       Test your methods by using the  problem4_test_Elevator  module.
#
# IMPORTANT:
#  1. Read the specification of the ENTIRE Elevator class BEFORE
#       writing any code.
#  2. Test each method AS YOU DEFINE IT (one by one).
# ----------------------------------------------------------------------


def main():
    """ Not used here, but could be used for informal testing. """
    # Put your tests in the   problem4_test_Elevator  module, NOT here.
    pass


# ----------------------------------------------------------------------
# USE this Person class in implementing the Elevator class below.
# ----------------------------------------------------------------------
class Person(object):
    """
    Simulates a person with an age (in years) and weight (in pounds).
    """

    def __init__(self, age, weight):
        """ Stores the Person's age and weight. """
        self.age = age
        self.weight = weight

    def __repr__(self):
        """ Returns a string representation of this Person. """
        return 'Person({}, {})'.format(self.age, self.weight)


class Elevator():
    """
    Simulates an Elevator that allows Person objects
    to enter and exit it.
    """

    def __init__(self, capacity):
        """
        This Elevator starts with the given capacity (in pounds).
        This Elevator starts with no people in it.
        """
        self.capacity = capacity
        self.people = 0
        self.listPeople = []
        self.pounds = 0

    def all_people_enter(self, people):
        """
        Simulates all the people in the given list of Person objects
        entering this Elevator, even if doing so would exceed the
        capacity of this Elevator.

        Precondition: the given argument is a list of Person objects.
        """
        for k in range(len(people)):
            self.people = self.people + 1
            self.listPeople.append(people[k])

    def last_people_exit(self, n):
        """
        Simulates the last  n  people who entered this Elevator
        now leaving it.

        Precondition:  n is a nonnegative integer that does not exceed
          the number of people currently in this Elevator.
        """
        for k in range(n):
            self.listPeople.remove(self.listPeople[len(self.listPeople) - (k + 1)])
            self.people = self.people - 1

    def remaining_capacity(self):
        """
        Returns the number of additional pounds that this Elevator
        can hold without exceeding its capacity.
        Note that if this elevator already exceeds its capacity,
        this will return a negative number.

        For example, if this Elevator has capacity 2000 and holds people
        with weights 150, 200, 150, then this method returns 1500.
        But if its capacity were 400, then this method returns -100.
        """
        for k in range(len(self.listPeople)):
            self.pounds = self.pounds + self.listPeople[k].weight
        return self.capacity - self.pounds
    def capacity_exceeded(self):
        """
        Returns True if the capacity of this Elevator has been exceeded,
        else returns False.
        """
        if self.capacity < self.pounds:
            return True
        else:
            return False

    def oldest_person(self):
        """
        Returns the oldest Person in this Elevator,
        but returns None if there are no people in this Elevator.
        """
        oldest = None
        for k in range(len(self.listPeople)):
            if self.listPeople[k].age > oldest:
                oldest = self.listPoeple[k]
        return oldest


    def elevator_with_oldest(self, elevators):
        """
        Given a list of Elevator objects, returns the Elevator that
        holds the oldest person.  Includes this Elevator in its
        calcuation (so that if this Elevator holds the oldest person,
        it returns this Elevator).

        Preconditions: the argument is a NON-EMPTY list of Elevator
        objects and each Elevator, including this one, holds at least person.

        Note to student: If you want to try a harder problem,
        don't make the assumptions of the Preconditions.
        """


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
