import tkinter as tk
from connectFourGame import Game


class Gui:
    def __init__(self, gameIn: Game):
        self.window = tk.Tk()
        self.window.title("Connect Four")
        self.window.config(bg="lightgrey")

        self.game = gameIn

    def startGame(self):
        def buttonClicked():
            self.playerSelection()

        textFrame = tk.Frame()
        buttonFrame = tk.Frame()

        welcomeText = tk.Label(text="Welcome to Connect Four!", master=textFrame)
        welcomeText.pack()

        informationText = tk.Label(text="Please press the play button below to start.", master=textFrame)
        informationText.pack()

        playButton = tk.Button(text="Play Game", command=buttonClicked, master=buttonFrame)
        playButton.pack()

        textFrame.pack()
        buttonFrame.pack()

        self.window.mainloop()

    def playerSelection(self):
        options = ["Player", "Random AI"]

        defaultSelect = tk.StringVar()
        defaultSelect.set("Player")

        for child in self.window.winfo_children():
            child.destroy()

        headingText = tk.Label(text="Please select the players for the game from the drop down lists below.")
        headingText.pack()

        optionList = tk.OptionMenu(self.window, defaultSelect, *options)
        optionList.pack()

        self.window.mainloop()

    def gameScreen(self):
        self.game.whoIsPlaying()

    def updateGameScreen(self):
        pass

    def clearScreen(self, screen: tk.Tk):
        for child in screen.winfo_children():
            child.destroy()


if __name__ == '__main__':
    guiRun = Gui()
    guiRun.startGame()
