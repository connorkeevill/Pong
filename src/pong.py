import sys
import pygame

from pygame.locals import *

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
grey = (162, 153, 145)
darkGrey = (62, 53, 45)

# IMPROVE: Use a class and draw these instead of using images
ball = pygame.image.load("images/Pong ball.png")
paddle1 = pygame.image.load("images/Pong Paddle.png")
paddle2 = pygame.image.load("images/Pong Paddle.png")

# | Set size for display
dispWidth = 1366
dispHeight = 700

# | Initial position for the ball
ballx = dispWidth / 2
bally = dispHeight / 2

# | Create the display
setDisplay = pygame.display.set_mode((dispWidth, dispHeight))

# | Initial heights for the paddles
paddle1y = 300
paddle2y = 300

# Screen Text:

# IMPROVE: These are the same

leftScoreFont = pygame.font.Font("freesansbold.ttf", 120)
rightScoreFont = pygame.font.Font("freesansbold.ttf", 120)

# IMPROVE: Make this more dynamic; don't hard code each score but concatenate the integer to the string

# Left Scores
leftScoreText0 = leftScoreFont.render("0", True, white)
leftScoreText1 = leftScoreFont.render("1", True, white)
leftScoreText2 = leftScoreFont.render("2", True, white)
leftScoreText3 = leftScoreFont.render("3", True, white)
leftScoreText4 = leftScoreFont.render("4", True, white)
leftScoreText5 = leftScoreFont.render("5", True, white)
leftScoreText6 = leftScoreFont.render("6", True, white)
leftScoreText7 = leftScoreFont.render("7", True, white)
leftScoreText8 = leftScoreFont.render("8", True, white)
leftScoreText9 = leftScoreFont.render("9", True, white)
leftScoreText10 = leftScoreFont.render("10", True, white)
# Right Scores
rightScoreText0 = rightScoreFont.render("0", True, white)
rightScoreText1 = rightScoreFont.render("1", True, white)
rightScoreText2 = rightScoreFont.render("2", True, white)
rightScoreText3 = rightScoreFont.render("3", True, white)
rightScoreText4 = rightScoreFont.render("4", True, white)
rightScoreText5 = rightScoreFont.render("5", True, white)
rightScoreText6 = rightScoreFont.render("6", True, white)
rightScoreText7 = rightScoreFont.render("7", True, white)
rightScoreText8 = rightScoreFont.render("8", True, white)
rightScoreText9 = rightScoreFont.render("9", True, white)
rightScoreText10 = rightScoreFont.render("10", True, white)

playFont = pygame.font.Font("freesansbold.ttf", 140)
pongFont = pygame.font.Font("freesansbold.ttf", 150)

playText = playFont.render("Play", True, white)
pongText = pongFont.render("Pong", True, white)

# IMPROVE: Use meaningful values, not just arbitrary numbers
playBox = dispWidth / 2 - 150, dispHeight / 2 + 50
pongBox = dispWidth / 2 - 190, 50

leftScoreBox = 500, 10
rightScoreBox = 800, 10

# IMPROVE: What is this colour even for??
playColour = darkGrey

# IMPROVE: Maybe contain these in a player class or something
leftScore = 0
rightScore = 0

# IMPROVE: Could change this to be a lot better
game = 'Start'

# IMPROVE: What do these do
balldir = 'Left'
Balldir = 'Still'

# IMPROVE: Extract into a file that does this
while True:
    # IMPROVE: With classes
    while game == 'Start':
        mousex, mousey = pygame.mouse.get_pos()
        setDisplay.fill(black)
        pygame.draw.rect(setDisplay, playColour, (dispWidth / 2 - 150, dispHeight / 2 + 55, 305, 145))
        setDisplay.blit(pongText, pongBox)
        setDisplay.blit(playText, playBox)
        pygame.display.flip()

        # IMPROVE: Use events instead, that can check from a button class
        if dispWidth / 2 - 150 < mousex < (dispWidth / 2 - 150) + 305 and dispHeight / 2 + 55 < mousey < (
                dispHeight / 2 + 55) + 145:
            playColour = grey
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    # IMPROVE: Use a new window for this maybe
                    game = 'Play'
        else:
            playColour = darkGrey

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    while game == 'Play':
        # Handling The Scores

        # IMPROVE: Just add one to an integer value
        if leftScore == 0:
            setDisplay.blit(leftScoreText0, leftScoreBox)
        elif leftScore == 1:
            setDisplay.blit(leftScoreText1, leftScoreBox)
        elif leftScore == 2:
            setDisplay.blit(leftScoreText2, leftScoreBox)
        elif leftScore == 3:
            setDisplay.blit(leftScoreText3, leftScoreBox)
        elif leftScore == 4:
            setDisplay.blit(leftScoreText4, leftScoreBox)
        elif leftScore == 5:
            setDisplay.blit(leftScoreText5, leftScoreBox)
        elif leftScore == 6:
            setDisplay.blit(leftScoreText6, leftScoreBox)
        elif leftScore == 7:
            setDisplay.blit(leftScoreText7, leftScoreBox)
        elif leftScore == 8:
            setDisplay.blit(leftScoreText8, leftScoreBox)
        elif leftScore == 9:
            setDisplay.blit(leftScoreText9, leftScoreBox)
        elif leftScore == 10:
            setDisplay.blit(leftScoreText10, leftScoreBox)

        if rightScore == 0:
            setDisplay.blit(rightScoreText0, rightScoreBox)
        elif rightScore == 1:
            setDisplay.blit(rightScoreText1, rightScoreBox)
        elif rightScore == 2:
            setDisplay.blit(rightScoreText2, rightScoreBox)
        elif rightScore == 3:
            setDisplay.blit(rightScoreText3, rightScoreBox)
        elif rightScore == 4:
            setDisplay.blit(rightScoreText4, rightScoreBox)
        elif rightScore == 5:
            setDisplay.blit(rightScoreText5, rightScoreBox)
        elif rightScore == 6:
            setDisplay.blit(rightScoreText6, rightScoreBox)
        elif rightScore == 7:
            setDisplay.blit(rightScoreText7, rightScoreBox)
        elif rightScore == 8:
            setDisplay.blit(rightScoreText8, rightScoreBox)
        elif rightScore == 9:
            setDisplay.blit(rightScoreText9, rightScoreBox)
        elif rightScore == 10:
            setDisplay.blit(rightScoreText10, rightScoreBox)

        leftCentre = paddle1y + 77
        rightCentre = paddle2y + 77
        ballCentre = bally + 27

        pygame.display.flip()
        setDisplay.fill(black)
        setDisplay.blit(paddle1, (100, paddle1y))
        setDisplay.blit(paddle2, (dispWidth - 134, paddle2y))
        setDisplay.blit(ball, (ballx, bally))
        pygame.draw.line(setDisplay, white, (dispWidth / 2, 0), (dispWidth / 2, 700), 4)

        # IMPROVE: Makke this easy to read
        az = pygame.key.get_pressed()
        km = pygame.key.get_pressed()

        # Movement for left hand paddle
        if az[K_a] and paddle1y > 0:
            paddle1y = paddle1y - 3
        if az[K_z] and paddle1y < dispHeight - 154:
            paddle1y = paddle1y + 3

        # Movement for right hand paddle
        if km[K_k] and paddle2y > 0:
            paddle2y = paddle2y - 3
        if km[K_m] and paddle2y < dispHeight - 154:
            paddle2y = paddle2y + 3
        # Movement for the ball

        if ballx < 100 and (paddle1y < bally < (paddle1y + 154) or paddle1y < (bally + 54) < (paddle1y + 154)):
            balldir = 'Right'
        elif ballx > dispWidth - 154 and (
                    paddle2y < bally < (paddle2y + 154) or paddle2y < (bally + 54) < (paddle2y + 154)):
            balldir = 'Left'

        if balldir == 'Left':
            ballx = ballx - 3
        if balldir == 'Right':
            ballx = ballx + 3
        if Balldir == 'Still':
            bally = bally
        if Balldir == 'Up1':
            bally -= 1
            if bally < 0:
                Balldir = 'Down1'
        if Balldir == 'Up2':
            bally -= 2
            if bally < 0:
                Balldir = 'Down2'
        if Balldir == 'Up3':
            bally -= 3
            if bally < 0:
                Balldir = 'Down3'

        if Balldir == 'Down1':
            bally += 1
            if bally + 54 > dispHeight:
                Balldir = 'Up1'
        if Balldir == 'Down2':
            bally += 2
            if bally + 54 > dispHeight:
                Balldir = 'Up2'
        if Balldir == 'Down3':
            bally += 3
            if bally + 54 > dispHeight:
                Balldir = 'Up3'

        if ballx < 97 and balldir == 'Left':
            rightScore += 1
            ballx = dispWidth / 2
            bally = dispHeight / 2
            balldir = 'Right'
            Balldir = 'Still'
        elif ballx > dispWidth - 152 and balldir == 'Right':
            leftScore += 1
            ballx = dispWidth / 2
            bally = dispHeight / 2
            balldir = 'Left'
            Balldir = 'Still'

        if ballx < 110:
            if leftCentre < ballCentre < leftCentre - 20:
                Balldir = 'Still'
            if leftCentre - 20 > ballCentre > leftCentre - 40:
                Balldir = 'Up1'
            if leftCentre - 40 > ballCentre > leftCentre - 60:
                Balldir = 'Up2'
            if leftCentre - 60 > ballCentre > leftCentre - 104:
                Balldir = 'Up3'

            if leftCentre + 20 < ballCentre < leftCentre + 40:
                Balldir = 'Down1'
            if leftCentre + 40 < ballCentre < leftCentre + 60:
                Balldir = 'Down2'
            if leftCentre + 60 < ballCentre < leftCentre + 104:
                Balldir = 'Down3'

        if ballx > (dispWidth - 163):
            if rightCentre < ballCentre < rightCentre - 20:
                Balldir = 'Still'
            if rightCentre - 20 > ballCentre > rightCentre - 40:
                Balldir = 'Up1'
            if rightCentre - 40 > ballCentre > rightCentre - 60:
                Balldir = 'Up2'
            if rightCentre - 60 > ballCentre > rightCentre - 104:
                Balldir = 'Up3'
            if rightCentre + 20 < ballCentre < rightCentre + 40:
                Balldir = 'Down1'
            if rightCentre + 40 < ballCentre < rightCentre + 60:
                Balldir = 'Down2'
            if rightCentre + 60 < ballCentre < rightCentre + 104:
                Balldir = 'Down3'

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
