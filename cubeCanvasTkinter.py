from tkinter import Tk, Canvas, Button, mainloop
"""
i = 0

master = Tk()

def action():
    global i
    if i % 2 == 0:
        w.itemconfig(rec0, fill="red")
        w.itemconfig(rec1, fill="yellow")
        w.itemconfig(rec2, fill="green")
        w.itemconfig(rec3, fill="black")
        w.itemconfig(rec4, fill="purple")
        w.itemconfig(rec5, fill="yellow")
        w.itemconfig(rec6, fill="green")
        w.itemconfig(rec7, fill="yellow")
        w.itemconfig(rec8, fill="white")
    else:
        w.itemconfig(rec0, fill="blue")
        w.itemconfig(rec1, fill="blue")
        w.itemconfig(rec2, fill="blue")
        w.itemconfig(rec3, fill="blue")
        w.itemconfig(rec4, fill="blue")
        w.itemconfig(rec5, fill="blue")
        w.itemconfig(rec6, fill="blue")
        w.itemconfig(rec7, fill="blue")
        w.itemconfig(rec8, fill="blue")

    i += 1

w = Canvas(master, width=200, height=200)
w.pack()

rec0 = w.create_rectangle(50, 50, 75, 75, fill="blue")
rec1 = w.create_rectangle(50, 75, 75, 100, fill="blue")
rec2 = w.create_rectangle(50, 100, 75, 125, fill="blue")

rec3 = w.create_rectangle(75, 50, 100, 75, fill="blue")
rec4 = w.create_rectangle(75, 75, 100, 100, fill="blue")
rec5 = w.create_rectangle(75, 100, 100, 125, fill="blue")

rec6 = w.create_rectangle(100, 50, 125, 75, fill="blue")
rec7 = w.create_rectangle(100, 75, 125, 100, fill="blue")
rec8 = w.create_rectangle(100, 100, 125, 125, fill="blue")

bouton = Button(master, text = "blah", command=action)
bouton.pack()

mainloop()




"""
from tkinter import *

# a subclass of Canvas for dealing with resizing of windows
class ResizingCanvas(Canvas):
    def __init__(self,parent,**kwargs):
        Canvas.__init__(self,parent,**kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

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

def main():
    root = Tk()
    myframe = Frame(root)
    myframe.pack(fill=BOTH, expand=YES)

    label = Label(myframe, text="Welcome to the Rubik's Cube Solver!")
    label.pack()

    mycanvas = ResizingCanvas(myframe,width=850, height=400, bg="red", highlightthickness=0)
    mycanvas.pack(fill=BOTH, expand=YES, padx=(20, 20), pady=(20, 20))

    bouton = Button(myframe, text = "blah")
    bouton.pack(expand=YES)

    mycanvas.create_rectangle(50, 25, 150, 75, fill="blue")

    mycanvas.addtag_all("all")
    root.mainloop()

if __name__ == "__main__":
    main()
#"""