__author__ = "@NyoomNyoom"
__email__ = "jacksonnorth1275@gmail.com"
__version__ = 1.0


class Player:
    def __init__(self, playerNum, agent):
        if playerNum == 1:
            self.playerColour = "blue"
        else:
            self.playerColour = "red"
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

    def checkNorth(self, playerCounter):
        pass

    def checkSouth(self, playerCounter):
        pass

    def checkWest(self, playerCounter):
        pass

    def checkEast(self, playerCounter):
        pass

    def checkNorthEast(self, playerCounter):
        pass

    def checkNorthWest(self, playerCounter):
        pass

    def checkSouthEast(self, playerCounter):
        pass

    def checkSouthWest(self, playerCounter):
        pass

