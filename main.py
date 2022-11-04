import turtle
import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Learning Coding With Turtle")

canvas = tk.Canvas(root)
canvas.grid(column=1,row=0)
canvas.config(width=400, height=300)
screen = turtle.TurtleScreen(canvas)
screen.bgcolor("cyan")
t = turtle.RawTurtle(screen,shape="turtle")

leftFrame = tk.Frame(root, width=200, height=300,padx=10, pady=10, bd=2, relief="solid")
leftFrame.grid(column=0,row=0)
leftFrame.propagate(0)

bottomFrame = tk.LabelFrame(root, width=600, height=100, padx=10, pady=10)
bottomFrame.grid(column=0,row=1,columnspan=2)
bottomFrame.propagate(0)

def clickEvent():
    label = tk.Label(leftFrame,text="버튼을 클릭했삼")
    label.pack()

btn = tk.Button(bottomFrame, text="play",command=clickEvent)
btn.pack()

tk.mainloop()
