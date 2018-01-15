#CK

import Helpers

class Title():
    def __init__(self, xPos, yPos, text, size, colour=(255, 255, 255)):

        # | Create text object
        self.text = text
        self.size = size
        self.colour = colour
        self.text = Helpers.createText(text, size, colour)

        # | Get the rect of the text and position
        self.rect = self.text.get_rect()
        self.rect.centerx = xPos
        self.rect.centery = yPos

    # | draw()
    # |-------------------------------------
    # | Blits the text to a passed surface
    # |-------------------------------
    def draw(self, surface):
        surface.blit(self.text, (self.rect.x, self.rect.y))

    # | changeText()
    # |---------------------------------
    # | Changes the text of the title
    # |---------------------------
    def changeText(self, newText, newSize=-1):
        # | If no size was passed, keep it the same
        if newSize < 0:
            newSize = self.size

        text = Helpers.createText(newText, newSize, self.colour)

        self.text = text
