# CK

import pygame
pygame.init()
from pygame.locals import *

# | Button()
# |---------------------------------------------------
# | Class for a button. Handles it's position, size
# | colours, text, drawing, hovering and clicks
# |--------------------------------------
class Button():
    def __init__(self, xPos, yPos, dimensions, colour, hoverColour, text=False, textColour=(255, 255, 255)):
        # | Assign passed variables
        self.dimensions = dimensions
        self.colour = colour
        self.hoverColour = hoverColour
        self.textColour = textColour
        self.text = self.createText(text, 15)

        # | Define the colour that'll be used to when drawing the button
        self.drawColour = colour

        # | Instantiate needed attributes for button
        self.isHovering = False
        self.xPos = None
        self.yPos = None

        # | Position the button
        self.positionAboutCentre(xPos, yPos)

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

    # | createText()
    # |------------------------------------
    # | Returns a text object that can be
    # | blitted to a a display, taking
    # | the text and size as params
    # |------------------------
    def createText(self, text, size):
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

    # | click()
    # |-------------------------------------------------
    # | Uses the isHovering flag from self.hover() to
    # | determine if a click was above the button
    # |--------------------------------------
    def clicked(self):
        return self.isHovering