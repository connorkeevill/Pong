#CK

import pygame

# | Ball()
# |------------------------------------------------------------
# | Class for the ball which handles its drawing and movement
# |------------------------------------------------------
class Ball(pygame.sprite.Sprite):
    def __init__(self, xPos, yPos, colour=(255, 255, 255)):
        # | Call __init__() of the Sprite() class to inherit
        pygame.sprite.Sprite.__init__(self)

        # | Create the rect for the ball
        self.rect = pygame.Rect(xPos, yPos, 20, 20)

        self.colour = colour

        # |Position the ball
        self.rect.centerx = xPos
        self.rect.centery = yPos

        self.xVelocity = 11
        self.yVelocity = 0

    # | draw()
    # |------------------
    # | Draws the ball
    # |-----------
    def draw(self, surface):
        pygame.draw.circle(surface, self.colour, (self.rect.centerx, self.rect.centery), self.rect.width // 2)

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

    # | setHorizontalDirectionLeft()
    # |----------------------------------------------------
    # | Changes the ball's x velocity so that it's moving
    # | left, providing that it isn't already doing so
    # |---------------------------------------------
    def setHorizontalDirectionLeft(self):
        if self.xVelocity > 0:
            self.changeDirectionX()

    # | setHorizontalDirectionLeftRight()
    # |----------------------------------------------------
    # | Changes the ball's x velocity so that it's moving
    # | left, providing that it isn't already doing so
    # |---------------------------------------------
    def setHorizontalDirectionRight(self):
        if self.xVelocity < 0:
            self.changeDirectionX()

    # | changeDirectionY()
    # |---------------------------------------------
    # | Changes the direction of the ball in the
    # | y-axis by changing the sign off the
    # | velocity. Allows the ball to
    # | 'bounce' off collisions
    # |---------------------
    def changeDirectionY(self):
        self.yVelocity *= -1

    # | setVerticalDirectionUp()
    # |----------------------------------------------
    # | Changes the ball's y velocity so that it's
    # | moving up, if it isn't already doing so
    # |------------------------------------
    def setVerticalDirectionUp(self):
        if self.yVelocity > 0:
            self.changeDirectionY()

    # | setVerticalDirectionDown()
    # |---------------------------------------------
    # | Changes the ball's y velocity so that it's
    # | moving down if it isn't already doing so
    # |--------------------------------------
    def setVerticalDirectionDown(self):
        if self.yVelocity < 0:
            self.changeDirectionY()

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