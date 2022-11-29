import pickle
import glob

class Stage:
    def __init__(self, path):
        self.path = path
        self.file_list = glob.glob(self.path+'*.pickle')
        self.file_list.sort()
        print(self.file_list)

        self.instructList = []
        self.goal = []
        for file in self.file_list:
            with open(file, "rb") as fr:
                pkl_stage = pickle.load(fr)
                self.instructList.append(pkl_stage['instruction_list'])
                self.goal.append(pkl_stage['goal'])

    def stages(self):
        return self.instructList, self.goal

    def save_stage(self, idx, instruction_list, goal):
        if len(instruction_list) == 0:
            print("instruction_list must contain at least one command. ")
        elif len(goal) != 2:
            print("stage goal length must to two. (x,y)")
        else:
            stageObject = {'instruction_list': instruction_list, 'goal': goal}
            self.file_list.append(f'{idx:02d}.pickle')
            with open(self.path + f"{idx:02d}.pickle", "wb") as fw:
                pickle.dump(stageObject, fw)

if __name__ == "__main__":
    stage = Stage("stage/")
    stage.save_stage(1,["turtle.forward(50)","turtle.forward(50)"],(100,0))
    stage.save_stage(2,["turtle.right(90)", "turtle.forward(50)", "turtle.forward(50)"], (0,-100))
    stage.save_stage(3,["turtle.left(90)", "turtle.left(90)", "turtle.left(90)", "turtle.forward(100)"], (0,-100))
    stage.save_stage(4,["turtle.forward(50)","turtle.left(90)","turtle.forward(50)"], (50, 50))
    stage.save_stage(5,["turtle.left(90)","turtle.forward(50)","turtle.left(90)","turtle.forward(50)"], (-50, 50))
    stage.save_stage(6,["turtle.left(45)","turtle.forward(50)",
                        "turtle.left(90)","turtle.forward(50)","turtle.forward(50)",
                        "turtle.right(90)","turtle.forward(50)"],(0,141))
    stage.save_stage(7,["turtle.forward(50)", "turtle.left(90)", "turtle.forward(50)",
                        "turtle.right(90)","turtle.forward(50)", "turtle.left(90)", "turtle.forward(50)"], (100, 100))
    stage.save_stage(8,["turtle.forward(50)","turtle.left(90)",
                        "turtle.forward(50)","turtle.left(90)",
                        "turtle.forward(100)","turtle.left(90)",
                        "turtle.forward(100)","turtle.left(90)","turtle.forward(100)"], (49,-50))
    stage.save_stage(9,["turtle.left(45)","turtle.forward(50)"],(35, 35))
    stage.save_stage(10,["turtle.left(45)","turtle.forward(50)",
                         "turtle.left(45)","turtle.forward(50)",
                         "turtle.left(45)","turtle.forward(50)",
                         "turtle.left(45)","turtle.forward(50)"], (-49, 120))
