#CK

from objects.Player import Player
import pygame


class HumanPlayer(Player):

    def __init__(self, paddle, scoreTitle, upKey, downKey):
        Player.__init__(self, paddle, scoreTitle)
        self.upKey = upKey
        self.downKey = downKey

    def movePaddle(self):
        keys = pygame.key.get_pressed()

        if keys[self.upKey]:
            self.movePaddleUp()
        if keys[self.downKey]:
            self.movePaddleDown()

