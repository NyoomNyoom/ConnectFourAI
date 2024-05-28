import tkinter as tk


class Gui:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Connect Four")
        self.window.config(bg="lightgrey")

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

        optionList = tk.OptionMenu(self.window, defaultSelect, *options)
        for child in self.window.winfo_children():
            child.destroy()
        headingText = tk.Label(text="Please select the players for the game from the drop down lists below.")
        headingText.pack()
        optionList.pack()

        self.window.mainloop()

    def gameScreen(self):
        pass

    def updateGameScreen(self):
        pass


if __name__ == '__main__':
    guiRun = Gui()
    guiRun.startGame()
