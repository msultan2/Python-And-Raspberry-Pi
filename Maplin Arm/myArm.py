import sys
import time
import os
import usb.core, usb.util

#Add current directory to system path
sys.path.append(os.getcwd())

#import the maplinrobot class
from maplinrobot import MaplinRobot

# Allocate the name 'RoboArm' to the USB device
RoboArm = usb.core.find(idVendor=0x1267, idProduct=0x0000)

# Check if the arm is detected and warn if not
if RoboArm is None:
    raise ValueError("Arm not found")

r = MaplinRobot()
r.MoveArm(t=2.0, cmd='base-anti-clockwise') # Rotates the base ant-clockwise
r.MoveArm(t=1.0, cmd='base-clockwise') # Rotates the base clockwise
r.MoveArm(t=1.0, cmd='shoulder-up') # Raises the shoulder
r.MoveArm(t=1.0, cmd='shoulder-down') # Lowers the shoulder
r.MoveArm(t=1.0, cmd='elbow-up') # Raises the elbow
r.MoveArm(t=1.0, cmd='elbow-down') # Lowers the elbow
r.MoveArm(t=1.0, cmd='wrist-up') # Raises the wrist
r.MoveArm(t=1.0, cmd='wrist-down') # Lowers the wrist
r.MoveArm(t=1.0, cmd='grip-open') # Opens the grip
r.MoveArm(t=1.0, cmd='grip-close') # Closes the grip
r.MoveArm(t=1.0, cmd='light-on') # Turns on the LED in the grip
r.MoveArm(t=1.0, cmd='light-off') # Turns the LED in the grip off
r.MoveArm(t=1.0, cmd='stop') # Stops all movement of the arm
