import turtle
import tkinter as tk

class MyTurtle(turtle.RawTurtle):
    def __init__(self, master, width, height):
        self.canvas = tk.Canvas(master)
        self.canvas.grid(column=1, row=0)
        self.canvas.config(width=width, height=height)
        self.screen = turtle.TurtleScreen(self.canvas)

        self.screen.register_shape("data/puddle-md.gif")
        super(MyTurtle, self).__init__(self.screen)

        # self.getscreen().bgcolor("green")
        self.river = turtle.RawTurtle(self.screen)
        self.river.penup()
        self.river.shape("data/puddle-md.gif")

        self.shape("turtle")
        self.shapesize(1.3, 1.3)
        self.speed(1)

    def setGoal(self,goal):
        self.river.setpos(goal)

    def reset(self):
        super(MyTurtle, self).reset()
        self.shapesize(1.3, 1.3)
        self.speed(1)


