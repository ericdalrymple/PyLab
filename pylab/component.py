import pylab.abstractentity

"""
Component
  Base class for all components that can be added to entities.
"""
class Component():

    # Properties
    entity : pylab.abstractentity.AbstractEntity = None

    def _setParent(self, entity : pylab.abstractentity.AbstractEntity):
        self.entity = entity

    def start(self):
        return

    def draw(self, surface):
        return

    def update(self, deltaTime):
        return

    def on_key_down(self, key):
        return

    def on_key_up(self, key):
        return

    def on_key_held(self, key):
        return
    
    def on_mouse_down(self, pos, button):
        return
        
    def on_mouse_up(self, pos, button):
        return

    def on_mouse_clicked(self, pos, button):
        return

    def on_mouse_move(self, pos):
        return