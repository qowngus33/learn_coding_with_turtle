import turtle
import tkinter as tk

WIDTH = 500
HEIGHT = 500

class MyTurtle(turtle.RawTurtle):
    def __init__(self, canvas):
        super(MyTurtle, self).__init__(canvas)
        self.shape("turtle")
        self.shapesize(2, 2)
        self.getscreen().bgcolor("yellow")

        self.center_offset_x = WIDTH / 2
        self.center_offset_y = HEIGHT / 2

        canvas.bind("<Button-1>", self.on_mouse_clicked)

        self.is_moving = False

    def on_mouse_clicked(self, event):
        if self.acquire_lock():
            x = event.x - self.center_offset_x
            y = -(event.y - self.center_offset_y)

            print("clicked ({0}, {1})".format(x, y))
            self.goto(x, y)

            self.release_lock()

    def acquire_lock(self):
        if self.is_moving is True:
            return False

        self.is_moving = True
        return True

    def release_lock(self):
        self.is_moving = False
