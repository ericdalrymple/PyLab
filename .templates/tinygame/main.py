import pygame
import pylab
import pylab.drawing.colours as colours
import pylab.drawing.shapes as shapes



Title = "_T_GAME_TITLE_T_"
BackgroundColour = (94, 94, 94)     # (red, green, blue)
WindowSize = (800, 600)             # (x, y)



# ======================================================================================= #
# Here is where we can put code to control our game.
# ======================================================================================= #

# This code will happen when the game starts.
def on_start(game):
    # Add something to show us the mouse position
    game.world.add_objects(pylab.MouseDisplay())
    return


# This code will happen over and over again until the game is closed.
# It should do things like move or change things around over time.
def on_update(game, deltaTime):
    return


# This code will happen over and over again until the game is closed.
# It should draw things on the screen.
def on_draw(game, surface):
    return






# This code will happen every time a key on the keyboard is pressed down.
def on_key_down(game, key):
    return


# This code will happen every time a key on the keyboard is released.
def on_key_up(game, key):
    return


# This code will happen over and over again as long as a key on the keyboard is held down.
def on_key_held(game, key):
    return


# This code will happen every time a mouse button is clicked.
def on_mouse_clicked(game, pos, button):
    return


# This code will happen every time a mouse button is pressed down.
def on_mouse_down(game, pos, button):
    return


# This code will happen every time a mouse button is released.
def on_mouse_up(game, pos, button):
    return


# This code will happen every time the cursor moved on the game surface.
def on_mouse_move(game, pos):    
    return






# ======================================================================================= #
# Launch the game.
# ======================================================================================= #
pylab.Game().launch(
    title=Title,
    backgroundColor = BackgroundColour,
    windowSize = WindowSize)
