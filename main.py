import tkinter as tk
import time

from game import GamePage
from stage import Stage
from imageFrame import ImageFrame

class LearnCodingWithTurtle:
    def __init__(self, root):
        self.root = root
        self.root.title("LCWT")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        self.gameFrame = [tk.Frame(self.root) for _ in range(len(instructList))]
        self.game = [GamePage(self.gameFrame[i],instructList[i],goal[i]) for i in range(len(instructList))]
        self.startFrame = ImageFrame(self.root,"image/startPage.png")
        self.gameTableFrame = ImageFrame(self.root,"image/gameTable.png")

        for i in range(len(self.gameFrame)):
            self.gameFrame[i].grid(row=0,column=0,sticky="nsew")
            self.game[i].homeBtn.configure(text = "Home", command=lambda:[self.gameTableFrame.tkraise()])

        self.gameTableFrame.grid(row=0, column=0, sticky="nsew")
        self.startFrame.grid(row=0, column=0, sticky="nsew")

        self.btnToTable = tk.Button(self.startFrame,
                                    width=15,
                                    padx=10,
                                    pady=10,
                                    text="Game Start",
                                    font=("Arial", 20),
                                    command=lambda:[self.gameTableFrame.tkraise()])
        self.btnToTable.place(x=190,y=300)

        self.btnToGame = []
        for i in range(len(instructList)):
            self.btnToGame.append(tk.Button(self.gameTableFrame,
                                            text=str(i+1),
                                            bg='white',
                                            font=("Arial", 15),
                                            command=lambda c=i:self.start_game(self.gameFrame[c],self.game[c])))
            self.btnToGame[i].place(x=95*(i+1), y=130*((i%2==1)+1))
        self.startFrame.tkraise()

    def start_game(self, frame, game):
        game.reset()
        frame.tkraise()
        game.show_goal()

if __name__ == '__main__':
    instructList, goal = Stage("stage/").stages()
    app = LearnCodingWithTurtle(tk.Tk())
    tk.mainloop()
