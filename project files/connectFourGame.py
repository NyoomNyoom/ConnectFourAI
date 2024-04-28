__author__ = "@NyoomNyoom"
__email__ = "jacksonnorth1275@gmail.com"
__version__ = 1.0


class Player:
    def __init__(self, agent):
        self.agent = agent

    def playGame(self):
        pass

    def getMove(self):
        move = self.agent.agentFunction()

        return move


class Game:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.isPlayer1 = True

        self.turnsTaken = 0

        # The game board, its being treated as a matrix :)
        self.gameBoard = [
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0]
                    ]

    def checkWinCon(self, player):
        pass

    # Checks if the move is legal, if not.
    def checkMoveLegal(self, column):
        validMove = False
        rowNum = 0

        # Check where the puck can be played in that column
        while rowNum <= 5:
            if self.gameBoard[rowNum][column] == 1 or self.gameBoard[rowNum][column] == 2:
                rowNum += 1
            else:
                validMove = True
                break
        return validMove

    # Makes the move in the given row.
    def makeMove(self, player):
        column = player.getMove()
        rowNum = 0

        if self.checkMoveLegal(column):
            if self.isPlayer1:
                self.gameBoard[rowNum][column] = 1
                self.isPlayer1 = False
            else:
                self.gameBoard[rowNum][column] = 2
                self.isPlayer1 = True
        else:
            self.makeMove(player)

    # A method to check if the there is four counters straight up or down.
    def checkUpDown(self, playerCounter):
        for rowNum in range(3):
            for colNum in range(6):
                if self.gameBoard[rowNum][colNum] == playerCounter:
                    # Checking the furthest counter first (in an effort to reduce comparisons).
                    if self.gameBoard[rowNum+3][colNum] == playerCounter:
                        if self.gameBoard[rowNum + 2][colNum] == playerCounter:
                            if self.gameBoard[rowNum + 1][colNum] == playerCounter:
                                return True
        return False  # runs if one if statement fails.

    def checkLeftRight(self, playerCounter):
        for rowNum in range(5):
            for colNum in range(4):
                if self.gameBoard[rowNum][colNum] == playerCounter:
                    if self.gameBoard[rowNum][colNum + 3] == playerCounter:
                        if self.gameBoard[rowNum][colNum + 2] == playerCounter:
                            if self.gameBoard[rowNum][colNum + 1] == playerCounter:
                                return True
        return False

    # A method to check the diagonal North east South west (/)
    def checkNESW(self, playerCounter):
        for rowNum in range(3,6):
            for colNum in range(5):
                if self.gameBoard[rowNum][colNum] == playerCounter:
                    if self.gameBoard[rowNum - 3][colNum + 3] == playerCounter:
                        if self.gameBoard[rowNum - 2][colNum + 2] == playerCounter:
                            if self.gameBoard[rowNum - 1][colNum + 1] == playerCounter:
                                return True
        return False

    # A method to check the diagonal North west South East (\)
    def checkNWSE(self, playerCounter):
        pass


