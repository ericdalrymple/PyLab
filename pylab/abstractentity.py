from pygame import Vector2
import pylab
import pylab.transform

"""
AbstractEntity
    Abstract base class for all entities in the game.
"""
class AbstractEntity():
    
    # Properties
    transform: pylab.transform.Transform = pylab.transform.Transform()
    
    def __init__(self, startPosition : Vector2):
        self.transform = pylab.transform.Transform()
        self.transform.set_position(startPosition.x, startPosition.y)

    def start(self):
        return
    
    def draw(self, surface):
        return

    def update(self, deltaTime, event):
        return
