#CK

import pygame
from sprites.Paddle import Paddle
from sprites.Ball import Ball
from resources import colours
from pages.Page import Page

class GamePlay(Page):
    def __init__(self, surface):
        # | Call the superclass __init__() method
        Page.__init__(self, surface)

        # | Create the ball and paddles
        self.ball = Ball(450, 100, colours.white)
        self.leftPaddle = Paddle(100, 100, colours.white)
        self.rightPaddle = Paddle(800, 100, colours.white)

        self.addToObjects([self.ball, self.leftPaddle, self.rightPaddle])

    # | update()
    # |--------------------------------------------------
    # | Code to update the page. Essentially code that
    # | is neither drawing the page, or handling
    # | events, but code that still needs to
    # | be ran each loop of the game
    # |------------------------
    def update(self):
        if self.ballBounceOnPaddle():
            self.ball.changeDirectionX()

        keyPresses = pygame.key.get_pressed()
        if keyPresses[pygame.K_k]:
            self.rightPaddle.moveUp()
        if keyPresses[pygame.K_m]:
            self.rightPaddle.moveDown()

        self.ball.move()

    # | handleEvent()
    # |---------------------------------------------------------------------
    # | Takes an event to determine what action can be taken to handle it
    # |---------------------------------------------------------------
    def handleEvent(self, event):
        action = None



        return action

    # | ballBounce()
    # |--------------------------------------------------------------------
    # | Determines if the ball has collided (hence bounce) with a paddle
    # |-------------------------------------------------------------
    def ballBounceOnPaddle(self):
        return self.ball.rect.colliderect(self.rightPaddle.rect) or self.ball.rect.colliderect(self.leftPaddle.rect)
