"""
Test 3, part of problem 3.

Authors: David Mutchler, Mark Hays, Michael Wollowski,
         Chandan Rupakheti, Matt Boutell, Dave Fisher,
         Claude Anderson, and Jack Richard.  November 2014.
"""  # TODO: PUT YOUR NAME IN THE ABOVE LINE.

# ----------------------------------------------------------------------
# TODO: Add code below (at the appropriate places)
#       to test your   Balloon   class as you implement it.
#       The   Balloon   class is in the separate file  balloon.py
#
# IMPORTANT:
#  1. Read the specification of the ENTIRE   Balloon   class BEFORE
#       writing any code.
#  2. Test each method AS YOU DEFINE IT (one by one).
# ----------------------------------------------------------------------

import problem3_balloon as balloon


def main():
    """ Tests the   Balloon  class """
    test_init()
    test_blow_air_into()
    test_puncture()
    test_let_air_out()
    test_owners_age()
    test_fuller_balloon()
    test_new_balloon()
    test_unpunctured_balloons()


def test_init():
    print('------------------------------------')
    print('Testing __init__:')

    child1 = balloon.Person(6, 40)
    adult1 = balloon.Person(28, 130)
    adult2 = balloon.Person(40, 170)

    balloon1 = balloon.Balloon(1.4, child1)
    balloon2 = balloon.Balloon(4.0, adult1)
    balloon3 = balloon.Balloon(1.5, adult2)
    balloon4 = balloon.Balloon(2.0, child1)

    print(balloon1.capacity, balloon1.owner, balloon1.currentVolume)
    print(balloon2.capacity, balloon2.owner, balloon2.currentVolume)
    print(balloon3.capacity, balloon3.owner, balloon3.currentVolume)
    print(balloon4.capacity, balloon4.owner, balloon4.currentVolume)


def test_blow_air_into():
    print('\n------------------------------------')
    print('Testing blow_air_into:')

    child1 = balloon.Person(6, 40)
    adult1 = balloon.Person(28, 130)
    adult2 = balloon.Person(40, 170)

    balloon1 = balloon.Balloon(1.4, child1)
    balloon2 = balloon.Balloon(4.0, adult1)
    balloon3 = balloon.Balloon(1.5, adult2)
    balloon4 = balloon.Balloon(2.0, child1)

    # Add code below here to continue this test:
    balloon1.blow_air_into(1)
    print(balloon1.currentVolume, balloon1.owner.is_happy)
    balloon2.blow_air_into(3)
    print(balloon2.currentVolume, balloon2.owner.is_happy)
    balloon3.blow_air_into(10)
    print(balloon3.currentVolume, balloon3.owner.is_happy)
    balloon4.blow_air_into(500)
    print(balloon4.currentVolume, balloon4.owner.is_happy)
def test_puncture():
    print('\n------------------------------------')
    print('Testing puncture:')

    child1 = balloon.Person(6, 40)
    adult1 = balloon.Person(28, 130)
    adult2 = balloon.Person(40, 170)

    balloon1 = balloon.Balloon(1.4, child1)
    balloon2 = balloon.Balloon(4.0, adult1)
    balloon3 = balloon.Balloon(1.5, adult2)
    balloon4 = balloon.Balloon(2.0, child1)

    # Add code below here to continue this test:
    balloon1.puncture()
    print(balloon1.popped, balloon1.currentVolume, balloon1.owner.is_happy)
    balloon2.puncture()
    print(balloon2.popped, balloon2.currentVolume, balloon2.owner.is_happy)
    print(balloon3.popped, balloon3.currentVolume, balloon3.owner.is_happy)
    print(balloon4.popped, balloon4.currentVolume, balloon4.owner.is_happy)

def test_let_air_out():
    print('\n------------------------------------')
    print('Testing let_air_out:')

    child1 = balloon.Person(6, 40)
    adult1 = balloon.Person(28, 130)
    adult2 = balloon.Person(40, 170)

    balloon1 = balloon.Balloon(1.4, child1)
    balloon2 = balloon.Balloon(4.0, adult1)
    balloon3 = balloon.Balloon(1.5, adult2)
    balloon4 = balloon.Balloon(2.0, child1)

    # Add code below here to continue this test:
    balloon1.blow_air_into(4)
    balloon1.let_air_out(1)
    balloon2.blow_air_into(4)
    balloon2.let_air_out(10)
    balloon3.blow_air_into(1)
    balloon3.let_air_out(9)
    balloon4.let_air_out(1)
    print(balloon1.currentVolume)
    print(balloon2.currentVolume)
    print(balloon3.currentVolume)
    print(balloon4.currentVolume)
def test_owners_age():
    print('\n------------------------------------')
    print('Testing owners_age:')

    child1 = balloon.Person(6, 40)
    adult1 = balloon.Person(28, 130)
    adult2 = balloon.Person(40, 170)

    balloon1 = balloon.Balloon(1.4, child1)
    balloon2 = balloon.Balloon(4.0, adult1)
    balloon3 = balloon.Balloon(1.5, adult2)
    balloon4 = balloon.Balloon(2.0, child1)

    # Add code below here to continue this test:
    print(balloon1.owners_age())
    print(balloon2.owners_age())
    print(balloon3.owners_age())
    print(balloon4.owners_age())

def test_fuller_balloon():
    print('\n------------------------------------')
    print('Testing fuller_balloon:')

    child1 = balloon.Person(6, 40)
    adult1 = balloon.Person(28, 130)
    adult2 = balloon.Person(40, 170)

    balloon1 = balloon.Balloon(1.4, child1)
    balloon2 = balloon.Balloon(4.0, adult1)
    balloon3 = balloon.Balloon(1.5, adult2)
    balloon4 = balloon.Balloon(2.0, child1)

    # Add code below here to continue this test:
    balloon1.currentVolume = 0.5
    balloon2.currentVolume = 0.1
    balloon3.currentVolume = 0.5
    balloon4.currentVolume = 0.8
    print(balloon1.fuller_balloon(balloon2))
    print(balloon1.fuller_balloon(balloon3))
    print(balloon4.fuller_balloon(balloon2))
    print(balloon2.fuller_balloon(balloon1))


def test_new_balloon():
    print('\n------------------------------------')
    print('Testing new_balloon:')

    child1 = balloon.Person(6, 40)
    adult1 = balloon.Person(28, 130)
    adult2 = balloon.Person(40, 170)

    balloon1 = balloon.Balloon(1.4, child1)
    balloon2 = balloon.Balloon(4.0, adult1)
    balloon3 = balloon.Balloon(1.5, adult2)
    balloon4 = balloon.Balloon(2.0, child1)

    # Add code below here to continue this test:
    print(balloon1.new_balloon())
    print(balloon2.new_balloon())
    print(balloon3.new_balloon())
    print(balloon4.new_balloon())

def test_unpunctured_balloons():
    print('\n------------------------------------')
    print('Testing unpunctured_balloons:')

    child1 = balloon.Person(6, 40)
    adult1 = balloon.Person(28, 130)
    adult2 = balloon.Person(40, 170)

    balloon1 = balloon.Balloon(1.4, child1)
    balloon2 = balloon.Balloon(4.0, adult1)
    balloon3 = balloon.Balloon(1.5, adult2)
    balloon4 = balloon.Balloon(2.0, child1)

    # Add code below here to continue this test:
    balloon2.puncture()
    list = [balloon2, balloon3, balloon4]
    print(balloon1.unpunctured_balloons(list))
    balloon3.puncture()
    print(balloon2.unpunctured_balloons(list))


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
