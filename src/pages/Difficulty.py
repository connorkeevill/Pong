#CK

import pygame

from objects.Button import Button
from objects.Title import Title
from resources import colours

from pages.Page import Page


class Difficulty(Page):
    def __init__(self, surface):
        Page.__init__(self, surface)

        # | btnEasy
        # |----------
        btnEasyDimensions = {'width':400, 'height':100}
        btnEasyXpos = 450
        btnEasyYpos = 200
        btnEasyColour = colours.red
        btnEasyHoverColour = colours.blue
        btnEasyText = "Easy"
        btnEasyTextSize = 30
        btnEasyTextColour = colours.black
        self.btnEasy = Button(btnEasyXpos, btnEasyYpos, btnEasyDimensions, btnEasyColour, btnEasyHoverColour,
                              btnEasyText, btnEasyTextSize, btnEasyTextColour)

        # | btnMedium
        # |------------
        btnMediumDimensions = {'width':400, 'height':100}
        btnMediumXpos = 450
        btnMediumYpos = 320
        btnMediumColour = colours.red
        btnMediumHoverColour = colours.blue
        btnMediumText = "Medium"
        btnMediumTextSize = 30
        btnMediumTextColour = colours.black
        self.btnMedium = Button(btnMediumXpos, btnMediumYpos, btnMediumDimensions, btnMediumColour, btnMediumHoverColour,
                                btnMediumText, btnMediumTextSize, btnMediumTextColour)

        # | btnHard
        # |------------
        btnHardDimensions = {'width': 400, 'height': 100}
        btnHardXpos = 450
        btnHardYpos = 440
        btnHardColour = colours.red
        btnHardHoverColour = colours.blue
        btnHardText = "Hard"
        btnHardTextSize = 30
        btnHardTextColour = colours.black
        self.btnHard = Button(btnHardXpos, btnHardYpos, btnHardDimensions, btnHardColour, btnHardHoverColour,
                                btnHardText, btnHardTextSize, btnHardTextColour)

        # | btnBack
        # |----------
        btnBackDimensions = {'width': 50, 'height': 20}
        btnBackXpos = 35
        btnBackYpos = 20
        btnBackColour = colours.red
        btnBackHoverColour = colours.blue
        btnBackText = "Back"
        btnBackTextSize = 19
        btnBackTextColour = colours.black
        self.btnBack = Button(btnBackXpos, btnBackYpos, btnBackDimensions, btnBackColour, btnBackHoverColour,
                              btnBackText, btnBackTextSize, btnBackTextColour)


        self.addToObjects([self.btnEasy, self.btnMedium, self.btnHard, self.btnBack])

    def handleEvent(self, event):
        action = None

        if event.type == pygame.MOUSEMOTION:
            xMouse, yMouse = pygame.mouse.get_pos()
            self.btnEasy.hover(xMouse, yMouse)
            self.btnMedium.hover(xMouse, yMouse)
            self.btnHard.hover(xMouse, yMouse)
            self.btnBack.hover(xMouse, yMouse)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.btnEasy.clicked():
                action = "OnePlayerGameEasy"
            elif self.btnMedium.clicked():
                action = "OnePlayerGameMedium"
            elif self.btnHard.clicked():
                action = "OnePlayerGameHard"
            elif self.btnBack.clicked():
                 action = "MainMenu"

        return action