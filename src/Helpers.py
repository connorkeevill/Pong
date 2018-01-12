#CK

import pygame
from pygame.locals import *
import sys

# | checkForQuit()
# |-------------------------------------------
# | Checks if a quit event has occurred and
# | takes the necessary action for it
# |-------------------------------
def checkForQuit(event):
    if event.type == QUIT:
        pygame.quit()
        sys.exit()

# | createText()
# |------------------------------------
# | Returns a text object that can be
# | blitted to a a display, taking
# | the text and size as params
# |------------------------
def createText(text, size, colour):
    font = pygame.font.SysFont("ocr a extended", size)
    text = font.render(text, False, colour)
    return text

