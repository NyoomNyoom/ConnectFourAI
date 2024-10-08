__author__ = "@NyoomNyoom"
__email__ = "jacksonnorth1275@gmail.com"
__version__ = 1.0

from settings import Settings


class Player:
    def __init__(self, agent, name):
        self.agent = agent
        self.counter = None
        self.name = ""
        self.playerName = name

    def getMove(self):
        move = self.agent.agentFunction()

        return move
    
    def setCounter(self, isPlayer1):
        self.counter = (1 if isPlayer1 else 2)
        self.name = ("Player 1" if isPlayer1 else "Player 2")


class Game:

    # The constructor for my game class.
    # Takes in a player class for player 1 and player 2. Initialises variables to default settings. Player 1 always
    # Starts the game.
    def __init__(self, player1: Player, player2: Player):
        # Variables from parameters.
        self.player1: Player = player1
        self.player2: Player = player2

        # Variables with default values each time.
        self.isPlayer1 = True
        self.turnsTaken = 0
        self.gameBoard = [  # The game board, which is being treated as a matrix :)
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0]]
        
        # Sets the counter for player 1 and 2 and also sets their name.
        self.player1.setCounter(True)
        self.player2.setCounter(False)
        self.isGameWon = False

    def whoIsPlaying(self):
        """
        A method to determine which players turn it is.
        :return: the Player object of who is playing.
        """
        return self.player1 if self.isPlayer1 else self.player2

    # A method to check if there is a winning combination on the game board.
    def checkWinCon(self, player: Player):
        playerCounter = player.counter

        if self.checkLeftRight(playerCounter):
            self.isGameWon = True
            return True
        elif self.checkUpDown(playerCounter):
            self.isGameWon = True
            return True
        elif self.checkNESW(playerCounter):
            self.isGameWon = True
            return True
        elif self.checkNWSE(playerCounter):
            self.isGameWon = True
            return True
        else:
            return False

    # Checks if the move is legal, returns true if the move is legal, returns false if not.
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

    # Makes the move in the given column if the move is legal. If the move is not legal, recursively call the makeMove
    # method.
    def makeMove(self, columnIn):
        column = columnIn
        rowNum = 0

        while rowNum <= 5:
            if self.gameBoard[rowNum][column] == 1 or self.gameBoard[rowNum][column] == 2:
                rowNum += 1
            else:
                break

        if self.isPlayer1:
            self.gameBoard[rowNum][column] = 1
            self.isPlayer1 = False
        else:
            self.gameBoard[rowNum][column] = 2
            self.isPlayer1 = True

    # A method to check if the there is four counters straight up or down.
    def checkUpDown(self, playerCounter):
        for rowNum in range(3):
            for colNum in range(7):
                if self.gameBoard[rowNum][colNum] == playerCounter:
                    # Checking the furthest counter first (in an effort to reduce comparisons).
                    if self.gameBoard[rowNum+3][colNum] == playerCounter:
                        if self.gameBoard[rowNum + 2][colNum] == playerCounter:
                            if self.gameBoard[rowNum + 1][colNum] == playerCounter:
                                return True
        return False  # runs if one if statement fails.

    def checkLeftRight(self, playerCounter):
        for rowNum in range(6):
            for colNum in range(4):
                if self.gameBoard[rowNum][colNum] == playerCounter:
                    if self.gameBoard[rowNum][colNum + 3] == playerCounter:
                        if self.gameBoard[rowNum][colNum + 2] == playerCounter:
                            if self.gameBoard[rowNum][colNum + 1] == playerCounter:
                                return True
        return False

    # A method to check the diagonal North east South west (/)
    def checkNESW(self, playerCounter):
        for rowNum in range(3, 6):
            for colNum in range(4):
                if self.gameBoard[rowNum][colNum] == playerCounter:
                    if self.gameBoard[rowNum - 3][colNum + 3] == playerCounter:
                        if self.gameBoard[rowNum - 2][colNum + 2] == playerCounter:
                            if self.gameBoard[rowNum - 1][colNum + 1] == playerCounter:
                                return True
        return False

    # A method to check the diagonal North west South East (\)
    def checkNWSE(self, playerCounter):
        for rowNum in range(3, 6):
            for colNum in range(3, 7):
                if self.gameBoard[rowNum][colNum] == playerCounter:
                    if self.gameBoard[rowNum - 3][colNum - 3] == playerCounter:
                        if self.gameBoard[rowNum - 2][colNum - 2] == playerCounter:
                            if self.gameBoard[rowNum - 1][colNum - 1] == playerCounter:
                                return True
        return False
