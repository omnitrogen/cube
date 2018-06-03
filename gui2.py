import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

import serial
import settings


if __name__ == "__main__":
    settings.init()
    # root = tk.Tk()
    # my_gui = RubiksSolverGui(settings.root)
    settings.root.mainloop()
    settings.ser.close()