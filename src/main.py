#CK

import pygame
from pygame.locals import *
import sys
from pages.MainMenu import MainMenu
from sprites.Ball import Ball
from sprites.Paddle import Paddle

pygame.init()

screen = pygame.display.set_mode((700, 600))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()
FPS = 60

pages = {"MainMenu": MainMenu(screen)}

page = "MainMenu"

while True:
    clock.tick(FPS)

    pages[page].draw()

    pygame.display.update()

    for event in pygame.event.get():
        pages[page].handleEvent(event)

        if event.type == QUIT:
            pygame.quit()
            sys.exit()