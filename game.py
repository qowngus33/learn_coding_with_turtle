import tkinter as tk
import time
from player import Player

class GamePage:
    def __init__(self, master, instruct_list, goal):
        self.width, self.height = (400, 300)
        self.command_num = 0
        self.max_command_num = 10
        self.goal = goal
        self.instruct_list = instruct_list
        self.master = master
        self.turtle = Player(master=self.master,width=self.width,height=self.height)
        self.turtle.setGoal(goal)

        self.leftFrame = tk.Frame(self.master,width=200,height=300,padx=10,pady=10,bd=2)
        self.leftFrame.grid(column=0,row=0)
        self.leftFrame.propagate(0)
        self.commandText = tk.Text(self.leftFrame,width=190,height=290,font=("Arial", 18))
        self.commandText.config(state="disabled")
        self.commandText.pack()

        self.bottomFrame = tk.LabelFrame(self.master,width=600,height=100,padx=10,pady=10,bg="white")
        self.bottomFrame.grid(column=0,row=1,columnspan=10)
        self.bottomFrame.propagate(0)

        self.btn = []
        btn_instruct = list(set(instruct_list))
        for idx, instruct in enumerate(btn_instruct):
            self.btn.append(tk.Button(self.bottomFrame,
                                      text=instruct,
                                      width=15,
                                      font=("Arial", 15),
                                      command=lambda c=idx:self.command_click("\n"+btn_instruct[c])))
            self.btn[idx].place(x=180*(idx % 2), y=40*(idx//2))

        self.runBtn = tk.Button(self.bottomFrame,width=5,text="Run",command=self.run_click,font=("Arial", 15),bg="white")
        self.deleteBtn = tk.Button(self.bottomFrame,width=5,text="Delete",command=self.delete_click,font=("Arial", 15))
        self.homeBtn = tk.Button(self.bottomFrame,width=5,text="Home",font=("Arial", 15))
        self.showGoalBtn = tk.Button(self.bottomFrame,width=5,text="Goal",command=self.show_goal,font=("Arial", 15))

        self.runBtn.place(x=self.width, y=0)
        self.deleteBtn.place(x=self.width, y=30)
        self.homeBtn.place(x=self.width + 80, y=0)
        self.showGoalBtn.place(x=self.width + 80, y=30)

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
        for command in command_list:
            if len(command) > 0:
                try:
                    exec("self." + command)
                except SyntaxError as err:
                    print(err.lineno)
        print(int(self.turtle.pos()[0]),int(self.turtle.pos()[1]),self.goal)
        if (int(self.turtle.pos()[0]),int(self.turtle.pos()[1])) == self.goal:
            time.sleep(0.5)
            self.game_over()
        else:
            time.sleep(1)
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
            exec("self."+instruct)
        time.sleep(1)
        self.turtle.reset()

    def game_over(self):
        self.commandText.configure(state='normal')
        self.commandText.delete("1.0", "end")
        if self.command_num <= len(self.instruct_list):
            self.commandText.insert(tk.END, f"SUCCESS!!\n\nYou Did It With Average Command Number Or Better!!")
        else:
            self.commandText.insert(tk.END, f"SUCCESS!!\n\nBut You Can Try Again With Shorter Length Of Commands.")
        self.commandText.config(state="disabled")
        self.command_num = 0

        # disable buttons
        self.deleteBtn.config(state="disabled")
        self.runBtn.config(state="disabled")
        self.showGoalBtn.config(state="disabled")
        for btn in self.btn:
            btn.config(state="disabled")

    def reset(self):
        self.turtle.reset()
        self.commandText.configure(state='normal')
        self.commandText.delete("1.0", "end")
        self.commandText.configure(state='normal')
        self.deleteBtn.config(state="normal")
        self.runBtn.config(state="normal")
        self.showGoalBtn.config(state="normal")
        for btn in self.btn:
            btn.config(state="normal")
