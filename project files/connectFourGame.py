__author__ = "@NyoomNyoom"
__email__ = "jacksonnorth1275@gmail.com"
__version__ = 1.0


class Player:
    def __init__(self, agent):
        self.agent = agent
        self.counter = None
        self.name = ""
        self.idName = ""

    #def getMove(self):
    #    move = self.agent.agentFunction()
    #
    #    return move
    
    def setCounter(self, isPlayer1):
        self.counter = (1 if isPlayer1 else 0)
        self.name = ("Player 1" if isPlayer1 else "Player 2")


class Game:

    # The constructor for my game class.
    # Takes in a player class for player 1 and player 2. Initialises variables to default settings. Player 1 always
    # Starts the game.
    def __init__(self, player1: Player, player2: Player):
        # Variables from parameters.
        self.player1 = player1
        self.player2 = player2

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

    def whoIsPlaying(self):
        return self.player1.name if self.isPlayer1 else self.player2.name

    # A method to check if there is a winning combination on the game board.
    def checkWinCon(self, player: Player):
        playerCounter = player.counter

        if self.checkLeftRight(playerCounter):
            return True
        elif self.checkUpDown(playerCounter):
            return True
        elif self.checkNESW(playerCounter):
            return True
        elif self.checkNWSE(playerCounter):
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

    # A method to run the game and enable the user to play against another user.
    def playGame(self):
        gameComplete = False

        print("----------------------------------------------------------------------------------------------")
        print("Welcome to connect four!")
        print()
        self.player1.idName = input("Please enter player 1's name:")
        self.player2.idName = input("Please enter player 2's name:")
        print("----------------------------------------------------------------------------------------------")
        print(f"Thanks {self.player1.idName} and {self.player2.idName}.")
        print("Please read the unstructions below on how to play.")
        print("The game is going to look like: ")
        print("1 2 3 4 5 6 7\n")
        for row in self.gameBoard[::-1]:
            for column in row:
                print(f"{column}", end=" ")
            print()
        print("To make a move, just enter in the number of the column you would like to make a move in.")

        print(f"{self.player1.idName} it is your turn!")
        while(not gameComplete):
            move = input()

            self.checkMoveLegal(move)

    def getMove(self):
        move = int(input())
        move -= 1

        if(self.checkMoveLegal(move)):
            return move
        else:
            print("Whoops! that column might already be full, please choose a different column")
            self.getMove()
