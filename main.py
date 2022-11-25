import tkinter as tk
import time
from myTurtle import MyTurtle

class LearningCodingWithTurtleGUI:
    def __init__(self, master, instruct_list, goal):
        self.width, self.height = (400, 300)
        self.command_num = 0
        self.max_command_num = 10
        self.instruct_list = instruct_list
        self.master = master
        self.master.title("Learning Coding With Turtle")
        self.master.geometry("600x400")
        self.master.resizable(False, False)
        self.turtle = MyTurtle(master=self.master,width=self.width,height=self.height)
        self.turtle.setGoal(goal)

        self.leftFrame = tk.Frame(self.master, width=200, height=300,padx=10, pady=10, bd=2, relief="solid")
        self.leftFrame.grid(column=0,row=0)
        self.leftFrame.propagate(0)

        self.commandText = tk.Text(self.leftFrame, width=190,height=290)
        self.commandText.pack()

        self.bottomFrame = tk.LabelFrame(self.master, width=600, height=100, padx=10, pady=10)
        self.bottomFrame.grid(column=0,row=1,columnspan=10)
        self.bottomFrame.propagate(0)

        self.btn = []
        for idx, instruct in enumerate(list(set(instruct_list))):
            self.btn.append(tk.Button(self.bottomFrame,
                                      text=instruct,
                                      command=lambda c=idx:self.command_click("\n"+instruct_list[c])))
            self.btn[idx].place(x=150*(idx % 2), y=40*(idx//2))
        self.runBtn = tk.Button(self.bottomFrame,
                                text="Run",
                                command=self.run_click)
        self.runBtn.place(x=self.width, y=0)
        self.deleteBtn = tk.Button(self.bottomFrame,
                                   text="Delete",
                                   command=self.delete_click)
        self.deleteBtn.place(x=self.width, y=30)
        self.resetBtn = tk.Button(self.bottomFrame,
                                  text="Reset",
                                  command=self.reset_click)
        self.resetBtn.place(x=self.width + 50, y=0)

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
        for instruct in self.instruct_list:
            exec("self."+instruct)
        time.sleep(1)
        self.turtle.reset()

    def start(self):
        self.master.after(200, self.step)

    def step(self):
        print(self.turtle.pos())
        if self.turtle.pos() == goal:
            self.commandText.delete("1.0", "end")
            self.commandText.insert(tk.END,"SUCCESS!!")
        else:
            self.master.after(1000, self.step)


if __name__ == '__main__':
    instructList = ["turtle.forward(50)","turtle.left(90)","turtle.forward(50)"]
    goal = (50,50)
    root = tk.Tk()
    app = LearningCodingWithTurtleGUI(root, instructList, goal)
    app.show_goal()
    app.start()
    tk.mainloop()
