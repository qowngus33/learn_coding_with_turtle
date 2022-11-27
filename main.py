import tkinter as tk

from game import GamePage
from stage import Stage
from imageFrame import ImageFrame

def center_window(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2)-(width/2)
    y = (screen_height/2)-(height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

class LearnCodingWithTurtle:
    def __init__(self, root, instructList, goal):
        self.root = root
        self.instructList = instructList
        self.goal = goal
        self.root.title("LCWT")
        self.root.resizable(False, False)
        center_window(self.root,600,400)

        self.gameFrame = [tk.Frame(self.root) for _ in range(len(self.instructList))]
        self.game = [GamePage(self.gameFrame[i],self.instructList[i],goal[i]) for i in range(len(self.instructList))]
        self.startFrame = ImageFrame(self.root,"image/startPage.png")
        self.gameTableFrame = ImageFrame(self.root,"image/gameTable.png")
        self.tutorialFrame = ImageFrame(self.root, "image/tutorial.png")

        # add home buttons
        for i in range(len(self.gameFrame)):
            self.gameFrame[i].grid(row=0,column=0,sticky="nsew")
            self.game[i].homeBtn.configure(text="Home",command=lambda:[self.gameTableFrame.tkraise()])
        self.homeBtn = tk.Button(self.tutorialFrame,text="Go Back",command=lambda:[self.gameTableFrame.tkraise()])
        self.homeBtn.place(x=500,y=10)

        self.btnToTable = tk.Button(self.startFrame,
                                    width=15,
                                    padx=10,
                                    pady=10,
                                    text="Game Start",
                                    font=("Arial", 20),
                                    command=lambda:[self.gameTableFrame.tkraise()])
        self.btnToTable.place(x=190,y=300)

        self.btnToGame = []
        for i in range(len(self.instructList)):
            self.btnToGame.append(tk.Button(self.gameTableFrame,
                                            text=str(i+1),
                                            bg='white',
                                            font=("Arial", 15),
                                            command=lambda c=i:self.start_game(self.gameFrame[c],self.game[c])))
            self.btnToGame[i].place(x=95*(i+1),y=130*((i%2==1)+1))

        self.btnToTutorial = tk.Button(self.gameTableFrame,text="?",command=lambda:[self.tutorialFrame.tkraise()])
        self.btnToTutorial.place(x=550,y=10)

        self.gameTableFrame.grid(row=0,column=0,sticky="nsew")
        self.tutorialFrame.grid(row=0, column=0, sticky="nsew")
        self.startFrame.grid(row=0,column=0,sticky="nsew")
        self.startFrame.tkraise()

    def start_game(self, frame, game):
        game.reset()
        frame.tkraise()
        game.show_goal()

if __name__ == '__main__':
    instruct_list, goals = Stage("stage/").stages()
    app = LearnCodingWithTurtle(tk.Tk(),instruct_list,goals)
    tk.mainloop()
