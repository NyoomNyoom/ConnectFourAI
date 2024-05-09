import random as ran

class RandomAgent:
    def __init__(self):
        self.name = "Random Agent"

    def agentFunction(self):
        return ran.randint(1,7)