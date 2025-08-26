import os
import pygame
import sys
import tinyengine.input
import tinyengine.world

from sys import exit

class Game(tinyengine.input.InputListener):

    input = None
    res_root = ""
    world = tinyengine.world.World()

    # Virtual
    def on_start(self):
        return
    
    def on_draw(self, surface : pygame.Surface):
        return

    def on_update(self, deltaTime : float):
        return


    # Public
    def launch(self, title, backgroundColor : tuple, windowSize : tuple, res_root: str):
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

        # Resource root init
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(".")))
        self.res_root = os.path.join(base_path, res_root)

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


    def res_path(self, relative_path: str) -> str:
        return os.path.join(self.res_root, relative_path)


    # Protected
    def start(self):
        self.on_start()
        self.world.start()


    def draw(self, surface: pygame.Surface):
        self.world.draw(surface)
        self.on_draw(surface)


    def update(self, deltaTime : float):
        self.input.update(deltaTime)
        self.world.update(deltaTime)
        self.on_update(deltaTime)
