import pygame
import pylab.component

"""
ArrowMovable
    Provides functionality to move the entity using the arrow keys.
"""
class ArrowMovable(pylab.component.Component):

    # Properties
    speed = 0

    # Internal members
    _down = False
    _left = False
    _right = False
    _up = False

    def __init__(self, speed = 50):
        self.speed = speed

    def update(self, deltaTime):
        move = pygame.Vector2(0, 0)

        if self._left:
            move += pygame.Vector2(-1, 0)
        if self._right:
            move += pygame.Vector2(1, 0)
        if self._up:
            move += pygame.Vector2(0, -1)
        if self._down:
            move += pygame.Vector2(0, 1)

        if move.length_squared() > 0:
            move = move.normalize() * (self.speed * deltaTime)
            self.entity.position.update(
                self.entity.position.x + move.x,
                self.entity.position.y + move.y 
            )


    def on_key_down(self, key):
        if key == pygame.K_LEFT:
            self._left = True
        
        if key == pygame.K_RIGHT:
            self._right = True
        
        if key == pygame.K_UP:
            self._up = True

        if key == pygame.K_DOWN:
            self._down = True


    def on_key_up(self, key):
        if key == pygame.K_LEFT:
            self._left = False
        
        if key == pygame.K_RIGHT:
            self._right = False
        
        if key == pygame.K_UP:
            self._up = False

        if key == pygame.K_DOWN:
            self._down = False