#CK

import pygame

from sprites.Paddle import Paddle
from sprites.Ball import Ball

from resources import colours

class GamePlay():
    def __init__(self, surface):
        self.surface = surface

        # | Create the ball and paddles
        self.ball = Ball(450, 100, colours.white)
        self.leftPaddle = Paddle(100, 100, colours.white)
        self.rightPaddle = Paddle(800, 100, colours.white)

        self.objects = [self.ball, self.leftPaddle, self.rightPaddle]

    # | update()
    # |--------------------------------------------------
    # | Code to update the page. Essentially code that
    # | is neither drawing the page, or handling
    # | events, but code that still needs to
    # | be ran each loop of the game
    # |------------------------
    def update(self):
        if self.ballBounce():
            self.ball.changeDirection()

        self.ball.move()

    # | draw()
    # |-----------------------------------------------
    # | Draws all objects on the page to the surface
    # |------------------------------------------
    def draw(self):
        for object in self.objects:
            object.draw(self.surface)

    # | handleEvent()
    # |---------------------------------------------------------------------
    # | Takes an event to determine what action can be taken to handle it
    # |---------------------------------------------------------------
    def handleEvent(self, event):
        action = None
        # | Insert code here

        return action

    # | ballBounce()
    # |--------------------------------------------------------------------
    # | Determines if the ball has collided (hence bounce) with a paddle
    # |-------------------------------------------------------------
    def ballBounce(self):
        return self.ball.rect.colliderect(self.rightPaddle.rect) or self.ball.rect.colliderect(self.leftPaddle.rect)
