#CK

import pygame

class Title():
    def __init__(self, surface, xPos, yPos, text, size, colour=(255, 255, 255)):
        self.surface = surface
        self.xPos = xPos
        self.yPos = yPos
        self.size = size
        self.colour = colour

        self.text = self.createText(text, size)

    def draw(self):
        self.surface.blit(self.text, (self.xPos, self.yPos))

    def createText(self, text, size):
        font = pygame.font.SysFont("Century Gothic", size)
        text = font.render(text, False, self.colour)
        return text

    def changeText(self, newText, newSize=-1):
        if newSize < 0:
            newSize = self.size

        text = self.createText(newText, newSize)

        self.text = text