"""
The Python Capstone Project.

CSSE 120 - Introduction to Software Development.
Team members: Joseph Jagiella, Ryan Coffman, Jack Richard (all of them).

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
import time
import math
s = ''

class DataContainer():
    def __init__(self):
        self.Robot = None
        self.list_of_waypoints = []

Robot = DataContainer()
# robot = Robot.Robot # This does not work
def main():
    """
    Tests functions in this module.
    Intended to be used internally by the primary author of this module.
    """
    print('-------------------------------')
    print('Testing functions in module m1:')
    print('-------------------------------')
    Robot.Robot = None
    # Make a window.
    root = tkinter.Tk()
    # Put a Frame on it.
    main_frame = my_frame(root, m0.Robot, s)
    main_frame.grid()

    # The rest of it is part of the frame.
    root.mainloop()
    Robot.Robot.shutdown()

def my_frame(root, dc, s):
    """
    Constructs and returns a Frame (on the given root window)
    that contains this module's widgets.
    Also sets up callbacks for this module's widgets.

    Preconditions:
      :type root: tkinter.Tk
      :type dc: m0.DataContainer
    """
    frame = ttk.Frame(root, padding=(60, 60))
    # Add a Label and an Entry.
    label = ttk.Label(frame, text='Enter the port:')
    label.grid(row=1, column=0)

    entry = ttk.Entry(frame, width=8)
    entry.grid(row=1, column=1)

    # Put a Button on the frame.
    # Make your Button do something with the Label and Entry.
    button2 = ttk.Button(frame, text='Connect to the Robot')
    button2.grid()
    button2['command'] = lambda: try_connect(entry.get())

    button3 = ttk.Button(frame, text='Disconnect from the Robot')
    button3.grid()
    button3['command'] = lambda: Disconnect()

    # Song_Button(root,frame)

    # movement(root, frame)

    # port_label = ttk.Label(frame, text=s)
    # port_label.grid()

    # addWaypoints(root, frame)

    return frame
def try_connect(s):
    # print(s)
    if type(s) == str and s == 'sim':
        port = s
        m0.Robot.Robot = new_create.Create(port)
    elif type(s) == str and s != 'sim':
        try:
            port = int(s)
            m0.Robot.Robot = new_create.Create(port)
        except ValueError:
            print('Bad Port')
            port = None
    else:
        print('Bad Port')
        port = None


def Disconnect():
    m0.Robot.Robot.shutdown()
    print('Disconnected')

def Song_Button():
    root = tkinter.Tk()
    frame = ttk.Frame(root, padding=(60, 60))
    frame.grid()

    button4 = ttk.Button(frame, text='Play Sample Song')
    button4.grid()
    button4['command'] = lambda: Song()

    label3 = ttk.Label(frame, text='Add a note (30-127, duration)')
    label3.grid()
    label4 = ttk.Label(frame, text='30 is rest, duration is in 1/64 of a second')
    label4.grid()

    label5 = ttk.Label(frame, text='Pitch (30-127):')
    label5.grid()
    entry3 = ttk.Entry(frame, width=8)
    entry3.grid()

    label5 = ttk.Label(frame, text='Duration (1/64 seconds):')
    label5.grid()
    entry4 = ttk.Entry(frame, width=8)
    entry4.grid()

    label6 = ttk.Label(frame, text='No notes added')

    button = ttk.Button(frame, text='Add note')
    button.grid()
    button['command'] = lambda: add_note(entry3.get(), entry4.get(), label6)

    label6.grid()

    button3 = ttk.Button(frame, text='Delete latest note')
    button3.grid()
    button3['command'] = lambda: delete_note(label6)

    button2 = ttk.Button(frame, text='Play Notes')
    button2.grid()
    button2['command'] = lambda: Play_Notes()

    root.mainloop()

def delete_note(label):
    list = m0.Robot.list_of_notes
    label['text'] = 'Note (' + str(list[len(list) - 1][0]) + ', ' + str(list[len(list) - 1][1]) + ') removed'
    list.pop(len(list) - 1)


def add_note(pitch, duration, label):
    m0.Robot.list_of_notes.append([pitch, duration])
    label['text'] = 'Note (' + str(pitch) + ', ' + str(duration) + ') added'

def Play_Notes():  # Plays the notes in the list list_of_notes
    list = m0.Robot.list_of_notes
    for k in range(len(list)):
        m0.Robot.Robot.playNote(int(list[k][0]), int(list[k][1]))
        time.sleep(int(list[k][1]) / 64)
        time.sleep(0.1)


def Song():
# Flying a helicopter is easy, just grab the controls and go BUM BA DA BUM BUM
# We may want to convert this to a MIDI file and read it, but this was easier
    o = 12  # Octave modifier. Goes in increments of 12 (or -12)
    m0.Robot.Robot.playNote(47 + o, 10)
    time.sleep(.3)
    m0.Robot.Robot.playNote(42 + o, 7)
    time.sleep(.15)
    m0.Robot.Robot.playNote(47 + o, 7)
    time.sleep(.15)
    m0.Robot.Robot.playNote(50 + o, 30)
    time.sleep(.6)
    m0.Robot.Robot.playNote(47 + o, 30)
    time.sleep(.6)
    #
    m0.Robot.Robot.playNote(50 + o, 10)
    time.sleep(.3)
    m0.Robot.Robot.playNote(47 + o, 7)
    time.sleep(.15)
    m0.Robot.Robot.playNote(50 + o, 7)
    time.sleep(.15)
    m0.Robot.Robot.playNote(54 + o, 30)
    time.sleep(.6)
    m0.Robot.Robot.playNote(50 + o, 30)
    time.sleep(.6)
    #
    m0.Robot.Robot.playNote(54 + o, 10)
    time.sleep(.3)
    m0.Robot.Robot.playNote(50 + o, 7)
    time.sleep(.15)
    m0.Robot.Robot.playNote(54 + o, 7)
    time.sleep(.15)
    m0.Robot.Robot.playNote(57 + o, 30)
    time.sleep(.6)
    m0.Robot.Robot.playNote(45 + o, 30)
    time.sleep(.6)
    #
    m0.Robot.Robot.playNote(50 + o, 10)
    time.sleep(.3)
    m0.Robot.Robot.playNote(45 + o, 7)
    time.sleep(.15)
    m0.Robot.Robot.playNote(50 + o, 7)
    time.sleep(.15)
    m0.Robot.Robot.playNote(54 + o, 50)
    time.sleep(1)

def movement():
    root = tkinter.Tk()
    frame = ttk.Frame(root, padding=(60, 60))
    frame.grid()

    label1 = ttk.Label(frame, text='Direction:')
    label1.grid()

    entry1 = ttk.Entry(frame, width=8)
    entry1.grid()

    label2 = ttk.Label(frame, text='Distance (cm):')
    label2.grid()

    entry2 = ttk.Entry(frame, width=8)
    entry2.grid()

    label3 = ttk.Label(frame, text='Speed (0,50)cm/s:')
    label3.grid()

    entry3 = ttk.Entry(frame, width=8)
    entry3.grid()

    button = ttk.Button(frame, text='Go')
    button.grid()
    button['command'] = lambda: Go(entry1.get(), entry2.get(), entry3.get(), m0.Robot.Robot)

    root.mainloop()

def Go(direction, distance, speed, robot):
    # Move autonomously
    speed = float(speed)
    distance = float(distance)
    if str(direction) == 'forward':
        robot.driveDirect(speed, speed)
        seconds = distance / speed
        time.sleep(seconds)
        robot.stop()
    if str(direction) == 'backward':
        robot.driveDirect(-speed, -speed)
        seconds = distance / speed
        time.sleep(seconds)
        robot.stop()
    if str(direction) == 'spin right':
        robot.driveDirect(speed, -speed)
        seconds = distance / speed
        time.sleep(seconds)
        robot.stop()
    if str(direction) == 'spin left':
        robot.driveDirect(-speed, speed)
        seconds = distance / speed
        time.sleep(seconds)
        robot.stop()

def addWaypoints():
    # Move through a series of specified waypoints
    root = tkinter.Tk()
    frame = ttk.Frame(root, padding=(60, 60))
    frame.grid()

    label1 = ttk.Label(frame, text='X-coordinate from Previous Waypoint (cm):')
    label1.grid()

    entry1 = ttk.Entry(frame, width=8)
    entry1.grid()

    label2 = ttk.Label(frame, text='Y-coordinate from Previous Waypoint (cm):')
    label2.grid()

    entry2 = ttk.Entry(frame, width=8)
    entry2.grid()

    label3 = ttk.Label(frame, text='No waypoints added')

    button1 = ttk.Button(frame, text='Add Waypoint')
    button1.grid()
    button1['command'] = lambda: addWaypoint(entry1.get(), entry2.get(), label3)

    button3 = ttk.Button(frame, text='Delete Latest Waypoint')
    button3.grid()
    button3['command'] = lambda: removeWaypoint(label3)

    button2 = ttk.Button(frame, text='Follow Waypoints')
    button2.grid()
    button2['command'] = lambda: followWaypoints(root, frame, m0.Robot.list_of_waypoints)


    label3.grid()

    root.mainloop()

def addWaypoint(x, y, label):
    m0.Robot.list_of_waypoints.append([x, y])
    label['text'] = 'Waypoint added (' + str(x) + ', ' + str(y) + ')'

def removeWaypoint(label):
    num = len(m0.Robot.list_of_waypoints) - 1
    label['text'] = 'Waypoint (' + str(m0.Robot.list_of_waypoints[num][0]) + ', ' + str(m0.Robot.list_of_waypoints[num][1]) + ')' ' removed.'
    m0.Robot.list_of_waypoints.pop(num)

def followWaypoints(root, frame, list):
    velocity = 20
    for k in range(len(list)):
        x = int(list[k][0])
        y = int(list[k][1])
        # Set angle needed to turn
        if x > 0 and y > 0:
            theta = math.pi / 2 - math.atan(y / x)
        elif x < 0 and y > 0:
            theta = math.pi / 2 - math.atan(y / x)
        elif x < 0 and y < 0:
            theta = math.pi - math.atan(y / x)
        elif x > 0 and y < 0:
            theta = math.pi - math.atan(y / x)
        elif x == 0 and y == 0:
            theta = 0
        elif x == 0 and y > 0:
            theta = 0
        elif x == 0 and y < 0:
            theta = math.pi
        elif x < 0 and y == 0:
            theta = math.pi / 2
        elif x > 0 and y == 0:
            theta = math.pi / 2
        distance = math.sqrt(x ** 2 + y ** 2)
        radius = 13.365  # 12.065 for real robot
        arclength = radius * theta
        # Turn
        if x > 0 and y > 0:
            m0.Robot.Robot.driveDirect(velocity, -velocity)
            time.sleep((arclength / velocity))
            m0.Robot.Robot.stop()
        elif x < 0 and y > 0:
            m0.Robot.Robot.driveDirect(-velocity, velocity)
            time.sleep((arclength / velocity))
            m0.Robot.Robot.stop()
        elif x < 0 and y < 0:
            m0.Robot.Robot.driveDirect(-velocity, velocity)
            time.sleep((arclength / velocity))
            m0.Robot.Robot.stop()
        elif x > 0 and y < 0:
            m0.Robot.Robot.driveDirect(velocity, -velocity)
            time.sleep((arclength / velocity))
            m0.Robot.Robot.stop()
        elif x == 0 and y == 0:
            pass
        elif x == 0 and y > 0:
            pass
        elif x == 0 and y < 0:
            m0.Robot.Robot.driveDirect(velocity, -velocity)
            time.sleep((arclength / velocity))
            m0.Robot.Robot.stop()
        elif x < 0 and y == 0:
            m0.Robot.Robot.driveDirect(-velocity, velocity)
            time.sleep((arclength / velocity))
            m0.Robot.Robot.stop()
        elif x > 0 and y == 0:
            m0.Robot.Robot.driveDirect(velocity, -velocity)
            time.sleep((arclength / velocity))
            m0.Robot.Robot.stop()
#         if theta > math.pi / 2:  # Doesn't work for (x<0 and y>0), check math
#             Robot.Robot.driveDirect(-velocity, velocity)
#             time.sleep((arclength / velocity))
#             Robot.Robot.stop()
#         elif x > 0 and y > 0:  # Doublecheck
#             Robot.Robot.driveDirect(velocity, -velocity)
#             time.sleep((arclength / velocity))
#             Robot.Robot.stop()
        # Drive forward the specified distance
        m0.Robot.Robot.driveDirect(velocity, velocity)
        time.sleep(distance / velocity)
        m0.Robot.Robot.stop()







# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
