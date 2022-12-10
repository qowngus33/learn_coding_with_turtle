import tkinter as tk
from tkinter.font import Font
import time
from imageFrame import ImageFrame
from player import Player

class GamePage:
    def __init__(self, master, instruct_list, goal):
        self.width, self.height = (400, 300)
        self.command_num = 0
        self.max_command_num = 10
        self.goal = goal
        self.instruct_list = instruct_list
        self.master = master
        self.gameFrame = tk.Frame(self.master, width=600, height=400, bd=2, bg="white")
        self.turtle = Player(master=self.gameFrame,width=self.width,height=self.height)
        self.turtle.setGoal(goal)
        self.turtle.setFootprint([])

        self.topFrame = tk.Frame(self.gameFrame,width=600,height=30,bd=2,bg="white")
        self.topFrame.grid(column=0, row=0,columnspan=10)
        self.leftFrame = tk.LabelFrame(self.gameFrame,width=200,height=300,padx=10,pady=10,bd=2)
        self.leftFrame.grid(column=0,row=1)
        self.bottomFrame = tk.LabelFrame(self.gameFrame,width=600,height=90,padx=10,pady=10,bg="white")
        self.bottomFrame.grid(column=0,row=2,columnspan=10)
        self.successFrame = ImageFrame(self.master, "image/success.png")

        self.gameFrame.grid(row=0, column=0, sticky="nsew")
        self.successFrame.grid(row=0, column=0, sticky="nsew")

        self.leftFrame.propagate(0)
        self.topFrame.propagate(0)
        self.bottomFrame.propagate(0)

        self.commandText = tk.Text(self.leftFrame,width=190,height=290,font=("Arial", 18))
        self.commandText.config(state="disabled")
        self.bold_font = Font(family="Arial", size=18, weight="bold")
        self.commandText.tag_configure("BOLD", font=self.bold_font)
        self.commandText.pack()
        self.stageNumText = tk.Text(self.topFrame,  font=("Arial", 18))

        self.btn = []
        btn_instruct = list(set(instruct_list))
        for idx, instruct in enumerate(btn_instruct):
            self.btn.append(tk.Button(self.bottomFrame,
                                      text=instruct,
                                      width=10,
                                      font=("Arial", 15),
                                      command=lambda c=idx:self.command_click("\n"+btn_instruct[c])))
            self.btn[idx].place(x=150*(idx % 2), y=35*(idx//2))

        self.homeBtn = tk.Button(self.topFrame,text="Go back",font=("Arial", 15))
        self.nextBtn = tk.Button(self.successFrame, text=">", font=("Arial", 15))
        self.runBtn = tk.Button(self.bottomFrame,width=5,text="Run",command=self.run_click,font=("Arial", 15),bg="white")
        self.deleteBtn = tk.Button(self.bottomFrame,width=5,text="Delete",command=self.delete_click,font=("Arial", 15))
        self.showGoalBtn = tk.Button(self.bottomFrame,width=5,text="Goal",command=self.show_goal,font=("Arial", 15))
        self.resetBtn = tk.Button(self.bottomFrame, width=5, text="Debug", command=self.debug,font=("Arial", 15))

        self.stageNumText.place(x=10, y=0)
        self.homeBtn.place(x=self.width+90, y=0)
        self.nextBtn.place(x=self.width+80, y=self.height/2+50)
        self.runBtn.place(x=self.width, y=0)
        self.deleteBtn.place(x=self.width+80, y=0)
        self.showGoalBtn.place(x=self.width, y=30)
        self.resetBtn.place(x=self.width+80, y=30)
        self.gameFrame.tkraise()

    def command_click(self, instruct):
        self.commandText.configure(state='normal')
        if self.command_num < self.max_command_num:
            self.commandText.insert(tk.END,instruct)
            self.command_num += 1
        self.commandText.config(state="disabled")

    def run_click(self):
        self.turtle.reset()
        result = self.commandText.get("1.0","end-1c")
        command_list = result.split("\n")
        valid_command_list = []
        for command in command_list:
            if len(command) > 0:
                try:
                    exec("self.turtle." + command)
                    valid_command_list.append(command)
                except SyntaxError as err:
                    print(err.lineno)
        success = True
        if len(valid_command_list) == len(self.instruct_list):
            for i in range(len(valid_command_list)):
                if valid_command_list[i] != self.instruct_list[i]:
                    success = False
        else:
            success = False
        if success:
            time.sleep(0.3)
            self.game_over()
        else:
            time.sleep(0.3)
            self.turtle.reset()

    def delete_click(self):
        self.commandText.configure(state='normal')
        result = self.commandText.get("1.0","end-1c")
        result = result[:max(0,result.rfind("\n"))]
        self.commandText.delete("1.0",tk.END)
        self.commandText.insert(tk.CURRENT,result)
        self.command_num = max(0,self.command_num-1)
        self.commandText.config(state="disabled")

    def show_goal(self):
        self.turtle.reset()
        for instruct in self.instruct_list:
            exec("self.turtle."+instruct)
        time.sleep(0.5)
        self.turtle.reset()

    def game_over(self):
        self.reset()
        self.successFrame.tkraise()

    def reset(self):
        self.turtle.reset()
        self.commandText.configure(state='normal')
        self.commandText.delete("1.0", "end")
        self.commandText.configure(state='disabled')
        self.deleteBtn.config(state="normal")
        self.runBtn.config(state="normal")
        self.showGoalBtn.config(state="normal")
        self.resetBtn.config(state="normal")
        for btn in self.btn:
            btn.config(state="normal")

    def debug(self):
        self.turtle.reset()
        result = self.commandText.get("1.0", "end-1c")
        command_list = result.split("\n")
        for idx, command in enumerate(command_list):
            if len(command) > 0:
                try:
                    self.make_bold(idx+1)
                    exec("self.turtle." + command)
                    time.sleep(0.4)
                    self.commandText.tag_remove("BOLD", str(idx+1) + ".0", str(idx+1) + ".0+1line")
                except SyntaxError as err:
                    print(err.lineno)
        time.sleep(0.3)
        self.turtle.reset()

    def make_bold(self,idx):
        try:
            self.commandText.tag_add("BOLD", str(idx)+".0", str(idx)+".0+1line")
        except tk.TclError:
            pass
