#CK

import pygame
import Helpers
from resources import colours
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

pages = {"MainMenu": MainMenu(screen),
         "Difficulty": Difficulty(screen),
         "OnePlayerGameEasy": GamePlay(screen, 1, 5),
         "OnePlayerGameMedium": GamePlay(screen, 1, 8),
         "OnePlayerGameHard": GamePlay(screen, 1, 10),
         "TwoPlayerGame": GamePlay(screen, 2),
         "pause": Pause(screen)}

page = pages["MainMenu"]
pageToResume = None

while True:
    page.update()
    page.draw()

    for event in pygame.event.get():
        action = page.handleEvent(event)

        if action in pages:
            if action == 'pause':
                pageToResume = page
                print(pageToResume)
            page = pages[action]

        Helpers.checkForQuit(event)

    pygame.display.update()
    clock.tick(FPS)
