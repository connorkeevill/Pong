#CK

from pages.MainMenu import MainMenu
from pages.GamePlay import GamePlay
from pages.Difficulty import Difficulty
from pages.Pause import Pause


class Router:
    def __init__(self, screen):
        self.screen = screen

        self.routes = {"MainMenu": self.createMainMenu,
                       "Difficulty": self.createDifficulty,
                       "OnePlayerGameEasy": self.createOnePlayerEasy,
                       "OnePlayerGameMedium": self.createOnePlayerMedium,
                       "OnePlayerGameHard": self.createOnePlayerHard,
                       "TwoPlayerGame": self.createTwoPlayer,
                       "Pause": self.createPause}

    # | route()
    # |----------------------------------------------------
    # | Returns a new instance of the class relating to
    # | the route that was passed into the method
    # |-------------------------------------
    def route(self, route):
        return self.routes[route]()

    # | createMainMenu()
    # |---------------------------------------
    # | Returns a new instance of MainMenu
    # |-------------------------------
    def createMainMenu(self):
        return MainMenu(self.screen)

    # | createDifficulty()
    # |----------------------------------------
    # | Returns a new instance of Difficulty
    # |---------------------------------
    def createDifficulty(self):
        return Difficulty(self.screen)

    # | createOnePlayerEasy()
    # |-------------------------------------------
    # | Returns a new instance of GamePlayer that
    # | is set for one player, and a slow AI
    # |---------------------------------
    def createOnePlayerEasy(self):
        return GamePlay(self.screen, 1, 5)

    # | createOnePlayerMedium()
    # |--------------------------------------------
    # | Returns a new instance of GamePlayer that
    # | is set for one player, and a medium AI
    # |------------------------------------
    def createOnePlayerMedium(self):
        return GamePlay(self.screen, 1, 8)

    # | createOnePlayerHard()
    # |-------------------------------------------
    # | Returns a new instance of GamePlayer that
    # | is set for one player and a fast AI
    # |-------------------------------
    def createOnePlayerHard(self):
        return GamePlay(self.screen, 1, 10)

    # | createTwoPlayer()
    # |---------------------------------------
    # | Returns a new instance of GamePlayer
    # | that is set for two player mode
    # |---------------------------
    def createTwoPlayer(self):
        return GamePlay(self.screen, 2)

    # | createPause()
    # |----------------------------------
    # | Returns a new instance of Pause
    # |------------------------------
    def createPause(self):
        return Pause(self.screen)