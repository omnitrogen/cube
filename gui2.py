from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import time

import serial
from goprocam import GoProCamera
from goprocam import constants

import settings

from quatre_etapes import *


class RubiksSolverGui:
    def __init__(self, master):
        self.master = master
        master.title("Rubik's Cube Solver!")

        self.frame = tk.Frame(master)

        self.image = Image.open("cubeR.gif")
        self.photo = ImageTk.PhotoImage(self.image)
        self.label = tk.Label(self.frame, image=self.photo)
        self.label.image = self.photo   # keep a reference!
        self.label.grid(row=0, column=0)

        self.label = tk.Label(self.frame, text="Welcome to the Rubik's Cube Solver!")
        self.label.grid(row=1, column=0, pady=(20, 10))

        self.pic_button = tk.Button(self.frame, text="Solve", command=self.solve)
        self.pic_button.grid(row=2, pady=(10, 10))

        self.frame.pack(padx=20, pady=20)


    def solve(self):
        cube = Cube(str())
        cube.resolution()
        print("solving")
        pass


if __name__ == "__main__":
    #ser = serial.Serial('/dev/cu.usbmodem1421', timeout=.1)
    #pic = Camera()
    settings.init()
    root = tk.Tk()
    my_gui = RubiksSolverGui(root)
    root.mainloop()
    settings.ser.close()