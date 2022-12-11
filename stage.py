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
    stage.save_stage(1, ["Forward()"],                                  (50,0))
    stage.save_stage(2, ["Left()"],                                     (0, 0))
    stage.save_stage(3, ["Left()","Forward()"],                         (0, 50))
    stage.save_stage(4, ["Forward()","Left()","Forward()"],             (50, 50))
    stage.save_stage(5, ["Left()","Left()","Left()", "Forward()"],      (0, -50))
    stage.save_stage(6, ["Left()","Forward()","Left()","Forward()"],    (-50, 50))
    stage.save_stage(7, ["Right()", "Forward()", "Forward()"],          (0,-100))
    stage.save_stage(8, ["Put()"],                                      (0, 0))
    stage.save_stage(9, ["Forward()", "Put()","Forward()"],             (100, 0))
    stage.save_stage(10, ["Left()","Forward()","Put()",
                          "Left()","Forward()","Forward()",
                          "Right()","Forward()"],                        (-100,100))
    stage.save_stage(11,["Forward()", "Left()", "Forward()","Put()",
                         "Right()","Forward()", "Left()", "Forward()"], (100, 100))
    stage.save_stage(12, ["Forward()", "Left()", "Forward()", "Left()",
                          "Forward()", "Left()", "Forward()", "Left()"], (0, 0))
    stage.save_stage(13, ["DrawRectangle()"],                            (0, 0))
    stage.save_stage(14, ["DrawRectangle()","Left()",
                          "DrawRectangle()","Left()",
                          "DrawRectangle()","Left()",
                          "DrawRectangle()"],                             (0, 0))

