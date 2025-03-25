import pygame.gfxdraw
import tinyengine.component

"""
ImageDrawable
    Provides basic default rendering for an image.
"""
class ImageDrawable(tinyengine.component.Component):

    # Properties
    radius = 5

    _imagePath = ""
    _image = None

    def __init__(self, image_path):
        self._imagePath = image_path
        self._image = pygame.image.load(self._imagePath)


    def draw(self, surface):
        width = self._image.get_rect().width
        height = self._image.get_rect().height
        surface.blit(
            self._image,
            (self.entity.position.x - (width >> 1),
             self.entity.position.y - (height >> 1),
             width,
             height)
        )