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
        # |---------------
        btnOneplayerXpos = 300
        btnOnePlayerYpos = 400
        btnOnePlayerDimensions = {"width":250, "height":100}
        btnOnePlayerColour = colours.btnPrimary
        btnOnePlayerHoverColour = colours.btnHover
        btnOnePlayerAction = "Difficulty"
        btnOnePlayerText = "One player"
        btnOnePlayerTextSize = 28
        btnOnePlayerTextColour = colours.btnText
        self.btnOnePlayer = Button(btnOneplayerXpos, btnOnePlayerYpos, btnOnePlayerDimensions, btnOnePlayerColour, btnOnePlayerHoverColour,
                                   btnOnePlayerAction, btnOnePlayerText, btnOnePlayerTextSize, btnOnePlayerTextColour)

        # | btnTwoPlayer
        # |---------------
        btnTwoPlayerXpos = 600
        btnTwoPlayerYpos = 400
        btnTwoPlayerDimensions = {"width":250, "height":100}
        btnTwoPlayerColour = colours.btnPrimary
        btnTwoPlayerHoverColour = colours.btnHover
        btnTwoPlayerAction = "TwoPlayerGame"
        btnTwoPlayerText = "Two player"
        btnTwoPlayerTextSize = 28
        btnTwoPlayerTextColour = colours.btnText
        self.btnTwoPlayer = Button(btnTwoPlayerXpos, btnTwoPlayerYpos, btnTwoPlayerDimensions, btnTwoPlayerColour, btnTwoPlayerHoverColour,
                                   btnTwoPlayerAction, btnTwoPlayerText, btnTwoPlayerTextSize, btnTwoPlayerTextColour)

        # | ttlPong
        # |----------
        ttlPongXpos = 450
        ttlPongYpos = 200
        self.ttlPong = Title(ttlPongXpos, ttlPongYpos, "Pong", 121)

        self.addToObjects([self.btnOnePlayer, self.btnTwoPlayer, self.ttlPong])
        self.addToButtons([self.btnOnePlayer, self.btnTwoPlayer])