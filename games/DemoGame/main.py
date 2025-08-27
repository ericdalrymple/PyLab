import os
import pygame.gfxdraw
import tinyengine

from tinyengine.objects.button import Button
from tinyengine.objects.mousedisplay import MouseDisplay

# ======================================================================================= #
# Player is our player character. It doesn't do much right now, but we can work on it.
# ======================================================================================= #
class Player(tinyengine.Entity):

    def __init__(self):
        super().__init__(0, 0, [])
    

    def draw(self, surface):
            pygame.gfxdraw.filled_circle(surface, 400, 300, 25, (0, 0, 255))


# ======================================================================================= #
# Player is our player character. It doesn't do much right now, but we can work on it.
# ======================================================================================= #
class MyButton(Button):

    def on_button_clicked(self):

        # Make the button do something.
        print("Button clicked!")

        return
    

# ======================================================================================= #
# Here is where we can put objects in our game.
# ======================================================================================= #
class MyGame(tinyengine.Game):

    def on_start(self):
        # Add something to show us the mouse position
        self.world.add_objects(MouseDisplay())

        # Setup the game
        self.world.add_objects(
            MyButton(x=10, y=10, width=200, height=25, text="My Button"),
            Player(),
            tinyengine.Image(300, 100, self.res_path("res/character.png")))
        

# ======================================================================================= #
# Launch the game.
# ======================================================================================= #
MyGame().launch(
    title="DemoGame",
    backgroundColor = (94, 94, 94),
    windowSize = (800, 600),
    res_root=os.path.dirname(os.path.abspath(__file__)))
