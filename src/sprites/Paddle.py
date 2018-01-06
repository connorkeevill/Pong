#CK

import pygame


class Paddle(pygame.sprite.Sprite):
    def __init__(self, colour=(255, 255, 255)):
        # | Call __init__() method of Sprite() to inherit
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((15, 70))
        self.image.fill(colour)
        self.rect = self.image.get_rect()

        self.rect.x = 40
        self.rect.y = 150

    def update(self):
        self.move()

    def move(self):
        self.rect.y += 3
        if self.rect.top > 300:
            self.rect.bottom = 0
