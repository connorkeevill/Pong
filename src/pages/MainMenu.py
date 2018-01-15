#CK

import pygame

from objects.Button import Button
from objects.Title import Title
from resources import colours

from pages.Page import Page

pygame.init()

class MainMenu(Page):
        def __init__(self, surface):
            Page.__init__(self, surface)

            # | Create Play Button
            btnPlayDimensions = {"width":300, "height":100}
            btnPlayXpos = 450
            btnPlayYpos = 450
            self.btnPlay = Button(btnPlayXpos, btnPlayYpos, btnPlayDimensions, colours.red, colours.blue, "Play")

            # | Create Title
            ttlPongXpos = 450
            ttlPongYpos = 200
            self.ttlPong = Title(ttlPongXpos, ttlPongYpos, "Pong", 121)

            self.addToObjects([self.btnPlay, self.ttlPong])

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

