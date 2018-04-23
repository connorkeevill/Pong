# CK

from objects.Title import Title
import pygame
import Helpers

pygame.init()

# | Button()
# |---------------------------------------------------
# | Class for a button. Handles it's position, size
# | colours, text, drawing, hovering and clicks
# |--------------------------------------
class Button():
    def __init__(self, xPos, yPos, dimensions, colour, hoverColour, text="", textSize=15, textColour=(255, 255, 255)):
        # | Create rect and position button
        self.rect = pygame.Rect(xPos, yPos, dimensions["width"], dimensions["height"])
        self.rect.centerx = xPos
        self.rect.centery = yPos

        # | Define colours
        self.colour = colour
        self.hoverColour = hoverColour
        self.drawColour = colour

        # | Define text stuff
        self.text = Title(xPos, yPos, text, 30, textColour)

        # | Instantiate needed attributes for button
        self.isHovering = False
        self.xPos = None
        self.yPos = None

    # | draw()
    # |----------------------------------------------------------------------
    # | Draws the button at it's location, on it's surface, in it's colour
    # |---------------------------------------------------------------
    def draw(self, surface):
        pygame.draw.rect(surface, self.drawColour, self.rect)
        self.text.draw(surface)

    # | hover()
    # |-------------------------------------------------
    # | Determines if the mouse is over the button and
    # | changes the drawColour accordingly if it is
    # |-----------------------------------------
    def hover(self, xMouse, yMouse):
        self.isHovering = self.rect.collidepoint(xMouse, yMouse)

        if self.isHovering:
            self.drawColour = self.hoverColour
        else:
            self.drawColour = self.colour

    # | click()
    # |-------------------------------------------------
    # | Uses the isHovering flag from self.hover() to
    # | determine if a click was above the button
    # |--------------------------------------
    def clicked(self):
        return self.isHovering