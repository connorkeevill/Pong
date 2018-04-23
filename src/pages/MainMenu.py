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

        # | btnOnePlayer
        # |-----------
        btnOnePlayerDimensions = {"width":250, "height":100}
        btnOneplayerXpos = 300
        btnOnePlayerYpos = 400
        self.btnOnePlayer = Button(btnOneplayerXpos, btnOnePlayerYpos, btnOnePlayerDimensions, colours.red, colours.blue, "One Player", 28, colours.black)

        # | btnTwoPlayer
        # |----------
        btnTwoPlayerDimensions = {"width":250, "height":100}
        btnTwoPlayerXpos = 650
        btnTwoPlayerYpos = 400
        self.btnTwoPlayer = Button(btnTwoPlayerXpos, btnTwoPlayerYpos, btnTwoPlayerDimensions, colours.red, colours.blue, "Two player", 28, colours.black)

        # | ttlPong
        # |----------
        ttlPongXpos = 450
        ttlPongYpos = 200
        self.ttlPong = Title(ttlPongXpos, ttlPongYpos, "Pong", 121)

        self.addToObjects([self.btnOnePlayer, self.btnTwoPlayer, self.ttlPong])

    # | handleEvent()
    # |---------------------------------------------------------------------
    # | Takes an event to determine what action can be taken to handle it
    # |---------------------------------------------------------------
    def handleEvent(self, event):
        action = None

        if event.type == pygame.MOUSEMOTION:
            xMouse, yMouse = pygame.mouse.get_pos()
            self.btnOnePlayer.hover(xMouse, yMouse)
            self.btnTwoPlayer.hover(xMouse, yMouse)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.btnOnePlayer.clicked():
                action = "OnePlayerGame"
            elif self.btnTwoPlayer.clicked():
                action = "TwoPlayerGame"

        return action
