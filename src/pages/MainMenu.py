#CK

import pygame

from objects.Button import Button
from objects.Title import Title
from resources import colours

from pages.Page import Page

pygame.init()

class MainMenu(Page):
    def __init__(self, surface):
        # | Call the superclass __init__() method
        Page.__init__(self, surface)

        # | btnPlay
        # |----------
        btnPlayDimensions = {"width":300, "height":100}
        btnPlayXpos = 450
        btnPlayYpos = 450
        self.btnPlay = Button(btnPlayXpos, btnPlayYpos, btnPlayDimensions, colours.red, colours.blue, "Play")

        # | ttlPong
        # |----------
        ttlPongXpos = 450
        ttlPongYpos = 200
        self.ttlPong = Title(ttlPongXpos, ttlPongYpos, "Pong", 121)

        self.addToObjects([self.btnPlay, self.ttlPong])

    # | handleEvent()
    # |---------------------------------------------------------------------
    # | Takes an event to determine what action can be taken to handle it
    # |---------------------------------------------------------------
    def handleEvent(self, event):
        action = None

        if event.type == pygame.MOUSEMOTION:
            xMouse, yMouse = pygame.mouse.get_pos()
            self.btnPlay.hover(xMouse, yMouse)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.btnPlay.clicked():
                action = "GamePlay"

        return action
