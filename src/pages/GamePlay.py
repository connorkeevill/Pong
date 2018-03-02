#CK

import pygame
import Helpers
from sprites.Paddle import Paddle
from sprites.Ball import Ball
from resources import colours
from pages.Page import Page
from objects.Title import Title
from objects.Player import Player

class GamePlay(Page):
    def __init__(self, surface):
        # | Call the superclass __init__() method
        Page.__init__(self, surface)

        # | Create the ball and paddles
        self.ball = Ball(450, 100, colours.white)
        self.leftPaddle = Paddle(100, 100, colours.white)
        self.rightPaddle = Paddle(800, 100, colours.white)

        # | Create the titles
        self.leftTitle = Title(10, 10, "0", 32, colours.white)
        self.rightTitle = Title(570, 10, "0", 32, colours.white)

        # | Create the players
        self.leftPlayer = Player(self.leftPaddle, self.leftTitle)
        self.rightPlayer = Player(self.rightPaddle, self.rightTitle)

        # | Integer to keep track of the number of keys that are being pressed, to indicate
        # | whether or not the paddles need to be moves - helps to improve performance.
        self.keysPressed = 0

        self.addToObjects([self.ball, self.leftPaddle, self.rightPaddle, self.leftTitle, self.rightTitle])

    # | update()
    # |--------------------------------------------------
    # | Code to update the page. Essentially code that
    # | is neither drawing the page, or handling
    # | events, but code that still needs to
    # | be ran each loop of the game
    # |------------------------
    def update(self):
        self.manageBounces()

        if self.ballPastEdges():
            self.ball.rect.centerx = Helpers.midpoint(0, self.surface.get_width())

        # | If any keys are pressed, check if the paddles need to move
        if not self.keysPressed == 0:
            self.movePaddles()

        self.ball.move()

    # | manageBounces()
    # |-----------------------------------------------------
    # | Manages collisions for the ball to allow "bounces"
    # |------------------------------------------------
    def manageBounces(self):
        # | Paddle bounces
        if self.ballHasBouncedOnPaddle():
            self.bounceBallOffPaddle()

        # | Boundary bounces
        self.bounceBallOffBoarder()

    # | movePaddles()
    # |-----------------------------------------------------
    # | Gets the keys that are currently being pressed by
    # | the user(s) and uses them to determine whether
    # | either of the paddles need to move or not
    # |-------------------------------------
    def movePaddles(self):
        keys = pygame.key.get_pressed()

        # | Movement for the left player
        if keys[pygame.K_a] and not self.paddleHasHitTop(self.leftPlayer.paddle):
            self.leftPlayer.movePaddleUp()
        if keys[pygame.K_z] and not self.paddleHasHitBottom(self.leftPlayer.paddle):
            self.leftPlayer.movePaddleDown()

        # | Movement for the right player
        if keys[pygame.K_k] and not self.paddleHasHitTop(self.rightPlayer.paddle):
            self.rightPlayer.movePaddleUp()
        if keys[pygame.K_m] and not self.paddleHasHitBottom(self.rightPlayer.paddle):
            self.rightPlayer.movePaddleDown()

    # | paddleHasHitBottom()
    # |---------------------------------------------
    # | Returns true if the passed paddle has made
    # | contact with the bottom of the window
    # |----------------------------------
    def paddleHasHitBottom(self, paddle):
        return paddle.rect.bottom >= self.surface.get_height()

    # | paddleHasHitTop()
    # |----------------------------------------------
    # | Returns true if the passed paddle has made
    # | contact with the top of the window
    # |------------------------------
    def paddleHasHitTop(self, paddle):
        return paddle.rect.top <= 0

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
    # |------------------------------------------------------------------------
    # | Determines whether the ball has collided (hence bounce) with a paddle
    # |-------------------------------------------------------------------
    def ballHasBouncedOnPaddle(self):
        return self.ball.rect.colliderect(self.rightPaddle.rect) or self.ball.rect.colliderect(self.leftPaddle.rect)

    # | bounceBallOffPaddle()
    # |-----------------------------------------------------------------
    # | Calculates the angle at which the ball should leave the paddle,
    # | and changes the lateral direction of ball motion to bounce
    # |-------------------------------------------------------
    def bounceBallOffPaddle(self):
        # | Change the ball's lateral direction of motion
        self.setBallDirection()

        # | Variable to store a reference to the paddle that the ball hit
        collidedPaddle = None

        # | Because this is only going to be called when a collision has occurred, I can check
        # | which paddle collided with the ball just by seeing which side of the screen
        # | the ball's on - saving the processing time of another collision check
        if self.ball.rect.centerx < Helpers.midpoint(0, self.surface.get_width()):
            collidedPaddle = self.leftPaddle
        elif self.ball.rect.centerx > Helpers.midpoint(0, self.surface.get_width()):
            collidedPaddle = self.rightPaddle

        # | Define the length of two of the sides of the triangle that'll be used
        # | to calculate the gradient of the ball when leaving the paddle
        displacementFromPaddleCentre = self.ball.rect.centery - collidedPaddle.rect.centery
        aimingDistance = collidedPaddle.rect.height // 2

        # | Calculate the gradient using "rise over run"
        gradient = (displacementFromPaddleCentre / aimingDistance)

        # | Sets the angle that the ball leaves the paddle with
        self.ball.setYVelocity(gradient)

    def setBallDirection(self):
        # | Because this method will only be called when a collision has occured with a paddle, we can just check one side
        ballCollidedWithLeftPaddle = self.ball.rect.centerx < Helpers.midpoint(0, self.surface.get_width())

        # | If the ball hit the left paddle, bounce right
        if ballCollidedWithLeftPaddle:
            self.ball.setHorizontalDirectionRight()
        # | Otherwise, bounce left
        else:
            self.ball.setHorizontalDirectionLeft()

    # | bounceBallOffBoarder()
    # |-------------------------------------------------
    # | Bounces checks for a collision between the ball
    # | and the upper and lower boarders of the game
    # | and changes the ball's vertical direction
    # | to make the ball bounce off the boarder
    # |--------------------------------------
    def bounceBallOffBoarder(self):
        ballHasCollidedWithTop = self.ball.rect.top <= 0
        ballHasCollidedWithBottom = self.ball.rect.bottom >= self.surface.get_height()

        if ballHasCollidedWithTop:
            self.ball.setVerticalDirectionDown()
        elif ballHasCollidedWithBottom:
            self.ball.setVerticalDirectionUp()

    # | ballPastEdges()
    # |------------------------------------------------------------------
    # | Determines whether the ball has left the horizontal bounds of
    # | the screen, to facilitate scoring, and putting the ball
    # | back into the centre of the screen after leaving
    # |---------------------------------------------
    def ballPastEdges(self):
        return self.ball.rect.right < 0 or self.ball.rect.left > self.surface.get_width()

    # | ballBounceOnBoarders()
    # |-----------------------------------------------------------------------
    # | Determines whether the ball is in contact with either the top of the
    # | bottom of the display, allowing it to "bounce" within the bounds
    # |------------------------------------------------------------
    def ballHasBouncedOnBoarders(self):
        return self.ball.rect.top <= 0 or self.ball.rect.bottom >= self.surface.get_height()