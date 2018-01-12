#CK

import pygame
from pygame.locals import *
import sys
import Helpers

from pages.MainMenu import MainMenu

pygame.init()

screen = pygame.display.set_mode((700, 600))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()
FPS = 60

pages = {"MainMenu": MainMenu(screen)}

page = "MainMenu"

while True:
    action = None
    clock.tick(FPS)

    pages[page].draw()

    pygame.display.update()

    for event in pygame.event.get():
        action = pages[page].handleEvent(event)

        Helpers.checkForQuit(event)

        if action == "GamePlay":
            print("Change to game page")
