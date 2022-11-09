import turtle
import tkinter as tk

class MyTurtle(turtle.RawTurtle):
    def __init__(self, master, width, height):
        self.canvas = tk.Canvas(master)
        self.canvas.grid(column=1, row=0)
        self.canvas.config(width=width, height=height)

        super(MyTurtle, self).__init__(self.canvas)

        self.shape("turtle")
        self.shapesize(1.3, 1.3)
        self.speed(1)
        self.getscreen().bgcolor("gray")

    def reset(self):
        super(MyTurtle, self).reset()
        self.speed(1)


