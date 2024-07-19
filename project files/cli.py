from connectFourGame import Game, Player
from userAgent import UserAgent
from randomAgent import RandomAgent


class Cli:
    def __init__(self, game: Game):
        self.player1: Player
        self.player2: Player
        self.game = game

        print("----------------------------------------------------------------------------------------------")
        print("Welcome to connect four!")
        print("----------------------------------------------------------------------------------------------")
        print("Please select the agent for player 1: ")

        valid = False

        while not valid:
            agent1 = input("Enter u for user, r for random")

            if agent1.lower() == "u":
                p1name = input("Player 1 please enter your name: ")
                self.player1 = Player(UserAgent(p1name), p1name)
                valid = True
            elif agent1.lower() == "r":
                p1name = "Random"
                self.player1 = Player(RandomAgent(), p1name)
                valid = True
            else:
                print("Incorrect character entered. Please enter a valid character")

        print("Please select the agent for player 2.")

        valid = False

        while not valid:
            agent2 = input("Enter u for user, r for random")

            if agent2.lower() == "u":
                p2name = input("Player 2 please enter your name: ")
                self.player2 = Player(UserAgent(p2name), p2name)
                valid = True
            elif agent2.lower() == "r":
                self.player2 = Player(RandomAgent(), "Random")
                valid = True
            else:
                print("Incorrect character entered. Please enter a valid character")

    def getMove(self, moveIn):
        if self.game.checkMoveLegal(moveIn):
            return moveIn
        else:
            print("Whoops! that column is already full, please choose a different column")
            self.printGameBoard()
            return self.getMove(int(input("Please enter a new column to play a counter in.")) - 1)

    # A method to print the game board.
    def printGameBoard(self):
        print("1 2 3 4 5 6 7\n")
        for row in self.game.gameBoard[::-1]:
            for column in row:
                print(f"{column}", end=" ")
            print()

    def commandLineGame(self):
        gameComplete = False

        print(f"Thanks {self.player1.playerName} and {self.player2.playerName}.")
        print("Please read the instructions below on how to play.")
        print("The game is going to look like: ")

        self.printGameBoard()

        print("To make a move, just enter in the number of the column you would like to make a move in.")

        while not gameComplete:
            self.printGameBoard()
            move = self.moveHandler(self.game.whoIsPlaying().getMove(), False)
            currPlayer: Player = self.player1 if self.isPlayer1 else self.player2
            self.game.makeMove(move)

            if self.game.turnsTaken >= 7:
                if self.game.checkWinCon(currPlayer):
                    print(f"Well done {currPlayer.playerName}!!! You have won the game!")
                    gameComplete = True
                else:  # If the game is not won.
                    self.game.turnsTaken += 1
            else:  # if turns taken is less than 7.
                self.game.turnsTaken += 1
            print(f"{currPlayer.playerName} it is your turn.")

        self.printGameBoard()
        print(f"Thanks for playing {self.player1.playerName} and {self.player2.playerName}!")
        print("If you would like to play again, please run the program again :)")

    # A method to get the move from a user recursively.
    def moveHandler(self, moveIn, tryAgain):
        if self.game.checkMoveLegal(moveIn):
            return moveIn
        else:
            print("Whoops! that column is already full, please choose a different column")
            self.printGameBoard()
            return self.moveHandler(self.game.whoIsPlaying().getMove(), False)