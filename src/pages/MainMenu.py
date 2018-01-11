#CK

import pygame

from objects.Button import Button
from resources import colours

class MainMenu():

        def __init__(self, surface):
            self.surface = surface
            self.btnPlay = Button(self.surface, self.surface.get_width()/2, self.surface.get_height()/2, 200, 75, colours.white, colours.red, "Play", colours.black)

        def draw(self):
            self.btnPlay.draw()

        def handleEvent(self, event):
            if event.type == pygame.MOUSEMOTION:
                xMouse, yMouse = pygame.mouse.get_pos()
                self.btnPlay.hover(xMouse, yMouse)

