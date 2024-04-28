import unittest

from connectFourGame import Game


class TestGame(unittest.TestCase):
    pass

    # A method to test if the game board is set up properly
    def test_gameboardINIT(self):
        newGame = Game("player 1", "player 2")
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
        newGame = Game("Player 1", "Player 2")

        self.assertEqual(newGame.player1, "Player 1" ,"Player 1 name not set correctly.")

    # A method to test if player2 is being setup properly
    def test_player2nameINIT(self):
        newGame = Game("Player 1", "Player 2")

        self.assertEqual(newGame.player1, "Player 2", "Player 2 name not set correctly.")

    # A method to check if turnsTaken is being setup properly
    def test_turnsTakenINIT(self):
        newGame = Game("Player 1", "Player 2")

        self.assertEqual(newGame.turnsTaken, 0)

    # A method to check if player 1 is selected at start.
    def test_playerSelection(self):
        newGame = Game("Player 1", "Player 2")

        self.assertEqual(newGame.isPlayer1, True, "Player 1 not selected at game start.")


if __name__ == '__main__':
    unittest.main()
