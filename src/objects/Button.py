# CK

import pygame
pygame.init()
from pygame.locals import *

# | Button()
# |---------------------------------------------------
# | Class for a button. Handles it's position, size
# | colours, text, drawing and mouse hovering
# |--------------------------------------
class Button():
    def __init__(self, surface, xPos, yPos, width, height, colour, hoverColour, text=False, textColour=(255, 255, 255)):
        # | Assign passed variables
        self.surface = surface
        self.xPos = xPos
        self.yPos = yPos
        self.width = width
        self.height = height
        self.colour = colour
        self.hoverColour = hoverColour
        self.textColour = textColour
        self.text = self.createText(text)

        self.drawColour = colour

    def createText(self, text):
        size = 15
        font = pygame.font.SysFont("Century Gothic", size)
        text = font.render(text, False, self.textColour)
        return text

    # | draw()
    # |----------------------------------------------------------------------
    # | Draws the button at it's location, on it's surface, in it's colour
    # |---------------------------------------------------------------
    def draw(self):
        pygame.draw.rect(self.surface, self.drawColour, (self.xPos, self.yPos, self.width, self.height))
        self.surface.blit(self.text, (self.xPos, self.yPos))

    # | hover()
    # |-------------------------------------------------
    # | Determines if the mouse is over the button and
    # | changes the drawColour accordingly if it is
    # |-----------------------------------------
    def hover(self, xMouse, yMouse):
        horizontalRange = self.xPos <= xMouse <= (self.xPos + self.width)
        verticalRange = self.yPos <= yMouse <= (self.yPos + self.height)

        if horizontalRange and verticalRange:
            self.drawColour = self.hoverColour
        else:
            self.drawColour = self.colour
