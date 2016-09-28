"""
The  **** PRACTICE **** Python Capstone Project.

CSSE 120 - Introduction to Software Development.
Team members: Joseph Jagiella, Ryan Coffman, Jack Richard.

The primary author of this module is: Joseph Jagiella.
"""
# TODO: Put the names of ALL team members in the above where indicated.
#       Put YOUR NAME in the above where indicated.

import m0
import m2
import m3
import m4

import tkinter
from tkinter import ttk
import new_create

# ----------------------------------------------------------------------
# TODO: Do the following in STAGES, using ITERATIVE ENHANCEMENT.
#       That means that for each stage, you implement it, TEST it,
#       COMMIT your work WITH A SHORT, REASONABLE MESSAGE,
#       and then and only then continue to the next stage.
#
# Your ultimate goal for your part of this Practice Project is to have
# correctly function buttons:
#   -- Connect using Simulator
#   -- Connect using Port
#   -- Disconnect
# plus an:
#   -- Entry box
# in which the user enters the port to use for connecting to a robot.
#
# Use the following ITERATIVE ENHANCEMENT PLAN, where each stage
# augments the preceding stages:
#
#   Stage 1: Frame appears with the three buttons and Entry box on it.
#
#   Stage 2: Connect_using_Simulator button prints a message, as a stub.
#              -- A STUB is placeholder code that lets you do some
#                 testing even before you have finished the real code.
#
#   Stage 3: Connect_using_Simulator button works correctly.
#              That is, pressing it connects to (i.e. constructs)
#              a robot in the simulator (which must already be open).
#
#   Stage 4: Connect_using_Port button prints whatever the user most
#               recently entered into the Entry box, as a stub.
#
#   Stage 5: Connect_using_Port button works correctly.
#              That is, pressing it connects to (i.e. constructs)
#              a robot using the port specified in the Entry box.
#              (There must already be the usual Bluetooth connection.)
#
#   Stage 6: The Disconnect button works correctly,
#              no matter which Connect button was used.
#
# Do ALL your work in THIS file.  Do not touch m0!
# You will INTEGRATE work in the NEXT session, using m0 to do so.
# ----------------------------------------------------------------------


class DataContainer1():
    """ A container for the data shared across the application. """

    def __init__(self, robot, port):
        """ Initializes instance variables (fields). """
        # Add     self.FOO = BLAH     here as needed.
        self.robot = robot
        self.port = port


def main():
    """
    Tests functions in this module.
    Intended to be used internally by the primary author of this module.
    """
    print('-------------------------------')
    print('Testing functions in module m1:')
    print('-------------------------------')
    # Make a window.
    root = tkinter.Tk()
    # Put a Frame on it.
    main_frame = my_frame(root)
    main_frame.grid()

    # The rest of it is part of the frame.
    root.mainloop()



def my_frame(root):
    """
    Constructs and returns a Frame (on the given root window)
    that contains this module's widgets.
    Also sets up callbacks for this module's widgets.

    Preconditions:
      :type root: tkinter.Tk
      :type data: DataContainer1
    """
    frame = ttk.Frame(root, padding=(60, 60))
    # Put a Button on the frame.
    button = ttk.Button(frame,
                                text='Press me!')
    button.grid()
    # Make your Button do something simple.
    button['command'] = lambda: print('Hello World!')
    # Add a Label and an Entry.
    label = ttk.Label(frame, text='Enter a string:')
    label.grid(row=1, column=0)

    entry = ttk.Entry(frame, width=8)
    entry.grid(row=1, column=1)

    # Make your Button do something with the Label and Entry.
    button2 = ttk.Button(frame, text='I entered a string')
    button2.grid()
    button2['command'] = lambda: print(entry.get())
    return frame

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
