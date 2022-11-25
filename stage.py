
class Stage:
    def __init__(self):
        self.load_stage()

    def load_stage(self):
        self.instructList = [["turtle.forward(50)"],
                             ["turtle.left(90)","turtle.forward(50)"],
                             ["turtle.forward(50)", "turtle.left(90)", "turtle.forward(50)", "turtle.left(90)", "turtle.forward(50)", "turtle.forward(50)"
                              , "turtle.left(90)", "turtle.forward(50)", "turtle.forward(50)", "turtle.left(90)", "turtle.forward(50)", "turtle.forward(50)",],
                             ["turtle.forward(50)"],
                             ["turtle.forward(50)"],]
        self.goal = [(50, 0), (0, 50), (50, 50), (50, 0), (50, 0)]

    def stages(self):
        return self.instructList, self.goal

    def save_stage(self):
        pass