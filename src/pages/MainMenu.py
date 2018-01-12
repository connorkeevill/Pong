#CK

import pygame

from objects.Button import Button
from resources import colours

class MainMenu():

        def __init__(self, surface):
            self.surface = surface


            # | Create the button to be the play button
            btnPlayDimensions = {"width":300, "height":100}
            btnPlayXpos = 450
            btnPlayYpos = 450
            self.btnPlay = Button(btnPlayXpos, btnPlayYpos, btnPlayDimensions, colours.red, colours.blue, "Play")

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
            # | The action to tell the main.py file what to do (if required)
            action = None

            # | Mouse motion events; allows for the hovering of buttons
            if event.type == pygame.MOUSEMOTION:
                xMouse, yMouse = pygame.mouse.get_pos()
                self.btnPlay.hover(xMouse, yMouse)

            # | Clicking events; for clicking on buttons
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.btnPlay.clicked():
                    action = "GamePlay"

            # | Return the action
            return action

