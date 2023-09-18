__author__ = "@NyoomNyoom"
__email__ = "jacksonnorth1275@gmail.com"
__version__ = 1.0

class player:

    def __init__(self, playerNum, agent, game):
        if(playerNum == 1):
            self.playerColour = "blue"
        else:
            self.playerColour = "red"
        self.agent = agent
        self.game = game

    def playGame(self):

    def getMove(self):
        move = self.agent.agentFunction()



class game:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        self.turnsTaken = 0

        #The game board, its being treated as a matrix :)
        self.gameBoard = [
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0]
                    ]

    def checkWinCon(self, player):

        if(self.turnsTaken > 7):

            for row in self.gameBoard:
                print(row)
