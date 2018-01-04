#CK

import pygame
from pygame.locals import *
import sys
from objects.Button import Button
from objects.Title import Title

pygame.init()

setDisplay = pygame.display.set_mode((300, 300))

red = (255, 0, 0)
green = (0, 255, 0)

bt = Button(setDisplay, 10, 10, 50, 50, red, green, "Hello")
title = Title(setDisplay, 10, 40, "Hello There", 14, red)

while True:
    bt.draw()
    title.draw()
    pygame.display.update()

    xmouse, ymouse = pygame.mouse.get_pos()

    bt.hover(xmouse, ymouse)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()