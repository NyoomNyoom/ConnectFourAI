from connectFourGame import Game, Player
from userAgent import UserAgent

player1Name = input("Please enter player 1's name: ")
player2Name = input("Please enter player 2's name: ")

game = Game(Player(UserAgent(player1Name)), Player(UserAgent(player2Name)))
game.playGame()
