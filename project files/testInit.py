import unittest

from connectFourGame import Game
from connectFourGame import Player
from userAgent import UserAgent


class TestGameInit(unittest.TestCase):

    # A method to test if the game board is set up properly
    def test_gameboardINIT(self):
        player1 = Player(UserAgent("p1"), "p1")
        player2 = Player(UserAgent("p2"), "p2")
        newGame = Game(player1, player2)
      
        gameBoardTest = [
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0]]

        self.assertEqual(newGame.gameBoard, gameBoardTest, "Game board not setup properly.")

    # A method to test if player1 is being setup properly
    def test_player1nameINIT(self):
        player1 = Player(UserAgent("p1"), "p1")
        player2 = Player(UserAgent("p2"), "p2")
        newGame = Game(player1, player2)

        self.assertEqual(newGame.player1.name, "Player 1", "Player 1 name not set correctly.")

    # A method to test if player2 is being setup properly
    def test_player2nameINIT(self):
        player1 = Player(UserAgent("p1"), "p1")
        player2 = Player(UserAgent("p2"), "p2")
        newGame = Game(player1, player2)

        self.assertEqual(newGame.player2.name, "Player 2", "Player 2 name not set correctly.")

    # A method to check if turnsTaken is being setup properly
    def test_turnsTakenINIT(self):
        player1 = Player(UserAgent("p1"), "p1")
        player2 = Player(UserAgent("p2"), "p2")
        newGame = Game(player1, player2)

        self.assertEqual(newGame.turnsTaken, 0)

    # A method to check if player 1 is selected at start.
    def test_playerSelection(self):
        player1 = Player(UserAgent("p1"), "p1")
        player2 = Player(UserAgent("p2"), "p2")
        newGame = Game(player1, player2)

        self.assertEqual(newGame.isPlayer1, True, "Player 1 not selected at game start.")


if __name__ == '__main__':
    unittest.main()
