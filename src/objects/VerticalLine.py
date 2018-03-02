#CK

import pygame

class VerticalLine():
    def __init__(self, xPos, startPoint, endPoint, segmentLenth, interval, colour=(255, 255, 255)):
        self.xPos = xPos
        self.startPoint = startPoint
        self.endPoint = endPoint
        self.segmentLength = segmentLenth
        self.interval = interval + segmentLenth # | This is the sum of interval and segmentLength, so that interval
                                                # | can refer to just the gap between segments, without having
                                                # | to compensate for the length of the segments too
        self.colour = colour
        self.lines = []

    def draw(self, surface):
        penYpos = 0
        while penYpos <= self.endPoint:
            segmentStartXpos = (self.xPos, penYpos)
            segmentEndXpos = (self.xPos, penYpos + self.segmentLength)

            pygame.draw.line(surface, self.colour, segmentStartXpos, segmentEndXpos, 4)


            penYpos += self.interval