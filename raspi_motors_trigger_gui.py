from tkinter import *
import tkinter as tk
from tkinter import ttk
from time import sleep
import RPi.GPIO as GPIO

DIR = 20   # Direction GPIO Pin
STEP = 21  # Step GPIO Pin
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
SPR = 48   # Steps per Revolution (360 / 7.5)

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CW)

MODE = (14, 15, 18)   # Microstep Resolution GPIO Pins
GPIO.setup(MODE, GPIO.OUT)
RESOLUTION = {'Full': (0, 0, 0),
              'Half': (1, 0, 0),
              '1/4': (0, 1, 0),
              '1/8': (1, 1, 0),
              '1/16': (0, 0, 1),
              '1/32': (1, 0, 1)}
GPIO.output(MODE, RESOLUTION['1/32'])

step_count = SPR * 32
delay = .0208 / 32


class MotorTrigger:
    def __init__(self, master):
        self.master = master
        master.title("Motors trigger!")

        self.frame = tk.Frame(master)

        self.label = tk.Label(self.frame, text="Welcome to the Motors trigger!")
        self.label.grid(row=0, column=0)

        self.pic_button = tk.Button(self.frame, text="Motor 1", command=rotateMotor1())
        self.pic_button.grid(row=1, column=0)

        self.frame.pack(padx=20, pady=20)

    def rotateMotor1(self, step_count = 200):
        for loop in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)

            sleep(.5)
            GPIO.output(DIR, CCW)
            for loop in range(step_count):
                GPIO.output(STEP, GPIO.HIGH)
                sleep(delay)
                GPIO.output(STEP, GPIO.LOW)
                sleep(delay)

            GPIO.cleanup()


if __name__ == "__main__":
    root = tk.Tk()
    my_gui = MotorTrigger(root)
    root.mainloop()
