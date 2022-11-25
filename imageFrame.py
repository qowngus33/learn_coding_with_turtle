import tkinter as tk
from PIL import ImageTk,Image

class ImageFrame(tk.Frame):
    def __init__(self, master, imagePath):
        self.master = master
        super(ImageFrame, self).__init__(self.master)

        self.bg = ImageTk.PhotoImage(Image.open(imagePath))
        self.lbl = tk.Label(self, image=self.bg)
        self.lbl.img = self.bg  # Keep a reference in case this code put is in a function.
        self.lbl.place(relx=0.5, rely=0.5, anchor='center')  # Place label in center of parent.
