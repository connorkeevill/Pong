#CK

import pygame
pygame.init()


class Paddle(pygame.sprite.Sprite):
    def __init__(self, xPos, yPos, colour=(255, 255, 255)):
        # | Call __init__() method of Sprite() to inherit
        pygame.sprite.Sprite.__init__(self)

        # | Create the rect for the paddle
        self.rect = pygame.Rect(xPos, yPos, 30, 140)

        self.colour = colour

        # | Position the paddle
        self.rect.centerx = xPos
        self.rect.centery = yPos

    def draw(self, surface):
        pygame.draw.rect(surface, self.colour, self.rect)

    def update(self):
        self.move()

    def move(self):
        None
