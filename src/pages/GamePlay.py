#CK

import pygame

from sprites.Paddle import Paddle
from sprites.Ball import Ball

from resources import colours

class GamePlay():
    def __init__(self, surface):
        self.surface = surface

        self.ball = Ball(450, 100, colours.white)

        self.leftPaddle = Paddle(100, 100, colours.white)
        self.rightPaddle = Paddle(800, 100, colours.white)

        self.sprites = pygame.sprite.Group()

        self.sprites.add(self.ball, self.leftPaddle, self.rightPaddle)

    # | draw()
    # |-----------------------------------------------
    # | Draws all objects on the page to the surface
    # |------------------------------------------
    def draw(self):
        self.sprites.draw(self.surface)

    # | handleEvent()
    # |---------------------------------------------------------------------
    # | Takes an event to determine what action can be taken to handle it
    # |---------------------------------------------------------------
    def handleEvent(self, event):
        None
