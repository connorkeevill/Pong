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
    def __init__(self, xPos, yPos, dimensions, colour, hoverColour, text=False, textColour=(255, 255, 255)):
        # | Assign passed variables
        self.dimensions = dimensions
        self.colour = colour
        self.hoverColour = hoverColour
        self.textColour = textColour
        self.text = self.createText(text)

        self.hover = False
        self.xPos = None
        self.yPos = None

        self.positionAboutCentre(xPos, yPos)

        # |--------------------------------------------------------------------------------
        # | The colour that'll be used when the button is drawn. It is separate from the
        # | hoverColour and colour to allow hoveing to take place without modifying
        # | the original colours of the button; to preserve the class attributes
        # |-----------------------------------------------------------------
        self.drawColour = colour

    # | positionAboutCentre()
    # |-----------------------------------------------------------
    # | Puts the centre of the button on the x and y positions
    # | passed, by subtracting half the width and height
    # |--------------------------------------------
    def positionAboutCentre(self, xPos, yPos):
        width = self.dimensions[0]
        height = self.dimensions[1]
        horizontalCentre = xPos - (width / 2)
        veritcalCentre = yPos - (height / 2)

        self.xPos = horizontalCentre
        self.yPos = veritcalCentre


    def createText(self, text):
        size = 15
        font = pygame.font.SysFont("Century Gothic", size)
        text = font.render(text, False, self.textColour)
        return text

    # | draw()
    # |----------------------------------------------------------------------
    # | Draws the button at it's location, on it's surface, in it's colour
    # |---------------------------------------------------------------
    def draw(self, surface):
        width = self.dimensions[0]
        height = self.dimensions[1]
        pygame.draw.rect(surface, self.drawColour, (self.xPos, self.yPos, width, height))
        surface.blit(self.text, (self.xPos, self.yPos))

    # | hover()
    # |-------------------------------------------------
    # | Determines if the mouse is over the button and
    # | changes the drawColour accordingly if it is
    # |-----------------------------------------
    def hover(self, xMouse, yMouse):
        width = self.dimensions[0]
        height = self.dimensions[1]
        horizontalRange = self.xPos <= xMouse <= (self.xPos + width)
        verticalRange = self.yPos <= yMouse <= (self.yPos + height)

        if horizontalRange and verticalRange:
            self.drawColour = self.hoverColour
            self.isHovering = True
        else:
            self.drawColour = self.colour
            self.isHovering = False

    def click(self):
        if self.isHovering:
            return True