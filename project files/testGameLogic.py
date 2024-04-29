import unittest
from connectFourGame import Game

class TestGameLogic(unittest.TestCase):

    # Testing methods for the legal move checker.

    # Checks on empty board.
    def test_moveCheckerEmpty(self):
        newGame = Game("Player 1", "player 2")

        self.assertEqual(newGame.checkMoveLegal(0), True, "Checker assumes legal move is illegal")

    # Checks on the last row of a column.
    def test_moveCheckerLastRow(self):
        newGame = Game("Player 1", "player 2")
        newGame.gameBoard = [
            [1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]

        self.assertEqual(newGame.checkMoveLegal(0), True, "Checker assumes legal move is illegal")

    # Checks on a full column.
    def test_moveCheckerIllegalMove(self):
        newGame = Game("Player 1", "player 2")
        newGame.gameBoard = [
            [1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0]]

        self.assertEqual(newGame.checkMoveLegal(0), False, "Checker assumes illegal move is legal")

    # Checks the last row of the last column.
    def test_moveCheckerLastRowLastCol(self):
        newGame = Game("Player 1", "player 2")
        newGame.gameBoard = [
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0]]

        self.assertEqual(newGame.checkMoveLegal(6), True, "Checker assumes legal move is illegal")

    # Testing methods for makeMove. I will not be adding a testing method for illegal moves as with the way I am developing the code,

    # Tests if the method can make a move on an empty board.
    def test_makeMoveEmtpy(self):
        newGame = Game("Player 1", "Player 2")
        expectedGameBoard = [
            [1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]

        newGame.makeMove(0)

        self.assertEqual(newGame.gameBoard, expectedGameBoard, "The game boards do not match.")

    # Tests if the method can make a move on the last row of a column.
    def test_makeMoveEmtpy(self):
        newGame = Game("Player 1", "Player 2")
        expectedGameBoard = [
            [1, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0]]

        newGame.gameBoard = [
            [1, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]

        newGame.makeMove(0)

        self.assertEqual(newGame.gameBoard, expectedGameBoard, "The game boards do not match.")

    # Checks if the method can make a move as player 2.
    def test_makeMovePlayer2(self):
        newGame = Game("Player 1", "Player 2")
        expectedGameBoard = [
            [2, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]

        newGame.isPlayer1 = False
        newGame.makeMove(0)

        self.assertEqual(newGame.gameBoard, expectedGameBoard, "The game boards do not match.")

    # Checks if the method can make a move in the last row.
    def test_makeMoveLastCol(self):
        newGame = Game("Player 1", "Player 2")
        expectedGameBoard = [
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]

        newGame.makeMove(6)

        self.assertEqual(newGame.gameBoard, expectedGameBoard, "The game boards do not match.")

    # Unit tests for the checkUpDown Method.

    # Testing a winning combination in the first column.
    def test_checkUpDownFirstCol(self):
        newGame = Game("Player 1", "Player 2")
        newGame.gameBoard = [
            [1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]

        self.assertEqual(newGame.checkUpDown(1), True, "Can't find a vertical winning combination on the game board.")

    # Testing a winning combination in the last column.
    def test_checkUpDownLastCol(self):
        newGame = Game("Player 1", "Player 2")
        newGame.gameBoard = [
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]

        self.assertEqual(newGame.checkUpDown(1), True, "Cant find a vertical winning combination on the game board.")
