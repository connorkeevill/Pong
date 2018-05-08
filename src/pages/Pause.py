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
        btnResumeColour = colours.grey
        btnResumeHoverColour = colours.lightGrey
        btnResumeText = "Resume"
        btnResumeTextSize = 35
        btnResumeTextColour = colours.white
        self.btnResume = Button(btnResumeXpos, btnResumeYpos, btnResumeDimensions, btnResumeColour, btnResumeHoverColour,
                           btnResumeText, btnResumeTextSize, btnResumeTextColour)

        # | btnQuit
        # |----------
        btnQuitDimensions = {'width': 450, 'height': 100}
        btnQuitXpos = self.surface.get_width() / 2
        btnQuitYpos = 350
        btnQuitColour = colours.grey
        btnQuitHoverColour = colours.lightGrey
        btnQuitText = "Quit"
        btnQuitTextSize = 35
        btnQuitTextColour = colours.white
        self.btnQuit = Button(btnQuitXpos, btnQuitYpos, btnQuitDimensions, btnQuitColour, btnQuitHoverColour,
                              btnQuitText, btnQuitTextSize, btnQuitTextColour)

        self.addToObjects([self.btnResume, self.btnQuit])

    # | handleEvent()
    # |---------------------------------------------------------------------
    # | Takes an event to determine what action can be taken to handle it
    # |---------------------------------------------------------------
    def handleEvent(self, event):
        action = None

        if event.type == pygame.MOUSEMOTION:
            xMouse, yMouse = pygame.mouse.get_pos()
            self.btnResume.hover(xMouse, yMouse)
            self.btnQuit.hover(xMouse, yMouse)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.btnResume.clicked():
                action = "Resume"
            elif self.btnQuit.clicked():
                action = "MainMenu"

        return action

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