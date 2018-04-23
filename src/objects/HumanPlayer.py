#CK

from objects.Player import Player
import pygame

# | HumanPlayer()
# |------------------------------------------------------------------
# | The object for a human controlled player. Controls the movement
# | of the player's paddle based off any keyboard input received
# |----------------------------------------------------------
class HumanPlayer(Player):
    # | Call the superclass __init__() method
    def __init__(self, paddle, scoreTitle, upKey, downKey):
        Player.__init__(self, paddle, scoreTitle)
        self.upKey = upKey
        self.downKey = downKey

    # | movePaddle()
    # |----------------------------------------------
    # | Gets the keys pressed and moves the player's
    # | paddle based on the pressed keys, and
    # | this player's controller keys
    # |-------------------------
    def movePaddle(self):
        keys = pygame.key.get_pressed()

        if keys[self.upKey]:
            self.movePaddleUp()
        if keys[self.downKey]:
            self.movePaddleDown()

