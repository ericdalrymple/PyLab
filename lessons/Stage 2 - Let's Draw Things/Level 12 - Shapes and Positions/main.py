import pygame.gfxdraw as draw
from tinyengine import *

# =============================================== #
# ======= LESSON 12: Shapes and Positions ======= #
# =============================================== #

# We learned how to show a screen, but now lets see if we can draw
# something a little more interesting. The screen will now show the mouse
# position to help you know the positions on the screen.

# ======================================================================================= #
# Here is where we can put objects in our game.
# ======================================================================================= #
class MyGame(tinyengine.Game):
    def on_start(self):
        self.world.add_object(MouseDisplay())
        self.world.add_object(Button(x=40, y=40, text="Help!"))
    
    def on_draw(self, surface):

        # Draw a blue circle of size 20 at x=400 and y=300
        draw.filled_circle(surface, 400, 300, 20, (0, 0, 255))


# Show a game window. You can use the same settings as level 11 here if you like.
MyGame().launch(
    title = "My Game",
    backgroundColor = (0, 0, 0),
    windowSize = (800, 600))

