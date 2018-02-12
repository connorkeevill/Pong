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

        # | Integer to keep track of the number of keys that are being pressed, to indicate
        # | whether or not the paddles need to be moves - helps to improve performance.
        self.keysPressed = 0

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

        if self.ballBounceOnBoarders():
            self.ball.changeDirectionY()

        # | If any keys are pressed, check if the paddles need to move
        if not self.keysPressed == 0:
            self.movePaddles()

        self.ball.move()

    # | movePaddles()
    # |-----------------------------------------------------
    # | Gets the keys that are currently being pressed by
    # | the user(s) and uses them to determine whether
    # | either of the paddles need to move or not
    # |-------------------------------------
    def movePaddles(self):
        keys = pygame.key.get_pressed()

        # | Movement for the right paddle
        if keys[pygame.K_k]:
            self.rightPaddle.moveUp()
        if keys[pygame.K_m]:
            self.rightPaddle.moveDown()
        # | Movement for the left paddle
        if keys[pygame.K_a]:
            self.leftPaddle.moveUp()
        if keys[pygame.K_z]:
            self.leftPaddle.moveDown()

    # | handleEvent()
    # |---------------------------------------------------------------------
    # | Takes an event to determine what action can be taken to handle it
    # |---------------------------------------------------------------
    def handleEvent(self, event):
        action = None
        if event.type == pygame.KEYDOWN:
            self.keysPressed += 1

        if event.type == pygame.KEYUP:
            self.keysPressed -= 1

        return action

    # | ballBounceOnPaddle()
    # |--------------------------------------------------------------------
    # | Determines if the ball has collided (hence bounce) with a paddle
    # |-------------------------------------------------------------
    def ballBounceOnPaddle(self):
        return self.ball.rect.colliderect(self.rightPaddle.rect) or self.ball.rect.colliderect(self.leftPaddle.rect)

    # | ballBounceOnBoarders()
    # |-------------------------------------------------------------------
    # | Determines if the ball is in contact with either the top of the
    # | bottom of the window, and "bounces" the ball off, to keep
    # | within the boundaries that the users are able to see
    # |-------------------------------------------------
    def ballBounceOnBoarders(self):
        return self.ball.rect.top <= 0 or self.ball.rect.bottom >= self.surface.get_height()