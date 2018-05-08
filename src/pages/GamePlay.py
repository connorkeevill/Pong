#CK

import os
import pygame
import Helpers
import threading
from sprites.Paddle import Paddle
from sprites.Ball import Ball
from objects.Title import Title
from objects.HumanPlayer import HumanPlayer
from objects.ComputerPlayer import ComputerPlayer
from objects.VerticalLine import VerticalLine
from objects.Button import Button
from pages.Page import Page
from resources import colours
from random import uniform

pygame.mixer.init()

currentPath = os.path.dirname(os.path.realpath(__file__))

class GamePlay(Page):
    def __init__(self, surface, playerAmount, AISpeed=-1):
        # | Call the superclass __init__() method
        Page.__init__(self, surface)

        self.bounceSound = pygame.mixer.Sound(os.path.join(currentPath, r"..\resources\ball hit paddle.wav"))
        self.AISpeed = AISpeed

        # | ball
        # |-------
        ballXpos = 450
        ballYpos = Helpers.midpoint(0, self.surface.get_height())
        ballColour = colours.white
        self.ball = Ball(ballXpos, ballYpos, ballColour)

        # | leftPaddle
        # |-------------
        leftPaddleXpos = 50
        leftPaddleYpos = Helpers.midpoint(0, self.surface.get_height())
        leftPaddleColour = colours.white
        leftPaddleWindowHeight = self.surface.get_height()
        self.leftPaddle = Paddle(leftPaddleXpos, leftPaddleYpos, leftPaddleWindowHeight, leftPaddleColour)

        # | rightPaddle
        # |--------------
        rightPaddleXpos = self.surface.get_width() - 50
        rightPaddleYpos = Helpers.midpoint(0, self.surface.get_height())
        rightPaddleColour = colours.white
        rightPaddleWindowHeight = self.surface.get_height()
        self.rightPaddle = Paddle(rightPaddleXpos, rightPaddleYpos, rightPaddleWindowHeight, rightPaddleColour)

        # | leftTitle
        # |------------
        leftTitleXpos = 20
        leftTitleYpos = 20
        leftTitleText = "0"
        leftTitleSize = 45
        leftTitleColour = colours.white
        self.leftTitle = Title(leftTitleXpos, leftTitleYpos, leftTitleText, leftTitleSize, leftTitleColour)

        # | rightTitle
        # |-------------
        rightTitleXpos = self.surface.get_width() - 20
        rightTitleYpos = 20
        rightTitleText = "0"
        rightTitleSize = 45
        rightTitleColour = colours.white
        self.rightTitle = Title(rightTitleXpos, rightTitleYpos, rightTitleText, rightTitleSize, rightTitleColour)

        # | leftPlayer
        # |-------------
        if playerAmount == 1:
            self.leftPlayer = ComputerPlayer(self.leftPaddle, self.leftTitle, self.ball)
            self.leftPlayer.paddle.setVelocity(self.AISpeed)
        elif playerAmount == 2:
            leftPlayerUpKey = pygame.K_a
            leftPlayerDownKey = pygame.K_z
            self.leftPlayer = HumanPlayer(self.leftPaddle, self.leftTitle, leftPlayerUpKey, leftPlayerDownKey)

        # | rightPlayer
        # |--------------
        rightPlayerUpKey = pygame.K_k
        rightPlayerDownKey = pygame.K_m
        self.rightPlayer = HumanPlayer(self.rightPaddle, self.rightTitle, rightPlayerUpKey, rightPlayerDownKey)

        # | verticalLine
        # |---------------
        verticalLineXpos = Helpers.midpoint(0, self.surface.get_width())
        verticalLineStartPoint = 0
        verticalLineEndPoint = self.surface.get_height()
        verticalLineSegmentLength = 20
        verticalLineInterval = 15
        verticalLineColour = colours.white
        self.verticalLine = VerticalLine(verticalLineXpos, verticalLineStartPoint, verticalLineEndPoint,
                                         verticalLineSegmentLength, verticalLineInterval, verticalLineColour)

        # | btnPause
        # |--------------
        btnPauseDimensions = {'width':40, 'height':40}
        btnPauseXpos = self.surface.get_width() / 2
        btnPauseYpos = 30
        btnPauseColour = colours.btnPrimary
        btnPauseHoverColour = colours.btnHover
        btnPauseText = '||'
        btnPauseTextSize = 30
        btnPauseTextColour = colours.btnText
        self.btnPause = Button(btnPauseXpos, btnPauseYpos, btnPauseDimensions, btnPauseColour, btnPauseHoverColour,
                               btnPauseText, btnPauseTextSize, btnPauseTextColour)

        # | Integer to keep track of the number of keys that are being pressed, to indicate
        # | whether or not the paddles need to be moves - helps to improve performance.
        self.keysPressed = 0

        # | The score needed to win
        self.winScore = 10

        # | Flag to indicate if the code needs to check if the ball is on the screen
        self.ballOnScreenNeedsToBeChecked = True

        # | The delay for the ball to be recentred in the screen after leaving (in seconds)
        self.ballCentreTimer = 0.5

        self.addToObjects([self.ball, self.leftPaddle, self.rightPaddle,
                           self.leftTitle, self.rightTitle, self.verticalLine,
                           self.btnPause])

    # | update()
    # |--------------------------------------------------
    # | Code to update the page. Essentially code that
    # | is neither drawing the page, or handling
    # | events, but code that still needs to
    # | be ran each loop of the game
    # |------------------------
    def update(self):
        # | Bounce the ball if necessary
        self.checkForCollisions()

        # | If the ball has moved off the (sides of the) screen, score a player, and put the ball back in the middle
        self.checkBallIsWithinScreen()

        # | If any keys are being pressed check if the paddles need to move
        self.movePlayerPaddles()

        self.ball.move()

    # | handleEvent()
    # |---------------------------------------------------------------------
    # | Takes an event to determine what action can be taken to handle it
    # |---------------------------------------------------------------
    def handleEvent(self, event):
        action = None

        if event.type == pygame.MOUSEMOTION:
            xMouse, yMouse = pygame.mouse.get_pos()
            self.btnPause.hover(xMouse, yMouse)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.btnPause.clicked():
                action = 'Pause'

        return action

    # | checkForCollisions()
    # |--------------------------------------------------------
    # | Checks for collisions for the ball to allow "bounces"
    # |--------------------------------------------------
    def checkForCollisions(self):
        # | Paddle bounces
        if self.ballHasBouncedOnPaddle():
            self.bounceBallOffPaddle()

            # | Play the bounce noise
            self.bounceSound.play()

        # | Boundary bounces
        self.bounceBallOffBoarder()

    # | movePlayerPaddles()
    # |-----------------------------------------------------
    # | Gets the keys that are currently being pressed by
    # | the user(s) and uses them to determine whether
    # | or not either of the paddles need to move
    # |--------------------------------------
    def movePlayerPaddles(self):
        self.rightPlayer.movePaddle()
        self.leftPlayer.movePaddle()

    # | ballBounceOnPaddle()
    # |------------------------------------------------------------------------
    # | Determines whether the ball has collided (hence bounce) with a paddle
    # |-------------------------------------------------------------------
    def ballHasBouncedOnPaddle(self):
        ballHasBouncedOnLeftPaddle = (self.ball.rect.colliderect(self.leftPaddle.rect))
        ballHasBouncedOnRightPaddle = (self.ball.rect.colliderect(self.rightPaddle.rect))
        return ballHasBouncedOnLeftPaddle or ballHasBouncedOnRightPaddle

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

    # | setBallDirection()
    # |---------------------------------------------------------------------
    # | Called after a ball has hit a paddle, this method will determine
    # | which paddle the ball has hit, and use this information to
    # | determine the direction that the ball needs to move in
    # | to allow it to bounce off of the paddle, preventing
    # | the ball from getting "stuck" within the paddle
    # |---------------------------------------------
    def setBallDirection(self):
        # | Because this method will only be called when a collision
        # | has occured with a paddle, we can just check one side
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

    # | checkBallIsWithinScreen()
    # |-------------------------------------------------
    # | Checks if the ball has gone off the edges of
    # | the screen, giving the player the point,
    # | and recentring the ball if it has
    # |-----------------------------
    def checkBallIsWithinScreen(self):
        # | Order of boolean statements is important here for efficiency; having the boolean before the
        # | method can save processing by taking advantage of the "and"'s short circuiting nature
        if self.ballOnScreenNeedsToBeChecked and self.ballPastEdges():
            self.allocatePointToPlayer()
            self.checkForPlayerWin()

            # | Tell the code that it doesn't need to check the ball off the screen
            self.ballOnScreenNeedsToBeChecked = False
            centreBallThread = threading.Timer(self.ballCentreTimer, self.recentreBall)
            centreBallThread.start()

    # | allocatePointToPlayer()
    # |----------------------------------------------------
    # | Determines which side of the screen the ball has
    # | gone off, and allocates a point to the player
    # | that's on the opposite side of the screen
    # |----------------------------------------
    def allocatePointToPlayer(self):
        ballHasGoneOffLeftEdge = self.ball.rect.centerx < 0
        ballHasGoneOffRightEdge = self.ball.rect.centerx > self.surface.get_width()

        if ballHasGoneOffLeftEdge:
            self.rightPlayer.increaseScore()
        elif ballHasGoneOffRightEdge:
            self.leftPlayer.increaseScore()

    # | recentreBall()
    # |----------------------------------------------------------
    # | Puts the ball back into the centre of the screen (after
    # | a player has scored) and gives it a random direction
    # |--------------------------------------------------
    def recentreBall(self):
        self.ball.rect.centerx = Helpers.midpoint(0, self.surface.get_width())
        self.ball.rect.centery = Helpers.midpoint(0, self.surface.get_height())

        newBallGradient = uniform(-0.6, 0.6) # | uniform() generates a random real number within the range [a, b)
        self.ball.setYVelocity(newBallGradient)

        # | Flip the direction of the ball so that it's heading towards the player that just scored
        self.ball.changeDirectionX()

        # | Tell the code that it needs to check the ball's location now that it's on the screen
        self.ballOnScreenNeedsToBeChecked = True

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

    # | checkForPlayerWin()
    # |----------------------------------------
    # | Checks if either player has won, and
    # | shows a message indicating that
    # | the player is the winner
    # |--------------------
    def checkForPlayerWin(self):
        if self.leftPlayer.score == self.winScore: self.showWinMessage(self.leftPlayer)
        elif self.rightPlayer.score == self.winScore: self.showWinMessage(self.rightPlayer)

    # | showWinMessage()
    # |---------------------------------------------------
    # | Immobilises the ball, and creates a title object
    # | (and adds it to the objects list to allow
    # | it to be drawn), essentially bringing
    # | the game to a closing screen.
    # |--------------------------
    def showWinMessage(self, player):
        self.ball.xVelocity = 0
        self.ball.yVelocity = 0
        side = ""

        # | congratulationsTitle
        # |-----------------------
        congratulationsTitleXpos = 0
        if player == self.leftPlayer:
            congratulationsTitleXpos = 1/4 * (self.surface.get_width())
            side = "left"
        elif player == self.rightPlayer:
            congratulationsTitleXpos = 3/4 * (self.surface.get_width())
            side = "right"
        congratulationsTitleLineOneYpos = Helpers.midpoint(0, self.surface.get_height()) - 70
        congratulationsTitleLineTwoYpos = Helpers.midpoint(0, self.surface.get_height()) - 30
        congratulationsTitleLineOneText = "The " + side
        congratulationsTitleLineTwoText = "player won!"
        congratulationsTitleSize = 55
        congratulationsTitleColour = colours.red
        congratulationsTitleLineOne = Title(congratulationsTitleXpos, congratulationsTitleLineOneYpos, congratulationsTitleLineOneText,
                                          congratulationsTitleSize, congratulationsTitleColour)
        congratulationsTitleLineTwo = Title(congratulationsTitleXpos, congratulationsTitleLineTwoYpos,
                                            congratulationsTitleLineTwoText,
                                            congratulationsTitleSize, congratulationsTitleColour)

        self.addToObjects([congratulationsTitleLineOne, congratulationsTitleLineTwo])