#CK

import pygame
pygame.init()

class Ball(pygame.sprite.Sprite):
    def __init__(self, xPos, yPos, colour=(255, 255, 255)):
        # | Call __init__() of the Sprite() class to inherit
        pygame.sprite.Sprite.__init__(self)

        # | Define how sprite should look, and the rect this should give it
        self.image = pygame.Surface((40, 40))
        self.image.fill((colour))
        self.rect = self.image.get_rect()

        # | Place it here while testing
        self.rect.centerx = xPos
        self.rect.centery = yPos

    def update(self):
        self.move()

    def move(self):
        self.rect.x += 5
        if self.rect.left > 300:
            self.rect.right = 0

