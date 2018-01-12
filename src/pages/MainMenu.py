#CK

import pygame

from objects.Button import Button
from resources import colours

class MainMenu():

        def __init__(self, surface):
            self.surface = surface
            self.btnPlay = Button(350, 300, [400, 150], colours.red, colours.blue, "Play")

        # | draw()
        # |---------------------------------------------
        # | Draws all items on the page to the surface
        # |----------------------------------------
        def draw(self):
            self.btnPlay.draw(self.surface)

        # | handleEvent()
        # |---------------------------------------------------------------------
        # | Takes an event to determine what action can be taken to handle it
        # |---------------------------------------------------------------
        def handleEvent(self, event):
            if event.type == pygame.MOUSEMOTION:
                xMouse, yMouse = pygame.mouse.get_pos()
                self.btnPlay.hover(xMouse, yMouse)
