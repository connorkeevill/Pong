#CK

import pygame
from pygame.locals import *
import sys
from objects.Button import Button
from objects.Title import Title
from sprites.Ball import Ball

pygame.init()

setDisplay = pygame.display.set_mode((300, 300))

clock = pygame.time.Clock()
FPS = 60

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

ball = Ball()

sprites = pygame.sprite.Group()

sprites.add(ball)


while True:
    clock.tick(FPS)

    setDisplay.fill(black)

    sprites.update()
    sprites.draw(setDisplay)




    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()