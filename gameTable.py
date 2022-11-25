import tkinter as tk
from PIL import ImageTk,Image

class GameTableFrame(tk.Frame):
    def __init__(self, master):
        self.master = master
        super(GameTableFrame, self).__init__(self.master)

        self.bg = ImageTk.PhotoImage(Image.open("image/gameTable.png"))
        self.lbl = tk.Label(self, image=self.bg)
        self.lbl.img = self.bg  # Keep a reference in case this code put is in a function.
        self.lbl.place(relx=0.5, rely=0.5, anchor='center')  # Place label in center of parent.