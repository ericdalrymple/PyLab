from pygame import Vector2

"""
AbstractEntity
    Abstract base class for all entities in the game.
"""
class AbstractEntity():
    
    # Properties
    position : Vector2 = Vector2(0, 0)
    scale : Vector2 = Vector2(1, 1)
    rotation : float = 0.0
    
    def __init__(self, startPosition : Vector2):
        self.position = startPosition

    def start(self):
        return
    
    def draw(self, surface):
        return

    def update(self, deltaTime, event):
        return
