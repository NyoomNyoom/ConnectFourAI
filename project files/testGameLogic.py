import unittest
from connectFourGame import Game
from connectFourGame import Player


class TestGameLogic(unittest.TestCase):

    # Testing methods for whoIsPlaying method.
    # Checks if method correctly reports Player 1 is playing.
    def test_whoIsPlayingP1(self):
        newGame = Game(Player("p1"), Player("p2"))

        self.assertEqual(newGame.whoIsPlaying(), "Player 1", "Returned that player 2 is playing.")

    # Checks if method correctly reports player 2 is playing.
    def test_whoIsPlayingP2(self):
        newGame = Game(Player("p1"), Player("p2"))
        newGame.isPlayer1 = False

        self.assertEqual(newGame.whoIsPlaying(), "Player 2", "Returned that player 1 is playing.")

    # Testing methods for the legal move checker.

    # Checks on empty board.
    def test_moveCheckerEmpty(self):
        player1 = Player("agent")
        player2 = Player("agent")
        newGame = Game(player1, player2)

        self.assertEqual(newGame.checkMoveLegal(0), True, "Checker assumes legal move is illegal")

    # Checks on the last row of a column.
    def test_moveCheckerLastRow(self):
        player1 = Player("agent")
        player2 = Player("agent")
        newGame = Game(player1, player2)
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
        player1 = Player("agent")
        player2 = Player("agent")
        newGame = Game(player1, player2)
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
        player1 = Player("agent")
        player2 = Player("agent")
        newGame = Game(player1, player2)
        newGame.gameBoard = [
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0]]

        self.assertEqual(newGame.checkMoveLegal(6), True, "Checker assumes legal move is illegal")

    # Testing methods for makeMove. I will not be adding a testing method for illegal
    # moves as with the way I am developing the code,they will not be making "no moves" / using the wrong counter etc.   

    # Tests if the method can make a move on an empty board.
    def test_makeMoveEmtpy(self):
        player1 = Player("agent")
        player2 = Player("agent")
        newGame = Game(player1, player2)
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
    def test_makeMoveLastRow(self):
        player1 = Player("agent")
        player2 = Player("agent")
        newGame = Game(player1, player2)
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
        player1 = Player("agent")
        player2 = Player("agent")
        newGame = Game(player1, player2)
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
        player1 = Player("agent")
        player2 = Player("agent")
        newGame = Game(player1, player2)
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
        player1 = Player("agent")
        player2 = Player("agent")
        newGame = Game(player1, player2)
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
        player1 = Player("agent")
        player2 = Player("agent")
        newGame = Game(player1, player2)
        newGame.gameBoard = [
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]

        self.assertEqual(newGame.checkUpDown(1), True, "Cant find a vertical winning combination on the game board.")

    def test_checkUpDownNoWinningCombo(self):
        player1 = Player("agent")
        player2 = Player("agent")
        newGame = Game(player1, player2)
        newGame.gameBoard = [
            [0, 1, 2, 2, 2, 1, 1],
            [0, 2, 1, 1, 2, 2, 1],
            [0, 0, 0, 2, 1, 1, 1],
            [0, 0, 0, 1, 1, 2, 2],
            [0, 0, 0, 2, 0, 2, 1],
            [0, 0, 0, 0, 0, 2, 1]]
        
        self.assertEqual(newGame.checkUpDown(1), False, "Found a winning combination when there shouldn't be one.")

    # Unit tests for checkLeftRight method.

    # Testing a winning combination in the first row.
    def test_checkLeftRightFirstRow(self):
        player1 = Player("agent")
        player2 = Player("agent")
        newGame = Game(player1, player2)
        newGame.gameBoard = [
            [1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]

        self.assertEqual(newGame.checkLeftRight(1), True, "Cant find a horizontal winning combination on the board.")

    # Testing a winning combination for the last row.
    def test_checkLeftRightLastRow(self):
        player1 = Player("agent")
        player2 = Player("agent")
        newGame = Game(player1, player2)
        newGame.gameBoard = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1]]

        self.assertEqual(newGame.checkLeftRight(1), True, "Cant find a horizontal winning combination on the board.")
    
    def test_checkLeftRightNoWin(self):
        player1 = Player("agent")
        player2 = Player("agent")
        newGame = Game(player1, player2)

        newGame.gameBoard = [
            [0, 1, 2, 2, 2, 1, 1],
            [0, 2, 1, 1, 2, 2, 1],
            [0, 0, 0, 2, 1, 1, 1],
            [0, 0, 0, 1, 1, 2, 2],
            [0, 0, 0, 2, 0, 2, 1],
            [0, 0, 0, 0, 0, 2, 1]]
        
        self.assertEqual(newGame.checkLeftRight(1), False, "Found a winning combination when there shouldn't be one.")
    
    # Unit tests for checkNESW method (/ diagonal).

    # Testing the checkNESW method on the first diagonal.
    def test_checkNESWFirstDiagonal(self):
        player1 = Player("agent")
        player2 = Player("agent")
        newGame = Game(player1, player2)
        newGame.gameBoard = [
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]
        
        self.assertEqual(newGame.checkNESW(1), True, "Can't find a diagonal win condition.")

    # Testing the checkNESW method on the last diagonal
    def test_checkNESWLastDiagonal(self):
        player1 = Player("agent")
        player2 = Player("agent")
        newGame = Game(player1, player2)
        newGame.gameBoard = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 0]]
        
        self.assertEqual(newGame.checkNESW(1), True, "Can't find a diagonal win condition")

    # Testing the code on a non-winning combination
    def test_checkNESWNoWin(self):
        player1 = Player("agent")
        player2 = Player("agent")
        newGame = Game(player1, player2)
        newGame.gameBoard = [
            [1, 1, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 1, 1, 1]]

        self.assertEqual(newGame.checkNESW(1), False, "Found a winning combination on a board that doesn't contain one")

    # Unit tests for checkNWSE diagonal (\)

    # Testing the checkNWSE method on a winning combination on the first diagonal.
    def test_checkNWSEFirstDiagonal(self):
        player1 = Player("agent")
        player2 = Player("agent")
        newGame = Game(player1, player2)
        newGame.gameBoard = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0]]
        
        self.assertEqual(newGame.checkNWSE(1), True, "Can't find a winning combination.")
    
    # Testing the checkNWSE method on a winning combination on the last diagonal.
    def test_checkNWSELastDiagonal(self):
        player1 = Player("agent")
        player2 = Player("agent")
        newGame = Game(player1, player2)
        newGame.gameBoard = [
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]
        
        self.assertEqual(newGame.checkNWSE(1), True, "Can't find a winning combination.")

    # Testing the checkNWSE method on a losing combination.
    def test_checkNWSENoWin(self):
        player1 = Player("agent")
        player2 = Player("agent")
        newGame = Game(player1, player2)
        newGame.gameBoard = [
            [0, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0]]

        self.assertEqual(newGame.checkNWSE(1), False, "Found a winning combination.")
        