#CK


import pygame
from resources import colours
from pages.Page import Page
from objects.Button import Button

class Pause(Page):
    def __init__(self, surface):
        # | Call the superclass __init__() method
        Page.__init__(self, surface)

        self.backgroundSurface = self.createBackgroundSurface()

        # | btnResume
        # |------------
        btnResumeDimensions = {'width':450, 'height':100}
        btnResumeXpos = self.surface.get_width() / 2
        btnResumeYpos = 200
        btnResumeColour = colours.btnPrimary
        btnResumeHoverColour = colours.btnHover
        btnResumeAction = "Resume"
        btnResumeText = "Resume"
        btnResumeTextSize = 35
        btnResumeTextColour = colours.btnText
        self.btnResume = Button(btnResumeXpos, btnResumeYpos, btnResumeDimensions, btnResumeColour, btnResumeHoverColour,
                                btnResumeAction, btnResumeText, btnResumeTextSize, btnResumeTextColour)

        # | btnQuit
        # |----------
        btnQuitDimensions = {'width': 450, 'height': 100}
        btnQuitXpos = self.surface.get_width() / 2
        btnQuitYpos = 350
        btnQuitColour = colours.btnPrimary
        btnQuitHoverColour = colours.btnHover
        btnQuitAction = "MainMenu"
        btnQuitText = "Quit"
        btnQuitTextSize = 35
        btnQuitTextColour = colours.btnText
        self.btnQuit = Button(btnQuitXpos, btnQuitYpos, btnQuitDimensions, btnQuitColour, btnQuitHoverColour,
                              btnQuitAction, btnQuitText, btnQuitTextSize, btnQuitTextColour)

        self.addToObjects([self.btnResume, self.btnQuit])
        self.addToButtons([self.btnResume, self.btnQuit])

    # | draw()
    # |-----------------------------------------------------
    # | Overrides the method from the superclass, to blit
    # | this page's background and prevent the screen
    # | being cleared between frames. This allows
    # | the sense of transparency that is seen.
    # |------------------------------------
    def draw(self):
        self.surface.blit(self.backgroundSurface, (0,0))
        self.drawObjects()

    # | createBackgroundSurface()
    # |----------------------------------------------------------
    # | Creates the surface that will be used as the background
    # | for this page, and populates it with a colour and
    # | a transparency value, to allow a fading effect
    # |---------------------------------------------
    def createBackgroundSurface(self):
        backgroundSurface = pygame.Surface((self.surface.get_width(), self.surface.get_height()))
        backgroundSurface.fill(colours.grey)
        backgroundSurface.set_alpha(7)

        return backgroundSurface