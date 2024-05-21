import tkinter as tk


class Gui:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Connect Four")
        self.window.config(bg="lightgrey")

    def startGame(self):
        self.window.mainloop()

    def playerSelection(self):
        pass

    def gameScreen(self):
        pass

    def updateGameScreen(self):
        pass

if __name__ == '__main__':
    guiRun = Gui()
    guiRun.startGame()
    