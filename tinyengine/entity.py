import pygame
import tinyengine.abstractentity
import tinyengine.component

"""
Entity
    Entity class for every entity in the game. Its behaviour is defined by its components.
"""
class Entity(tinyengine.abstractentity.AbstractEntity):
    
    active = True
    visible = True

    _children : list[tinyengine.abstractentity.AbstractEntity] = []
    _components : list[tinyengine.component.Component] = []
    
    def __init__(self, startX : float = 0.0, startY : float = 0.0, components : list[tinyengine.component.Component] = []):
        super().__init__(pygame.Vector2(startX, startY))
        
        self._components = components
        for comp in self._components:
            comp._setParent(self)


    def start(self):
        for comp in self._components:
            comp.start()
    

    def draw(self, surface):
        if not self.visible:
            # Not visible; don't draw
            return
        
        for comp in self._components:
            comp.draw(surface)

    
    def update(self, deltaTime):
        if not self.active:
            # Not active; don't tick
            return
        
        for comp in self._components:
            comp.update(deltaTime)
    

    def on_key_down(self, key):
        for comp in self._components:
            comp.on_key_down(key)


    def on_key_up(self, key):
        for comp in self._components:
            comp.on_key_up(key)


    def on_key_held(self, key):
        for comp in self._components:
            comp.on_key_held(key)
    

    def on_mouse_down(self, position, button):
        for comp in self._components:
            comp.on_mouse_down(position, button)
    
    
    def on_mouse_up(self, position, button):
        for comp in self._components:
            comp.on_mouse_up(position, button)


    def on_mouse_clicked(self, position, button):
        for comp in self._components:
            comp.on_mouse_clicked(position, button)


    def on_mouse_move(self, position):
        for comp in self._components:
            comp.on_mouse_move(position)
