import turtle
import tkinter as tk

class Player(turtle.RawTurtle):
    def __init__(self, master, width, height):
        self.canvas = tk.Canvas(master)
        self.canvas.grid(column=1, row=1)
        self.canvas.config(width=width, height=height)
        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.bgpic("image/noname.png")

        self.screen.register_shape("image/puddle.gif")
        self.screen.register_shape("image/put.gif")
        self.screen.register_shape("image/none.gif")
        super(Player, self).__init__(self.screen)

        self.river = turtle.RawTurtle(self.screen)
        self.river.penup()
        self.river.shape("image/puddle.gif")

        self.put = turtle.RawTurtle(self.screen)
        self.put.penup()
        self.put.shape("image/none.gif")

        self.foot_print = []

        self.shape("turtle")
        self.shapesize(1.3, 1.3)
        self.speed(1)

    def setGoal(self,goal):
        self.river.setpos(goal)

    def setFootprint(self, foot_print):
        # self.foot_print.append(turtle.RawTurtle(self.screen))
        # self.foot_print[len(self.foot_print)-1].shape("image/foot-print.gif")
        # self.foot_print[len(self.foot_print) - 1].setpos(0,0)
        pass

    def reset(self):
        super(Player, self).reset()
        self.put.shape("image/none.gif")
        self.shapesize(1.3, 1.3)
        self.speed(1)

    def Forward(self):
        self.forward(50)

    def Left(self):
        self.left(90)

    def Right(self):
        self.right(90)

    def Put(self):
        self.put.setpos(self.pos())
        self.put.shape("image/put.gif")

