import tkinter as tk
import time
from myTurtle import MyTurtle
from PIL import Image, ImageTk

class GamePage:
    def __init__(self, master, instruct_list, goal):
        self.width, self.height = (400, 300)
        self.command_num = 0
        self.max_command_num = 10
        self.goal = goal
        self.isShowingGoal = False
        self.instruct_list = instruct_list
        self.master = master

        self.turtle = MyTurtle(master=self.master,width=self.width,height=self.height)
        self.turtle.setGoal(goal)

        self.leftFrame = tk.Frame(self.master,width=200,height=300,padx=10,pady=10,bd=2,relief="solid")
        self.leftFrame.grid(column=0,row=0)
        self.leftFrame.propagate(0)
        self.commandText = tk.Text(self.leftFrame,width=190,height=290)
        self.commandText.pack()

        self.bottomFrame = tk.LabelFrame(self.master,width=600,height=100,padx=10,pady=10)
        self.bottomFrame.grid(column=0,row=1,columnspan=10)
        self.bottomFrame.propagate(0)

        self.btn = []
        btn_instruct = list(set(instruct_list))
        for idx, instruct in enumerate(btn_instruct):
            self.btn.append(tk.Button(self.bottomFrame,
                                      text=instruct,
                                      width=15,
                                      command=lambda c=idx:self.command_click("\n"+btn_instruct[c])))
            self.btn[idx].place(x=180*(idx % 2), y=40*(idx//2))

        self.runBtn = tk.Button(self.bottomFrame,width=5,text="Run",command=self.run_click)
        self.deleteBtn = tk.Button(self.bottomFrame,width=5,text="Delete",command=self.delete_click)
        self.resetBtn = tk.Button(self.bottomFrame,width=5,text="Reset",command=self.reset_click)
        self.showGoalBtn = tk.Button(self.bottomFrame,width=5,text="Goal",command=self.show_goal)

        self.runBtn.place(x=self.width, y=0)
        self.deleteBtn.place(x=self.width, y=30)
        self.resetBtn.place(x=self.width + 80, y=0)
        self.showGoalBtn.place(x=self.width + 80, y=30)

    def command_click(self, instruct):
        if self.command_num < self.max_command_num:
            self.commandText.insert(tk.END,instruct)
            self.command_num += 1

    def run_click(self):
        result = self.commandText.get("1.0","end-1c")
        command_list = result.split("\n")
        for command in command_list:
            if len(command) > 0:
                exec("self."+command)

    def delete_click(self):
        result = self.commandText.get("1.0","end-1c")
        result = result[:max(0,result.rfind("\n"))]
        self.commandText.delete("1.0",tk.END)
        self.commandText.insert(tk.CURRENT,result)
        self.command_num = max(0,self.command_num-1)

    def reset_click(self):
        self.turtle.reset()

    def show_goal(self):
        self.isShowingGoal = True
        for instruct in self.instruct_list:
            exec("self."+instruct)
        time.sleep(1)
        self.turtle.reset()
        self.isShowingGoal = False

    def start(self):
        self.master.after(200, self.step)

    def step(self):
        print(self.turtle.pos())
        if (int(self.turtle.pos()[0]),int(self.turtle.pos()[1])) == self.goal:
            if not self.isShowingGoal:
                self.commandText.delete("1.0", "end")
                if self.command_num <= len(self.instruct_list):
                    self.commandText.insert(tk.END,f"SUCCESS!!\n\nYou Did It With Average Command Number Or Better!!")
                else:
                    self.commandText.insert(tk.END, f"SUCCESS!!\n\nBut You Can Try Again With Shorter Length Of Commands.")
        else:
            self.master.after(1000, self.step)
