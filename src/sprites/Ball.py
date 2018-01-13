#CK

import pygame
pygame.init()

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

        self.xVelocity = 5
        self.yVelocity = 0

    def draw(self, surface):
        pygame.draw.rect(surface, self.colour, self.rect)

    def update(self):
        self.move()

    def move(self):
        self.rect.centerx += self.xVelocity
        self.rect.centery += self.yVelocity

    def changeDirection(self):
        self.xVelocity *= -1
