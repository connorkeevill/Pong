#CK

import pygame
from pygame.locals import *
import sys
import Helpers

from resources import colours

from pages.MainMenu import MainMenu
from pages.GamePlay import GamePlay

pygame.init()

screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()
FPS = 60

pages = {"MainMenu": MainMenu(screen),
         "GamePlay": GamePlay(screen)}

page = "MainMenu"

while True:
    screen.fill(colours.black)

    action = None
    clock.tick(FPS)

    pages[page].draw()

    pygame.display.update()

    for event in pygame.event.get():
        action = pages[page].handleEvent(event)

        Helpers.checkForQuit(event)

        if action == "GamePlay":
            page = action
            print("Change to game page")
