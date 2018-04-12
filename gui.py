from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import time

import optimized_color_finder

class ResizingCanvas(tk.Canvas):
    def __init__(self,parent,**kwargs):
        tk.Canvas.__init__(self,parent,**kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()
        self.r1 = []

    def on_resize(self,event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all",0,0,wscale,hscale)


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

        self.frame2 = tk.Frame(self.frame)
        self.frame2.grid(row=4)

        self.frame3 = tk.Frame(self.frame2)
        self.frame3.pack(fill=BOTH, expand=YES)

        self.mycanvas = ResizingCanvas(self.frame3,width=301, height=226, bg="white", highlightthickness=0)
        self.mycanvas.pack(fill=BOTH, expand=YES, padx=(20, 20), pady=(20, 20))


        self.r1 = [self.mycanvas.create_rectangle(0, 75, 25, 100, fill="lime green"),
            self.mycanvas.create_rectangle(0, 100, 25, 125, fill="lime green"),
            self.mycanvas.create_rectangle(0, 125, 25, 150, fill="lime green"),

            self.mycanvas.create_rectangle(25, 75, 50, 100, fill="lime green"),
            self.mycanvas.create_rectangle(25, 100, 50, 125, fill="lime green"),
            self.mycanvas.create_rectangle(25, 125, 50, 150, fill="lime green"),

            self.mycanvas.create_rectangle(50, 75, 75, 100, fill="lime green"),
            self.mycanvas.create_rectangle(50, 100, 75, 125, fill="lime green"),
            self.mycanvas.create_rectangle(50, 125, 75, 150, fill="lime green")]


        self.rec11 = self.mycanvas.create_rectangle(75, 0, 100, 25, fill="white")
        self.rec12 = self.mycanvas.create_rectangle(75, 25, 100, 50, fill="white")
        self.rec13 = self.mycanvas.create_rectangle(75, 50, 100, 75, fill="white")

        self.rec14 = self.mycanvas.create_rectangle(100, 0, 125, 25, fill="white")
        self.rec15 = self.mycanvas.create_rectangle(100, 25, 125, 50, fill="white")
        self.rec16 = self.mycanvas.create_rectangle(100, 50, 125, 75, fill="white")

        self.rec17 = self.mycanvas.create_rectangle(125, 0, 150, 25, fill="white")
        self.rec18 = self.mycanvas.create_rectangle(125, 25, 150, 50, fill="white")
        self.rec19 = self.mycanvas.create_rectangle(125, 50, 150, 75, fill="white")


        self.rec21 = self.mycanvas.create_rectangle(75, 75, 100, 100, fill="red")
        self.rec22 = self.mycanvas.create_rectangle(75, 100, 100, 125, fill="red")
        self.rec23 = self.mycanvas.create_rectangle(75, 125, 100, 150, fill="red")

        self.rec24 = self.mycanvas.create_rectangle(100, 75, 125, 100, fill="red")
        self.rec25 = self.mycanvas.create_rectangle(100, 100, 125, 125, fill="red")
        self.rec26 = self.mycanvas.create_rectangle(100, 125, 125, 150, fill="red")

        self.rec27 = self.mycanvas.create_rectangle(125, 75, 150, 100, fill="red")
        self.rec28 = self.mycanvas.create_rectangle(125, 100, 150, 125, fill="red")
        self.rec29 = self.mycanvas.create_rectangle(125, 125, 150, 150, fill="red")


        self.rec31 = self.mycanvas.create_rectangle(75, 150, 100, 175, fill="yellow")
        self.rec32 = self.mycanvas.create_rectangle(75, 175, 100, 200, fill="yellow")
        self.rec33 = self.mycanvas.create_rectangle(75, 200, 100, 225, fill="yellow")

        self.rec34 = self.mycanvas.create_rectangle(100, 150, 125, 175, fill="yellow")
        self.rec35 = self.mycanvas.create_rectangle(100, 175, 125, 200, fill="yellow")
        self.rec36 = self.mycanvas.create_rectangle(100, 200, 125, 225, fill="yellow")

        self.rec37 = self.mycanvas.create_rectangle(125, 150, 150, 175, fill="yellow")
        self.rec38 = self.mycanvas.create_rectangle(125, 175, 150, 200, fill="yellow")
        self.rec39 = self.mycanvas.create_rectangle(125, 200, 150, 225, fill="yellow")


        self.rec41 = self.mycanvas.create_rectangle(150, 75, 175, 100, fill="blue")
        self.rec42 = self.mycanvas.create_rectangle(150, 100, 175, 125, fill="blue")
        self.rec43 = self.mycanvas.create_rectangle(150, 125, 175, 150, fill="blue")

        self.rec44 = self.mycanvas.create_rectangle(175, 75, 200, 100, fill="blue")
        self.rec45 = self.mycanvas.create_rectangle(175, 100, 200, 125, fill="blue")
        self.rec46 = self.mycanvas.create_rectangle(175, 125, 200, 150, fill="blue")

        self.rec47 = self.mycanvas.create_rectangle(200, 75, 225, 100, fill="blue")
        self.rec48 = self.mycanvas.create_rectangle(200, 100, 225, 125, fill="blue")
        self.rec49 = self.mycanvas.create_rectangle(200, 125, 225, 150, fill="blue")


        self.rec51 = self.mycanvas.create_rectangle(225, 75, 250, 100, fill="orange")
        self.rec52 = self.mycanvas.create_rectangle(225, 100, 250, 125, fill="orange")
        self.rec53 = self.mycanvas.create_rectangle(225, 125, 250, 150, fill="orange")

        self.rec54 = self.mycanvas.create_rectangle(250, 75, 275, 100, fill="orange")
        self.rec55 = self.mycanvas.create_rectangle(250, 100, 275, 125, fill="orange")
        self.rec56 = self.mycanvas.create_rectangle(250, 125, 275, 150, fill="orange")

        self.rec57 = self.mycanvas.create_rectangle(275, 75, 300, 100, fill="orange")
        self.rec58 = self.mycanvas.create_rectangle(275, 100, 300, 125, fill="orange")
        self.rec59 = self.mycanvas.create_rectangle(275, 125, 300, 150, fill="orange")


        self.mycanvas.addtag_all("all")

        #self.close_button = tk.Button(self.frame, text="Close", command=master.quit)
        #self.close_button.grid(row=5, pady=(10, 20))

        self.answer = tk.StringVar()
        self.answerLabel = tk.Label(self.frame, textvariable=self.answer)
        self.answerLabel.grid(row=5)

        self.frame.pack(padx=20, pady=20)

    def solve_cube(self):
        print("solving done")
        pass

    def take_photo(self):
        #take_pic_with_gopro
        MAX = 5
        progress_var = DoubleVar()
        self.progress_bar_label = Label(self.frame, text="scanning...")
        self.progress_bar_label.grid(row=6)
        self.progressbar = ttk.Progressbar(root, variable=progress_var, maximum=MAX)
        self.progressbar.pack(fill=X, expand=1)
        k = 0
        while k <= MAX:
        ### some work to be done
            progress_var.set(k)
            k += 0.1
            time.sleep(0.01)
            self.frame.update()

        #finder = optimized_color_finder.ColorFinder("/Users/felixdefrance/.envs/cv/cube/test3.png")
        #result = finder.analyse()
        result = ["orange", "green", "orange", "green","orange", "green","orange", "green", "orange"]
        for elt, i in zip(self.r1, range(len(self.r1))):
            self.mycanvas.itemconfig(elt, fill=str(result[i]))

        #self.answer.set(str(finder.analyse()))

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
