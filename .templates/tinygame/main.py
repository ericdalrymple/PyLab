import os
import tinyengine

from tinyengine.objects.mousedisplay import MouseDisplay

Title = "_T_GAME_TITLE_T_"
BackgroundColour = (94, 94, 94)
WindowSize = (800, 600)

# ======================================================================================= #
# Here is where we can put code to control our game.
# ======================================================================================= #
class MyGame(tinyengine.Game):

    def on_start(self):
        # Add something to show us the mouse position
        self.world.add_objects(MouseDisplay())
        return


    def on_update(self, deltaTime):
        # This code will happen over and over again until the game is closed.
        # It should do things like move or change things around over time.
        return super().on_update(deltaTime)
    
    
    def on_draw(self, surface):
        # This code will happen over and over again until the game is closed.
        # It should draw things on the screen.
        return super().on_draw(surface)
    

    def on_key_down(self, key):
        # This code will happen every time a key on the keyboard is pressed down.
        return super().on_key_down(key)
    

    def on_key_up(self, key):
        # This code will happen every time a key on the keyboard is released.
        return super().on_key_up(key)
    

    def on_key_held(self, key):
        # This code will happen over and over again as long as a key on the keyboard is held down.
        return super().on_key_held(key)
    


# ======================================================================================= #
# Launch the game.
# ======================================================================================= #
MyGame().launch(
    title=Title,
    backgroundColor = BackgroundColour,
    windowSize = WindowSize,
    res_root=os.path.dirname(os.path.abspath(__file__)))
