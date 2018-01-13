#CK

import Helpers

class Title():
    def __init__(self, xPos, yPos, text, size, colour=(255, 255, 255)):
        # | Assign params
        self.xPos = xPos
        self.yPos = yPos
        self.size = size
        self.colour = colour

        # | Get text object
        self.text = Helpers.createText(text, size, colour)
        self.positionAboutCentre(xPos, yPos)

    def positionAboutCentre(self, xPos, yPos):
        width = self.text.get_width()
        height = self.text.get_height()
        horizontalCentre = xPos - (width / 2)
        veritcalCentre = yPos - (height / 2)

        self.xPos = horizontalCentre
        self.yPos = veritcalCentre

    # | draw()
    # |-------------------------------------
    # | Blits the text to a passed surface
    # |-------------------------------
    def draw(self, surface):
        surface.blit(self.text, (self.xPos, self.yPos))

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