import pygame.gfxdraw
import tinyengine

from tinyengine.objects.button import Button
from tinyengine.objects.mousedisplay import MouseDisplay

# ======================================================================================= #
# Player is our player character. It doesn't do much right now, but we can work on it.
# ======================================================================================= #
class Player(tinyengine.Entity):

    def __init__(self):
        super().__init__(
            400, 300,
            [
                  tinyengine.ImageDrawable(tinyengine.res_path("res/character.png"), 64, 64)
            ])


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

printdraw=False
printupdate=False
printmousemove=False
printkeyheld=False

def on_start(game):
     game.world.add_objects(MouseDisplay())

     # Setup the game
     game.world.add_objects(
          MyButton(x=10, y=10, width=200, height=25, text="My Button"),
          Player())


def on_draw(game, surface):
     global printdraw

     if printdraw:
          print("DRAW")
          printdraw = False


def on_update(game, deltaTime):
     global printupdate

     if printupdate:
          print("UPDATE")
          printupdate = False


def on_key_down(game, key):
     print("KEY DOWN")


def on_key_held(game, key):
     global printdraw
     global printkeyheld
     global printmousemove
     global printupdate

     if key is pygame.K_d:
          printdraw = True

     if key is pygame.K_k:
          printkeyheld = True

     if key is pygame.K_m:
          printmousemove = True
     
     if key is pygame.K_u:
          printupdate = True

     if printkeyheld:
          print("KEY HELD")


def on_key_up(game, key):
     global printdraw
     global printkeyheld
     global printmousemove
     global printupdate

     print("KEY UP")

     printdraw = False
     printkeyheld = False
     printmousemove = False
     printupdate = False


def on_mouse_clicked(game, pos, button):
     print("MOUSE CLICKED")


def on_mouse_down(game, pos, button):
     print("MOUSE DOWN")


def on_mouse_move(game, pos):
     global printmousemove

     if printmousemove:
          print("MOUSE MOVE")
          printmousemove = False


def on_mouse_up(game, pos, button):
     print("MOUSE UP")


# ======================================================================================= #
# Launch the game.
# ======================================================================================= #
tinyengine.Game().launch(
    title="DemoGame",
    backgroundColor = (94, 94, 94),
    windowSize = (800, 600))
