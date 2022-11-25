import pickle
import glob

class Stage:
    def __init__(self, path):
        self.path = path
        self.file_list = glob.glob(self.path+'*.pickle')
        self.file_list.sort()

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
        stageObject = {'instruction_list': instruction_list, 'goal': goal}

        self.file_list.append(f'{idx}.pickle')
        with open(self.path+f"{idx}.pickle", "wb") as fw:
            pickle.dump(stageObject, fw)

if __name__ == "__main__":
    stage = Stage("stage/")
    stage.save_stage(1,["turtle.forward(50)","turtle.forward(50)"],(100,0))
    stage.save_stage(2,["turtle.left(90)", "turtle.left(90)", "turtle.left(90)", "turtle.forward(50)"], (0,-50))
    stage.save_stage(3,["turtle.right(90)", "turtle.forward(50)", "turtle.forward(50)"], (0,-100))
    stage.save_stage(4,["turtle.forward(50)", "turtle.left(90)", "turtle.forward(50)",
                        "turtle.right(90)","turtle.forward(50)", "turtle.left(90)", "turtle.forward(50)"], (100, 100))
    stage.save_stage(5,["turtle.forward(50)","turtle.left(90)",
                        "turtle.forward(50)","turtle.left(90)",
                        "turtle.forward(100)","turtle.left(90)",
                        "turtle.forward(100)","turtle.left(90)","turtle.forward(100)"], (49,-50))
