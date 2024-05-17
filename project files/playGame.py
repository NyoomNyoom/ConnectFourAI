from connectFourGame import Game, Player
from userAgent import UserAgent
from randomAgent import RandomAgent

player1Name = input("Please enter player 1's name: ")

game = Game(Player(UserAgent(player1Name)), Player(RandomAgent()), "cli")
game.playGame()
