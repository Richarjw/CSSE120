"""
The Python Capstone Project.

This file contains data SHARED by the other modules in this project.

CSSE 120 - Introduction to Software Development.
Team members: Joseph Jagiella, Ryan Coffman, Jack Richard (all of them).
"""
# TODO: Put the names of ALL team members in the above where indicated.

import m1
import m2
import m3
import m4

import tkinter
from tkinter import ttk

# ----------------------------------------------------------------------
# TODO: TEAM-PROGRAM this module so that it runs your entire program,
#       incorporating parts from m1 .. m4.
# ----------------------------------------------------------------------


class DataContainer():
    """ A container for the data shared across the application. """

    def __init__(self):
        """ Initializes instance variables (fields). """
        # Add     self.FOO = BLAH     here as needed.
        self.Robot = None
        self.list_of_waypoints = []
        self.speed = 0
        self.follow = True
        self.black = 0
        self.white = 4094
        self.list_of_notes = []

Robot = DataContainer()
s = ''

def main():
    """ Runs the MAIN PROGRAM. """
    print('----------------------------------------------')
    print('Integration Testing of the INTEGRATED PROGRAM:')
    print('----------------------------------------------')
    # Make a window.
    root = tkinter.Tk()
    # Put a Frame on it.
    frame = ttk.Frame(root, padding=(60, 60))

    main_frame = m1.my_frame(root, Robot, s)
    main_frame.grid()


#     m1.Song_Button(root, main_frame)
#
#     m1.movement(root, main_frame)
#
#     port_label = ttk.Label(main_frame, text=s)
#     port_label.grid()
#
#     m1.addWaypoints(root, main_frame)

    # Have a button for each feature that pulls up a separate GUI

    button1 = ttk.Button(main_frame, text='Music')
    button1.grid()
    button1['command'] = lambda: m1.Song_Button()

    button3 = ttk.Button(main_frame, text='Autonomous Movement')
    button3.grid()
    button3['command'] = lambda: m1.movement()

    button2 = ttk.Button(main_frame, text='Follow Waypoints')
    button2.grid()
    button2['command'] = lambda: m1.addWaypoints()

    # Add other 2 people's stuff
    m2.initial_frame(main_frame)
    m3.initial_frame(main_frame)

    # The rest of it is part of the frame.
    root.mainloop()
    try:  # Error catching
        Robot.Robot.shutdown()
    except AttributeError:
        pass



# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
