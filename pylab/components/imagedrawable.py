import pygame.gfxdraw
import pylab.component

"""
ImageDrawable
    Provides basic default rendering for an image.
"""
class ImageDrawable(pylab.component.Component):

    # Properties
    radius = 5

    _imagePath = ""
    _image = None
    _width = 0.0
    _height = 0.0

    def __init__(self, image_path: str, width: float = 0.0, height: float = 0.0):
        self._imagePath = image_path
        self._image = pygame.image.load(self._imagePath)

        self._width = width
        self._height = height
        self._image = pygame.transform.scale(self._image, (self._width, self._height))


    def draw(self, surface):
        pos : pygame.Vector2 = self.entity.transform.get_world_position()
        surface.blit(
            self._image,
            (
                pos.x - (self._width >> 1),
                pos.y - (self._height >> 1),
                self._width,
                self._height
            )
        )