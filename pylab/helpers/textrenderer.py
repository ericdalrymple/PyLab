import pygame.gfxdraw
import pylab.component

"""
TextRenderer
    Provides basic default rendering for an entity.
"""
class TextRenderer():

    # Constants
    ANCHOR_CENTER    : int = 0
    ANCHOR_LEFT      : int = 1
    ANCHOR_RIGHT     : int = 2
    ANCHOR_BOTTOM    : int = 3
    ANCHOR_TOP       : int = 4

    # Public fields
    fontColor       : tuple = (31, 31, 31)
    fontSize        : int = 30
    horizontalAlign : int = ANCHOR_CENTER
    text            : str = ""
    verticalAlign   : int = ANCHOR_CENTER


    # Private fields
    _font : pygame.font.Font = None


    # Private methods
    def __init__(self, x=0, y=0, textSize:int = 30, color:tuple = (0, 0, 0), hAlign:int = ANCHOR_CENTER, vAlign:int = ANCHOR_CENTER, text:str = ""):
        self.fontColor = color
        self.fontSize = textSize
        self.horizontalAlign = hAlign
        self.verticalAlign = vAlign
        self.text = text

        self._font = pygame.font.Font(None, self.fontSize)


    # Publuc methods
    def draw(self, surface, x, y):
        render = self._font.render(self.text, 1, self.fontColor)

        textOffsetX = 0
        if self.horizontalAlign == self.ANCHOR_LEFT:
            textOffsetX = 0
        elif self.horizontalAlign == self.ANCHOR_RIGHT:
            textOffsetX = -render.get_size()[0]
        elif self.horizontalAlign == self.ANCHOR_CENTER:
            textOffsetX = -render.get_size()[0] * 0.5

        textOffsetY = 0
        if self.verticalAlign == self.ANCHOR_TOP:
            textOffsetY = 0
        elif self.verticalAlign == self.ANCHOR_BOTTOM:
            textOffsetY = -render.get_size()[1]
        elif self.verticalAlign == self.ANCHOR_CENTER:
            textOffsetY = -render.get_size()[1] * 0.5

        textX = int(x + textOffsetX)
        textY = int(y + textOffsetY)
        surface.blit(render, (textX, textY))