class UserAgent:
    def __init__(self, name):
        self.name = name

    def agentFunction(self):
        print(f"{self.name} it is your turn!")
        userMove = input("Please enter the column you would like to play the counter in: ")

        return int(userMove) - 1
