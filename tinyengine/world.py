import pygame
import tinyengine.component
import tinyengine.entity
import tinyengine.input

class World(tinyengine.input.InputListener):

    objects : list[tinyengine.entity.Entity] = []

    def __init__(self):
        return
    
    def start(self):
        return

    def draw(self, surface : pygame.Surface):
        for object in self.objects:
            object.draw(surface)


    def update(self, deltaTime : float):
        for object in self.objects:
            object.update(deltaTime)


    def on_key_down(self, key):
        for object in self.objects:
            object.on_key_down(key)


    def on_key_up(self, key):
        for object in self.objects:
            object.on_key_up(key)


    def on_key_held(self, key):
        for object in self.objects:
            object.on_key_held(key)
    

    def on_mouse_down(self, pos, button):
        for object in self.objects:
            object.on_mouse_down(pos, button)
    
    
    def on_mouse_up(self, pos, button):
        for object in self.objects:
            object.on_mouse_up(pos, button)


    def on_mouse_clicked(self, pos, button):
        for object in self.objects:
            object.on_mouse_clicked(pos, button)


    def on_mouse_move(self, pos):
        for object in self.objects:
            object.on_mouse_move(pos)

    
    def add_objects(self, *objects : tinyengine.entity.Entity):
        for object in objects:
            self.objects.append(object)
            object.start()
    
    def add_object(self, x : float = 0.0, y : float = 0.0, components : list[tinyengine.component.Component] = []):
        self.add_objects(
            tinyengine.Entity(x, y, components)
        )
