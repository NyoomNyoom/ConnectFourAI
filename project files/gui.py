import tkinter as tk
from tkinter import ttk
from connectFourGame import Game
from connectFourGame import Player
from userAgent import UserAgent
from randomAgent import RandomAgent


class Gui:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Connect Four")
        self.window.config(bg="lightgrey")

        self.player1_name: tk.Entry

        self.player1: Player
        self.player2: Player
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

            self.initGame()

        titleFrame = tk.Frame()
        headingFrame = tk.Frame()
        player1Frame = tk.Frame()
        player2Frame = tk.Frame()
        playFrame = tk.Frame()

        defaultSelect = tk.StringVar()
        defaultSelect.set("Player")

        defaultSelect2 = tk.StringVar()
        defaultSelect2.set("Player")

        titleText = tk.Label(text="Player Selection", font=("Arial", 30), master=titleFrame)
        titleText.pack()

        informationText = tk.Label(text="Please select the players for the game from the drop down lists below.",
                                   master=headingFrame)
        informationText.pack()

        player1Text = tk.Label(text="Please select a player type for player 1: ", master=player1Frame)
        player1Text.pack()

        self.player1_agent = ttk.Combobox(player1Frame, values=["player", "random ai"])
        self.player1_agent.set("player")
        self.player1_agent.pack()

        tk.Label(player1Frame, text="Player 1 Name:").pack()
        self.player1_name = tk.Entry(player1Frame)
        self.player1_name.pack()

        player2Text = tk.Label(text="Please select a player type for player 2: ", master=player2Frame)
        player2Text.pack()

        tk.Label(player2Frame, text="Player 2 Name:").pack()
        self.player2_name = tk.Entry(player2Frame)
        self.player2_name.pack()

        self.player2_agent = ttk.Combobox(player2Frame, values=["player", "random ai"])
        self.player2_agent.set("player")
        self.player2_agent.pack()

        playbtn = tk.Button(text="Play", master=playFrame, command=playClicked)
        playbtn.pack()

        titleFrame.pack()
        headingFrame.pack()
        player1Frame.pack()
        player2Frame.pack()
        playFrame.pack()

        self.window.mainloop()

    def initGame(self):
        self.player1 = Player(self.player1_agent.get(), self.player1_name.get())
        self.player2 = Player(self.player2_agent.get(), self.player2_name.get())
        self.game = Game(self.player1, self.player2)

        self.gameScreen()

    def gameScreen(self):
        self.clearScreen(self.window)

        gameFrame = tk.Frame(self.window)
        gameFrame.pack()

        buttonFrame = tk.Frame(gameFrame)
        buttonFrame.pack()

        # Create buttons for each column
        self.move_buttons = []
        for col in range(7):
            button = tk.Button(buttonFrame, text="Drop", command=lambda c=col: self.make_move(c))
            button.grid(row=0, column=col, padx=5, pady=5)
            self.move_buttons.append(button)

        self.board = tk.Canvas(gameFrame, width=280, height=240)
        self.board.pack()

        self.updateGameScreen(self.game.gameBoard, self.board)

        self.status_label = tk.Label(gameFrame, text=f"{self.game.whoIsPlaying().name}'s turn")
        self.status_label.pack()

    def make_move(self, column):
        if self.game.checkMoveLegal(column):
            self.game.makeMove(column)
            self.updateGameScreen(self.game.gameBoard, self.board)

            if self.game.isGameWon:
                self.status_label.config(text=f"{self.game.whoIsPlaying().name} wins!")
                self.disable_buttons()
            elif self.game.turnsTaken == 42:
                self.status_label.config(text="It's a draw!")
                self.disable_buttons()
            else:
                self.status_label.config(text=f"{self.game.whoIsPlaying().name}'s turn")

    @staticmethod
    def updateGameScreen(gameBoardIn, background: tk.Canvas):
        gameBoard = gameBoardIn
        background.delete("all")
        background.create_rectangle(0, 0, 280, 240, fill="blue")

        for row in range(6):
            for col in range(7):
                x1 = col * 40 + 5
                y1 = (5 - row) * 40 + 5
                x2 = x1 + 30
                y2 = y1 + 30

                if gameBoard[row][col] == 0:
                    color = "white"
                elif gameBoard[row][col] == 1:
                    color = "yellow"
                else:
                    color = "red"

                background.create_oval(x1, y1, x2, y2, fill=color, outline="black")

    def disable_buttons(self):
        for button in self.move_buttons:
            button.config(state="disabled")


    def clearScreen(self, screen: tk.Tk):
        for child in screen.winfo_children():
            child.destroy()


if __name__ == '__main__':
    player1 = Player(UserAgent("p1"), "p1")
    player2 = Player(UserAgent("p2"), "p2")
    newGame = Game(player1, player2)

    guiRun = Gui()
    guiRun.startGame()