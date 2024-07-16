from connectFourGame import Game, Player


class Cli:
    def __init__(self):
        player1: Player
        player2: Player
        print("----------------------------------------------------------------------------------------------")
        print("Welcome to connect four!")
        print("----------------------------------------------------------------------------------------------")
        print("Please enter player 1's name!")

    def getMove(self, moveIn):
        if self.checkMoveLegal(moveIn):
            return moveIn
        else:
            print("Whoops! that column is already full, please choose a different column")
            self.printGameBoard()
            return self.getMove(int(input("Please enter a new column to play a counter in.")) - 1)

    # A method to print the game board.
    def printGameBoard(self):
        print("1 2 3 4 5 6 7\n")
        for row in self.gameBoard[::-1]:
            for column in row:
                print(f"{column}", end=" ")
            print()

    def commandLineGame(self):
        gameComplete = False

        print(f"Thanks {self.player1.idName} and {self.player2.idName}.")
        print("Please read the instructions below on how to play.")
        print("The game is going to look like: ")

        self.printGameBoard()

        print("To make a move, just enter in the number of the column you would like to make a move in.")

        while not gameComplete:
            self.printGameBoard()
            move = self.moveHandler(self.whoIsPlaying().getMove(), False)
            currPlayer: Player = self.player1 if self.isPlayer1 else self.player2
            self.makeMove(move)

            if self.turnsTaken >= 7:
                if self.checkWinCon(currPlayer):
                    print(f"Well done {currPlayer.idName}!!! You have won the game!")
                    gameComplete = True
                else:  # If the game is not won.
                    self.turnsTaken += 1
            else:  # if turns taken is less than 7.
                self.turnsTaken += 1
            print(f"{currPlayer.idName} it is your turn.")

        self.printGameBoard()
        print(f"Thanks for playing {self.player1.idName} and {self.player2.idName}!")
        print("If you would like to play again, please run the program again :)")


    # A method to get the move from a user recursively.
    def moveHandler(self, moveIn, tryAgain):
        if self.checkMoveLegal(moveIn):
            return moveIn
        else:
            print("Whoops! that column is already full, please choose a different column")
            self.printGameBoard()
            return self.moveHandler(self.whoIsPlaying().getMove(), False)