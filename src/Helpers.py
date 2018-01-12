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
    if event.type == QUIT :
        pygame.quit()
        sys.exit()