#CK

import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, xPos, yPos, colour=(255, 255, 255)):
        # | Call __init__() of the Sprite() class to inherit
        pygame.sprite.Sprite.__init__(self)

        # | Create the rect for the ball
        self.rect = pygame.Rect(xPos, yPos, 40, 40)

        self.colour = colour

        # |Position the ball
        self.rect.centerx = xPos
        self.rect.centery = yPos

        self.xVelocity = 8
        self.yVelocity = 0

    # | draw()
    # |------------------
    # | Draws the ball
    # |-----------
    def draw(self, surface):
        pygame.draw.rect(surface, self.colour, self.rect)

    # | move()
    # |--------------------------------------------------
    # | Applies the ball's velocities to move the ball
    # |--------------------------------------------
    def move(self):
        self.rect.centerx += self.xVelocity
        self.rect.centery += self.yVelocity

    # | changeDirectionX()
    # |---------------------------------------------
    # | Changes the direction of the ball in the
    # | x-axis by changing the sign of the
    # | velocity. Allows the ball to
    # | 'bounce' off collisions
    # |-------------------
    def changeDirectionX(self):
        self.xVelocity *= -1

    # | changeDirectionY()
    # |---------------------------------------------
    # | Changes the direction of the ball in the
    # | y-axis by changing the sign off the
    # | velocity. Allows the ball to
    # | 'bounce' off collisions
    # |---------------------
    def changeDirectionY(self):
        self.yVelocity *= -1

    # | setYVelocity()
    # |--------------------------------------------------------------
    # | Takes a gradient for the ball to follow as input, and then,
    # | using the ball's xVelocity, scales the gradient into
    # | the yVelocity which will cause the ball to
    # | move with the same gradient passed
    # |-------------------------------
    def setYVelocity(self, gradient):
        # | Using the absolute value of the xVelocity to prevent negative values flipping the direction of motion
        newVelocity = gradient * abs(self.xVelocity)
        self.yVelocity = newVelocity