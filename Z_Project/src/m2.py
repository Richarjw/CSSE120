"""
The Python Capstone Project.

CSSE 120 - Introduction to Software Development.
Team members: Ryan Coffman, Joe Jagiella, Jack Richard (all of them).

The primary author of this module is: Ryan Coffman.
"""
# DONE: Put the names of ALL team members in the above where indicated.
#       Put YOUR NAME in the above where indicated.

import m0
import m1
import m3
import m4
import time
import tkinter
from tkinter import ttk
import new_create
from numbers import Integral


# class Data_container(): #Integrated into m0
#     def __init__(self):
#         self.speed = 0
#         self.follow = False
#
# speed = Data_container()

def main():
    """
    Tests functions in this module.
    Intended to be used internally by the primary author of this module.
    """
    print('-------------------------------')
    print('Testing functions in module m2:')
    print('-------------------------------')

def initial_frame(main_frame):
#     root = tkinter.Tk()

#     main_frame = ttk.Frame(root, padding=(30, 10), relief='raised')
#     main_frame.grid()

    hours_button = ttk.Button(main_frame, text='Hours')
    hours_button.grid()

    tele_button = ttk.Button(main_frame, text='Be tele-operated')
    tele_button.grid()

    follow_button = ttk.Button(main_frame, text='follow')
    follow_button.grid()

    hours_button['command'] = lambda: run_my_frame()
    tele_button['command'] = lambda: run_be_tele_operated()
    follow_button['command'] = lambda: run_follow_line()

    # root.mainloop()

def run_my_frame():

    my_frame()

def my_frame():
    """
    Constructs and returns a Frame (on the given root window)
    that contains this module's widgets.
    Also sets up callbacks for this module's widgets.

    Preconditions:
      :type root: tkinter.Tk
      :type dc: m0.DataContainer
    """
    root = tkinter.Tk()

    main_frame = ttk.Frame(root, padding=(30, 10), relief='raised')
    main_frame.grid()

    joe_button = ttk.Button(main_frame, text='Joe')
    joe_button.grid()

    ryan_button = ttk.Button(main_frame, text='Ryan')
    ryan_button.grid()

    jack_button = ttk.Button(main_frame, text='Jack')
    jack_button.grid()

    hours_label = ttk.Label(main_frame, text='Press a button to see the number of hours')
    hours_label.grid()

    joe_button['command'] = lambda: hours_worked('hours-1.txt', hours_label, 'Joe')
    ryan_button['command'] = lambda: hours_worked('hours-2.txt', hours_label, 'Ryan')
    jack_button['command'] = lambda:  hours_worked('hours-3.txt', hours_label, 'Jack')

    root.mainloop()

def hours_worked(file_name, label, name):
    """
    formats the test string to say how many hours each person has worked
    """
    number_of_hours = 0
    with open(file_name) as f:
        line = f.readline()
        while line != "":
            number_of_hours += float(line)
            line = f.readline()
        f.close()
    format_string = name + ' has worked ' + str(number_of_hours) + ' hours'
    label['text'] = format_string


def run_be_tele_operated():

    be_tele_operated()

def change_speed(set_speed):
    m0.Robot.speed = set_speed


def be_tele_operated():

    root = tkinter.Tk()

#     port = 'sim'
#     robot = new_create.Create(port)

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()

    speed_label = ttk.Label(main_frame, text='Enter the speed:')
    speed_label.grid()

    speed_entry = ttk.Entry(main_frame, width=10)
    speed_entry.grid()

    set_speed_button = ttk.Button(main_frame, text='Set speed')
    set_speed_button.grid()

    w_label = ttk.Label(main_frame, text='w: move forward')
    a_label = ttk.Label(main_frame, text='a: spin left')
    s_label = ttk.Label(main_frame, text='s: move backward')
    d_label = ttk.Label(main_frame, text='d: spin right')
    q_label = ttk.Label(main_frame, text='q: move forward and left')
    e_label = ttk.Label(main_frame, text='e: move forward and right')
    z_label = ttk.Label(main_frame, text='z: move backward and right')
    c_label = ttk.Label(main_frame, text='c: move backward and left')
    w_label.grid()
    a_label.grid()
    s_label.grid()
    d_label.grid()
    q_label.grid()
    e_label.grid()
    z_label.grid()
    c_label.grid()

    set_speed_button['command'] = lambda: change_speed(int(speed_entry.get()))

    root.bind_all('<KeyPress>', lambda event: pressed_a_key(event, m0.Robot.Robot, m0.Robot.speed))
    root.bind_all('<KeyRelease>', lambda event: released_a_key(m0.Robot.Robot))

    root.mainloop()

def pressed_a_key(event, robot, speed=30):

    if event.keysym == 'w':
        robot.driveDirect(speed, speed)
    if event.keysym == 'a':
        robot.driveDirect(-speed, speed)
    if event.keysym == 's':
        robot.driveDirect(-speed, -speed)
    if event.keysym == 'd':
        robot.driveDirect(speed, -speed)
    if event.keysym == 'e':
        robot.driveDirect(speed, speed // 2)
    if event.keysym == 'q':
        robot.driveDirect(speed // 2, speed)
    if event.keysym == 'z':
        robot.driveDirect(-speed // 2, -speed)
    if event.keysym == 'c':
        robot.driveDirect(-speed, -speed // 2)


def released_a_key(robot):

    robot.stop()

def run_follow_line():

    follow_line()

def follow_stop():

    m0.Robot.follow = False

def follow_line():

    root = tkinter.Tk()

#     port = 'sim'
#     robot = new_create.Create(port)

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()

    follow_button = ttk.Button(main_frame, text='Follow')
    follow_button.grid()

    stop_button = ttk.Button(main_frame, text='stop')
    stop_button.grid()

    read_black_button = ttk.Button(main_frame, text='Read Black')
    read_black_button.grid()

    read_white_button = ttk.Button(main_frame, text='Read White')
    read_white_button.grid()

    follow_button['command'] = lambda: start_follow(m0.Robot.Robot, root)
    stop_button['command'] = lambda: follow_stop()
    root.bind_all('<KeyPress>', lambda event: pressed_a_key(event, m0.Robot.Robot))
    root.bind_all('<KeyRelease>', lambda event: released_a_key(m0.Robot.Robot))
    read_black_button['command'] = lambda: read_black(m0.Robot.Robot)
    read_white_button['command'] = lambda: read_white(m0.Robot.Robot)

    root.mainloop()


def read_black(robot):
    left_signal = robot.getSensor('CLIFF_FRONT_LEFT_SIGNAL')
    right_signal = robot.getSensor('CLIFF_FRONT_RIGHT_SIGNAL')
    m0.Robot.black = (left_signal + right_signal) / 2
    print(m0.Robot.black)

def read_white(robot):
    left_signal = robot.getSensor('CLIFF_FRONT_LEFT_SIGNAL')
    right_signal = robot.getSensor('CLIFF_FRONT_RIGHT_SIGNAL')
    m0.Robot.white = (left_signal + right_signal) / 2
    print(m0.Robot.white)


def start_follow(robot, root):

#     stopper.follow = False
#     left_sensor = new_create.Sensors.cliff_front_left_signal
#     right_sensor = new_create.Sensors.cliff_front_right_signal
#     while True:
#         left_read = robot.getSensor(left_sensor)
#         right_read = robot.getSensor(right_sensor)
#         if stopper.follow:
#             break
#         if (left_read > 1000) and (right_read > 1000):
#             robot.driveDirect(5, 5)
#             time.sleep(0.3)
#             robot.stop()
#
#         if (left_read < 1000) and (right_read > 1000):
#             robot.driveDirect(-5, 5)
#             time.sleep(0.3)
#             robot.stop()
#
#         if (left_read > 1000) and (right_read < 1000):
#             robot.driveDirect(5, -5)
#             time.sleep(0.3)
#             robot.stop()
#         root.update()
#
#     robot.stop()

    left_error_previous = 0
    right_error_previous = 0
    expected_reading = (m0.Robot.black + m0.Robot.white) / 2
    kp = 0.025
    ki = 0.0
    kd = 0.005
    m0.Robot.follow = True

    while m0.Robot.follow:
        left_sensor = robot.getSensor('CLIFF_FRONT_LEFT_SIGNAL')
        right_sensor = robot.getSensor('CLIFF_FRONT_RIGHT_SIGNAL')

        left_error = left_sensor - expected_reading
        right_error = right_sensor - expected_reading

        left_derivative = abs(left_error - left_error_previous)
        right_derivative = abs(right_error - right_error_previous)

        left_integral = left_error_previous + left_error
        right_integral = right_error_previous + right_error

        left_wheel_speed = kp * left_error + kd * left_derivative + ki * left_integral + 5
        right_wheel_speed = kp * right_error + kd * right_derivative + ki * right_integral + 5

        if left_wheel_speed < 0:
            left_wheel_speed = 2
        if right_wheel_speed < 0:
            right_wheel_speed = 2

        robot.driveDirect(left_wheel_speed, right_wheel_speed)

        left_error_previous = left_error
        right_error_previous = right_error

        root.update()

    robot.stop()




# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
