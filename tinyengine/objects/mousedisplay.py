import pygame
import tinyengine

# ======================================================================================= #
# MouseDisplay writes the position of the mouse cursor on the screen.
# ======================================================================================= #
class MouseDisplay(tinyengine.Entity):

    _font : pygame.font.Font = None
    _mousePos : tuple = (0, 0)

    def __init__(self):
        super().__init__(0, 0, [])

    def draw(self, surface : pygame.Surface):

        # Draw the text for the mouse position
        if not self._font is None:
            text = f"(x={self._mousePos[0]}, y={self._mousePos[1]})"
            render = self._font.render(text, 1, (255, 0, 0))
            surface.blit(render, (surface.get_width() - render.get_size()[0] - 10, 10))


    def update(self, deltaTime):

        # Set the font
        if self._font is None:
            self._font = pygame.font.Font(None, 30)


    def on_mouse_move(self, pos):

        # Update the mouse position
        self._mousePos = pos
