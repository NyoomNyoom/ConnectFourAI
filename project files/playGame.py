from connectFourGame import Game, Player
from userAgent import UserAgent
from randomAgent import RandomAgent

game = Game(Player(UserAgent("Jackson")), Player(RandomAgent()))
game.playGame()
