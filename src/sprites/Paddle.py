#CK

import pygame
pygame.init()


class Paddle(pygame.sprite.Sprite):
    def __init__(self, xPos, yPos, colour=(255, 255, 255)):
        # | Call __init__() method of Sprite() to inherit
        pygame.sprite.Sprite.__init__(self)

        # | Create the paddle's rect and position it
        self.rect = pygame.Rect(xPos, yPos, 30, 140)
        self.rect.centerx = xPos
        self.rect.centery = yPos

        self.colour = colour

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
        self.rect.y -= 3

    # | moveDown()
    # |------------------------
    # | Moves the paddle down
    # |--------------------
    def moveDown(self):
        self.rect.y += 3