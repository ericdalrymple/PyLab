import pygame.gfxdraw
import tinyengine.component

"""
DefaultDrawable
    Provides basic default rendering for an entity.
"""
class DefaultDrawable(tinyengine.component.Component):

    # Properties
    radius = 5

    def draw(self, surface):
        pygame.gfxdraw.filled_circle(
            surface,
            int(self.entity.position.x),
            int(self.entity.position.y),
            self.radius,
            (0, 255, 0)
        )