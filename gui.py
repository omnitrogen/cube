from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import time


class MyButton(Button):
    def __init__(self, master):
        Button.__init__(self, master)
        self.ishide = False
        self['text'] = 'OK'
 
    def hide(self):
        if not self.ishide:
            self.pack_forget()
            self.ishide = True
            bt['text'] = "display OK"
        else:
            self.pack()
            self.ishide = False
            bt['text'] = "hide OK"

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

        self.pic_button = tk.Button(self.frame, text="Scan the cube", command=self.take_photo)
        self.pic_button.grid(row=2, pady=(10, 10))

        self.loading = tk.Label(self.frame, text="----------")
        self.loading.grid(row=3, pady=(10, 10))

        self.solve_button = tk.Button(self.frame, text="Solve the cube", command=self.solve_cube)
        self.solve_button.grid_forget()

        self.canvas = tk.Canvas(self.frame, width = 400, height = 200, borderwidth=0, background='green', highlightthickness=0)
        self.canvas.grid(row=4, pady=(10, 10))

        #self.close_button = tk.Button(self.frame, text="Close", command=master.quit)
        #self.close_button.grid(row=5, pady=(10, 20))

        self.frame.pack(padx=20, pady=20)

    def solve_cube(self):
        print("solving done")
        pass

    def take_photo(self):
        #take_pic_with_gopro
        MAX = 30
        progress_var = DoubleVar()
        self.progress_bar_label = Label(self.frame, text="scanning...")
        self.progress_bar_label.grid(row=5)
        self.progressbar = ttk.Progressbar(root, variable=progress_var, maximum=MAX)
        self.progressbar.pack(fill=X, expand=1)
        k = 0
        while k <= MAX:
        ### some work to be done
            progress_var.set(k)
            k += 0.1
            time.sleep(0.01)
            self.frame.update()
        if self.solve_button.winfo_ismapped():
            self.solve_button.grid_forget()
        else:
            self.solve_button.grid(pady=(10, 20))
        self.progress_bar_label.grid_forget()
        self.progressbar.pack_forget()
        self.pic_button["state"] = "disabled"
        print("taking photos")
        pass


if __name__ == "__main__":
    root = tk.Tk()
    my_gui = RubiksSolverGui(root)
    root.mainloop()
