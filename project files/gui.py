import tkinter as tk
from connectFourGame import Game
from connectFourGame import Player
from userAgent import UserAgent
from randomAgent import RandomAgent


class Gui:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Connect Four")
        self.window.config(bg="lightgrey")

        self.game: Game

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
        self.clearScreen(self.window)

        def playClicked():
            # Change to a game creation.

            self.gameScreen()

        titleFrame = tk.Frame()
        headingFrame = tk.Frame()
        player1Frame = tk.Frame()
        player2Frame = tk.Frame()
        playFrame = tk.Frame()

        options = ["Player", "Random AI"]
        defaultSelect = tk.StringVar()
        defaultSelect.set("Player")

        options2 = ["Player", "Random AI"]
        defaultSelect2 = tk.StringVar()
        defaultSelect2.set("Player")

        titleText = tk.Label(text="Player Selection", font=("Arial", 30), master=titleFrame)
        titleText.pack()

        informationText = tk.Label(text="Please select the players for the game from the drop down lists below.",
                                   master=headingFrame)
        informationText.pack()

        player1Text = tk.Label(text="Please select a player type for player 1: ", master=player1Frame)
        player1Text.pack()

        optionList = tk.OptionMenu(player1Frame, defaultSelect, *options)
        optionList.pack()

        player2Text = tk.Label(text="Please select a player type for player 2: ", master=player2Frame)
        player2Text.pack()

        option2List = tk.OptionMenu(player2Frame, defaultSelect2, *options2)
        option2List.pack()

        playbtn = tk.Button(text="Play", master=playFrame, command=playClicked)
        playbtn.pack()

        titleFrame.pack()
        headingFrame.pack()
        player1Frame.pack()
        player2Frame.pack()
        playFrame.pack()

        self.window.mainloop()

    def gameScreen(self):
        while not self.game.isGameWon:
            self.clearScreen(self.window)

            board = tk.Canvas()
            board.create_rectangle(0, 0, 600, 700, fill="blue")

            self.game.playGame()

            self.updateGameScreen(self.game.gameBoard, board)
            board.pack()

            self.window.mainloop()

    def updateGameScreen(self, gameBoardIn, background: tk.Canvas):
        gameBoard = gameBoardIn

        rowNum = 0
        colNum = 0

        for row in gameBoard:
            for space in row:
                if space == 0:
                    background.create_oval(colNum*40,rowNum*40, (colNum+1)*40, (rowNum+1)*40, fill="white")
                elif space == 1:
                    background.create_oval(colNum * 40, rowNum * 40, (colNum + 1) * 40, (rowNum + 1) * 40, fill="yellow")
                elif space == 2:
                    background.create_oval(colNum * 40, rowNum * 40, (colNum + 1) * 40, (rowNum + 1) * 40, fill="red")
                colNum += 1
            rowNum += 1
            colNum = 0

    def clearScreen(self, screen: tk.Tk):
        for child in screen.winfo_children():
            child.destroy()


if __name__ == '__main__':
    player1 = Player(UserAgent("p1"))
    player2 = Player(UserAgent("p2"))
    newGame = Game(player1, player2)

    guiRun = Gui(newGame)
    guiRun.gameScreen()
