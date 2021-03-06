#CK

import pygame
pygame.init()

# | Paddle()
# |-------------------------------------------------
# | Class for a paddle, which handles the paddle's
# | location, movement and drawing of paddle
# |------------------------------------
class Paddle(pygame.sprite.Sprite):
    def __init__(self, xPos, yPos, windowHeight, colour=(255, 255, 255)):
        # | Call __init__() method of Sprite() to inherit
        pygame.sprite.Sprite.__init__(self)

        # | Create the paddle's rect and position it
        self.rect = pygame.Rect(xPos, yPos, 15, 90)
        self.rect.centerx = xPos
        self.rect.centery = yPos

        self.windowHeight = windowHeight

        self.colour = colour

        # | The paddle's speed
        self.yVelocity = 10

    # | draw()
    # |-------------------
    # | Draws the paddle
    # |---------------
    def draw(self, surface):
        pygame.draw.rect(surface, self.colour, self.rect)

    # | moveUp()
    # |-----------------------
    # | Moves the paddle up
    # |------------------
    def moveUp(self):
        if self.rect.top > 0:
            self.rect.y -= self.yVelocity

    # | moveDown()
    # |------------------------
    # | Moves the paddle down
    # |--------------------
    def moveDown(self):
        if self.rect.bottom < self.windowHeight:
            self.rect.y += self.yVelocity

    def setVelocity(self, newVelocity):
        self.yVelocity = newVelocity