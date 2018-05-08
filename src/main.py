#CK

import pygame
import Helpers
from Router import Router
from pages.MainMenu import MainMenu
from pages.GamePlay import GamePlay
from pages.Difficulty import Difficulty
from pages.Pause import Pause
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'  # | This centers the window
pygame.init()

screenWidth = 900
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Pong")

FPS = 60
clock = pygame.time.Clock()

pages = ["MainMenu",
         "Difficulty",
         "OnePlayerGameEasy",
         "OnePlayerGameMedium",
         "OnePlayerGameHard",
         "TwoPlayerGame",
         "Pause"]


router = Router(screen)

page = router.route('MainMenu')
pageToResume = None

while True:
    page.update()
    page.draw()

    for event in pygame.event.get():
        action = page.handleEvent(event)

        # | If the action is to change page
        if action in pages:
            if action == 'Pause':
                pageToResume = page

            page = router.route(action)
        # | If we are resuming from a pause
        elif action == 'Resume':
            page = pageToResume

        Helpers.checkForQuit(event)

    pygame.display.update()
    clock.tick(FPS)
