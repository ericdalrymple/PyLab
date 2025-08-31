from pygame import Vector2
import tinyengine
import tinyengine.transform

"""
AbstractEntity
    Abstract base class for all entities in the game.
"""
class AbstractEntity():
    
    # Properties
    transform: tinyengine.transform.Transform = tinyengine.transform.Transform()
    
    def __init__(self, startPosition : Vector2):
        self.transform = tinyengine.transform.Transform()
        self.transform.set_position(startPosition.x, startPosition.y)

    def start(self):
        return
    
    def draw(self, surface):
        return

    def update(self, deltaTime, event):
        return
