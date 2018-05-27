import os
import time
import serial


def init():
    global ser
    ser = serial.Serial('/dev/cu.usbmodem1421', timeout=.1)
    print("init done")
