#CK


import pygame
from resources import colours
from pages.Page import Page
from objects.Button import Button

class Pause(Page):
    def __init__(self, surface):
        # | Call the superclass __init__() method
        Page.__init__(self, surface)

        self.backgroundSurface = pygame.Surface((self.surface.get_width(), self.surface.get_height()))
        self.backgroundSurface.fill(colours.grey)
        self.backgroundSurface.set_alpha(5)

        # | btnResume
        # |------------
        btnResumeDimensions = {'width':300, 'height':100}
        btnResumeXpos = self.surface.get_width() / 2
        btnResumeYpos = 300
        btnResumeColour = colours.grey
        btnResumeHoverColour = colours.lightGrey
        btnResumeText = "Resume"
        btnResumeTextSize = 32
        btnResumeTextColour = colours.white
        self.btnResume = Button(btnResumeXpos, btnResumeYpos, btnResumeDimensions, btnResumeColour, btnResumeHoverColour,
                           btnResumeText, btnResumeTextSize, btnResumeTextColour)

        # | btnQuit
        # |----------
        btnQuitDimensions = {'width': 300, 'height': 100}
        btnQuitXpos = self.surface.get_width() / 2
        btnQuitYpos = 500
        btnQuitColour = colours.grey
        btnQuitHoverColour = colours.lightGrey
        btnQuitText = "Quit"
        btnQuitTextSize = 32
        btnQuitTextColour = colours.white
        self.btnQuit = Button(btnQuitXpos, btnQuitYpos, btnQuitDimensions, btnQuitColour, btnQuitHoverColour,
                              btnQuitText, btnQuitTextSize, btnQuitTextColour)

        self.addToObjects([self.btnResume, self.btnQuit])

    def draw(self):
        self.surface.blit(self.backgroundSurface, (0,0))
        self.drawObjects()