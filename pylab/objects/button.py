import pygame
import pylab
from pylab.helpers.textrenderer import *

class Button(pylab.Entity):

    # Constants
    STATE_IDLE      = 0
    STATE_HOVERED   = 1
    STATE_PRESSED   = 2

    # Public
    color       : tuple = (127, 127, 127)
    cornerSize  : int = 5
    fontColor   : tuple = (31, 31, 31)
    hoverColor  : tuple = (195, 195, 195)
    pressedColor: tuple = (91, 91, 91)
    size        : tuple = (200, 50)

    # Private
    _currentColor = color
    _state = 0
    _textRenderer = None


    def __init__(self, x=0, y=0, width=150, height=50, text="", textSize=30):
        super().__init__(x, y, [])
        self.size = (width, height)
        self._textRenderer = TextRenderer(
            x, y,
            textSize,
            (31, 31, 31),
            TextRenderer.ANCHOR_CENTER,
            TextRenderer.ANCHOR_CENTER,
            text)


    def __contains_point__(self, point : tuple):
        pos : pygame.Vector2 = self.transform.get_world_position()
        left = pos.x
        top = pos.y
        right = left + self.size[0]
        bottom = top + self.size[1]

        x = point[0]
        y = point[1]

        is_outside = (x < left) or (y < top) or (x > right) or (y > bottom)

        return not is_outside
    

    def __refresh_color__(self):

        # Set color according to state
        self._currentColor = self.STATE_IDLE
        if self._state == self.STATE_IDLE:
            self._currentColor = self.color

        elif self._state == self.STATE_HOVERED:
            self._currentColor = self.hoverColor

        elif self._state == self.STATE_PRESSED:
            self._currentColor = self.pressedColor


    def __set_state__(self, newState):

        self._state = newState
        self.__refresh_color__()

    
    # Virtual
    def on_button_clicked(self):
        return


    # Overrides
    def start(self):
        super().start()

    def draw(self, surface):
        pos : pygame.Vector2 = self.transform.get_world_position()

        # Draw
        pygame.draw.rect(
            surface,
            color=self._currentColor,
            rect=(
                int(pos.x),
                int(pos.y),
                self.size[0],
                self.size[1]),
            width=0,
            border_radius=-1,
            border_top_left_radius=self.cornerSize,
            border_top_right_radius=self.cornerSize,
            border_bottom_left_radius=self.cornerSize,
            border_bottom_right_radius=self.cornerSize)
        
        # Draw the text for the mouse position
        self._textRenderer.draw(
            surface,
            int(pos.x + (self.size[0] * 0.5)),
            int(pos.y + (self.size[1] * 0.5)))
        

    def update(self, deltaTime):

        self.__refresh_color__()
        

    def on_mouse_move(self, pos):
        
        if self.__contains_point__(pos):
            if self._state == self.STATE_IDLE:
                self.__set_state__(self.STATE_HOVERED)
            
        else:
            self.__set_state__(self.STATE_IDLE)


        
    def on_mouse_down(self, pos, button):

        if button != pygame.BUTTON_LEFT:
            return

        if self.__contains_point__(pos):
            if self._state != self.STATE_PRESSED:
                self.__set_state__(self.STATE_PRESSED)
    

    def on_mouse_up(self, pos, button):

        if button != pygame.BUTTON_LEFT:
            return

        if self._state == self.STATE_PRESSED:
            if self.__contains_point__(pos):
                self.__set_state__(self.STATE_HOVERED)
                self.on_button_clicked()
            else:
                self.__set_state__(self.STATE_IDLE)
