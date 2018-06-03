import os
import time
import serial

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

import serial

from quatre_etapes import *


class RubiksSolverGui:
    def __init__(self, master):
        self.master = master
        master.title("Rubik's Cube Solver!")

        self.frame = tk.Frame(master)

        self.image = Image.open("cubeR2.gif")
        self.photo = ImageTk.PhotoImage(self.image)
        self.label = tk.Label(self.frame, image=self.photo)
        self.label.grid(row=0, column=0)

        self.label = tk.Label(self.frame, text="Welcome to the Rubik's Cube Solver!")
        self.label.grid(row=1, column=0, pady=(5, 5))

        self.pic_button = tk.Button(self.frame, text="Scan", command=self.solve)
        self.pic_button.grid(row=2, pady=(5, 5))

        self.frame.pack(padx=5, pady=5)

        self.frame2 = tk.Frame(master)
        self.solve_button = tk.Button(self.frame2, text="Solve", command=self.solve)
        self.solve_button.grid_forget()
        self.frame2.pack()

    def solve(self):
        cube = Cube(str())
        cube.resolution()
        print("solving")
        pass

def init():
    global ser
    ser = serial.Serial('/dev/ttyACM0', timeout=.1)
    global root
    root = tk.Tk()
    global my_gui
    my_gui = RubiksSolverGui(root)
    global incr
    incr = 0
    global images
    images = []
    global photos
    photos = []
    global texts
    texts = []
    global pos
    pos = {1: (0, 0, 1, 0), 2: (0, 1, 1, 1), 3: (2, 0, 3, 0), 4: (2, 1, 3, 1), 5: (4, 0, 5, 0), 6: (4, 1, 5, 1), 7: (6, 0, 7, 0), 8: (6, 1, 7, 1)}
    global vs
    vs = []
    print("init done")
