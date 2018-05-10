#CK

import pygame

from objects.Button import Button
from objects.Title import Title
from resources import colours

from pages.Page import Page

class Difficulty(Page):
    def __init__(self, surface, pageName):
        Page.__init__(self, surface, pageName)

        # | btnEasy
        # |----------
        btnEasyXpos = 450
        btnEasyYpos = 200
        btnEasyDimensions = {'width':400, 'height':100}
        btnEasyColour = colours.btnPrimary
        btnEasyHoverColour = colours.btnHover
        btnEasyAction = "OnePlayerGameEasy"
        btnEasyText = "Easy"
        btnEasyTextSize = 30
        btnEasyTextColour = colours.btnText
        self.btnEasy = Button(btnEasyXpos, btnEasyYpos, btnEasyDimensions, btnEasyColour, btnEasyHoverColour,
                              btnEasyAction, btnEasyText, btnEasyTextSize, btnEasyTextColour)

        # | btnMedium
        # |------------
        btnMediumXpos = 450
        btnMediumYpos = 320
        btnMediumDimensions = {'width':400, 'height':100}
        btnMediumColour = colours.btnPrimary
        btnMediumHoverColour = colours.btnHover
        btnMediumAction = "OnePlayerGameMedium"
        btnMediumText = "Medium"
        btnMediumTextSize = 30
        btnMediumTextColour = colours.btnText
        self.btnMedium = Button(btnMediumXpos, btnMediumYpos, btnMediumDimensions, btnMediumColour, btnMediumHoverColour,
                                btnMediumAction, btnMediumText, btnMediumTextSize, btnMediumTextColour)

        # | btnHard
        # |------------
        btnHardXpos = 450
        btnHardYpos = 440
        btnHardDimensions = {'width': 400, 'height': 100}
        btnHardColour = colours.btnPrimary
        btnHardHoverColour = colours.btnHover
        btnHardAction = "OnePlayerGameHard"
        btnHardText = "Hard"
        btnHardTextSize = 30
        btnHardTextColour = colours.btnText
        self.btnHard = Button(btnHardXpos, btnHardYpos, btnHardDimensions, btnHardColour, btnHardHoverColour,
                              btnHardAction, btnHardText, btnHardTextSize, btnHardTextColour)

        # | btnBack
        # |----------
        btnBackXpos = 35
        btnBackYpos = 20
        btnBackDimensions = {'width': 50, 'height': 20}
        btnBackColour = colours.btnPrimary
        btnBackHoverColour = colours.btnHover
        btnBackAction = "MainMenu"
        btnBackText = "Back"
        btnBackTextSize = 19
        btnBackTextColour = colours.btnText
        self.btnBack = Button(btnBackXpos, btnBackYpos, btnBackDimensions, btnBackColour, btnBackHoverColour,
                              btnBackAction, btnBackText, btnBackTextSize, btnBackTextColour)

        self.addToObjects([self.btnEasy, self.btnMedium, self.btnHard, self.btnBack])
        self.addToButtons([self.btnEasy, self.btnMedium, self.btnHard, self.btnBack])
