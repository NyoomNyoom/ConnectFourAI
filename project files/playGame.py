from gui import Gui

from settings import Settings

gameSettings = Settings()

if gameSettings.gameType == "cli":
    pass
elif gameSettings.gameType == "gui":
    game = Gui()
    game.startGame()

