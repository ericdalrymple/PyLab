import pygame
import sys
import tinyengine.input
import tinyengine.world

from sys import exit

class Game(tinyengine.input.InputListener):

    input = None
    world = tinyengine.world.World()

    __callbacks = {}
    

    # Private
    def __get_callback__(self, name: str):
        # Lazy-fetch the callback matching the specified name from the main module.
        cb = self.__callbacks.get(name)
        if cb is None:
            # Cache the callback to avoid calling getattr every time
            cb = getattr(sys.modules['__main__'], name, None)
            self.__callbacks.update({name: cb})

        # Return the callback if found
        if not cb is None and callable(cb):
            return cb

        return None
    

    # Virtual
    def on_start(self):
        return
    
    def on_draw(self, surface : pygame.Surface):
        return

    def on_update(self, deltaTime : float):
        return

    def on_key_down(self, key):
        cb = self.__get_callback__('on_key_down')
        if not cb is None:
            cb(self, key)
    
    def on_key_held(self, key):
        cb = self.__get_callback__('on_key_held')
        if not cb is None:
            cb(self, key)
    
    def on_key_up(self, key):
        cb = self.__get_callback__('on_key_up')
        if not cb is None:
            cb(self, key)
    
    def on_mouse_clicked(self, pos, button):
        cb = self.__get_callback__('on_mouse_clicked')
        if not cb is None:
            cb(self, pos, button)
    
    def on_mouse_down(self, pos, button):
        cb = self.__get_callback__('on_mouse_down')
        if not cb is None:
            cb(self, pos, button)
    
    def on_mouse_move(self, pos):
        cb = self.__get_callback__('on_mouse_move')
        if not cb is None:
            cb(self, pos)
    
    def on_mouse_up(self, pos, button):
        cb = self.__get_callback__('on_mouse_up')
        if not cb is None:
            cb(self, pos, button)
    

    # Public
    def launch(self, title, backgroundColor : tuple, windowSize : tuple):
        # Game Settings
        fps = 60
        viewport = pygame.Surface(windowSize, pygame.SRCALPHA, 32)

        # Pygame init
        pygame.init()
        pygame.display.set_caption(title)
        screen = pygame.display.set_mode(windowSize)
        clock = pygame.time.Clock()

        # Input init
        self.input = tinyengine.InputDispatcher(0.1)
        self.input.addListener(self)
        self.input.addListener(self.world)

        # Start
        self.start()

        # Game loop
        while True:

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                elif event.type == pygame.KEYDOWN:
                    self.input.on_key_down(event.key)
                
                elif event.type == pygame.KEYUP:
                    self.input.on_key_up(event.key)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.input.on_mouse_down(event.pos, event.button)

                elif event.type == pygame.MOUSEBUTTONUP:
                    self.input.on_mouse_up(event.pos, event.button)
                
                elif event.type == pygame.MOUSEMOTION:
                    self.input.on_mouse_move(event.pos)

            # Logic
            self.update(clock.get_rawtime() / 1000)

            # Rendering
            viewport.fill(backgroundColor)
            self.draw(viewport)

            scaled_viewport = pygame.transform.smoothscale(viewport, screen.get_size())
            screen.blit(scaled_viewport, (0, 0))

            pygame.display.flip()
            clock.tick(fps)


    # Protected
    def start(self):
        self.on_start()
        self.world.start()

        cb = self.__get_callback__('on_start')
        if not cb is None:
            cb(self)


    def draw(self, surface: pygame.Surface):
        self.world.draw(surface)
        self.on_draw(surface)

        cb = self.__get_callback__('on_draw')
        if not cb is None:
            cb(self, surface)


    def update(self, deltaTime : float):
        self.input.update(deltaTime)
        self.world.update(deltaTime)
        self.on_update(deltaTime)

        cb = self.__get_callback__('on_update')
        if not cb is None:
            cb(self, deltaTime)
