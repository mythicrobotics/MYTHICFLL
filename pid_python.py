# This module provides block functions to set PID values.
# Just add this file to Pybricks Code.
# Then you can import the functions into your block programs.


from pybricks.tools import run_task

async def awaitable():
    return None

def set_pid(control, *values):
    print("Original", control.pid())
    control.pid(*values)
    print("New     ", control.pid())

    if run_task():
        return awaitable()

def motor_pid(motor, *values):
    return set_pid(motor.control, *values)

def distance_pid(drivebase, *values):
    return set_pid(drivebase.distance_control, *values)

def heading_pid(drivebase, *values):
    return set_pid(drivebase.heading_control, *values)

