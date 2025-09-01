import pygame.gfxdraw as draw
from pylab import *

#                     STAGE 3                     #
# =============================================== #
# ============= LESSON 03: Movement ============= #
# =============================================== #

# We learned how to show a screen, but now lets see if we can draw
# something a little more interesting. The screen will now show the mouse
# position to help you know the positions on the screen.

x = 400
y = 300
radius = 20

speedX = 1
speedY = 1

def on_start(game):
    game.world.add_objects(MouseDisplay())


def on_draw(game, surface):

    # Move the ball
    x += speedX
    y += speedY

    if y + radius < 0:
        y = 600 + radius

    # Bring the ball back to the top
    if y - radius > 600:
        y = -radius
    
    # Bounce the ball off the sides
    if x - radius < 0 or x + radius > 800:
        speedX *= -1

    # Draw the blue ball
    draw.filled_circle(surface, x, y, radius, (0, 0, 255))



# Show a game window. You can use the same settings as level 11 here if you like.
Game().launch(
    title = "My Game",
    backgroundColor = (0, 0, 0),
    windowSize = (800, 600),
    callbacks = {
        "start" : on_start,
        "draw" : on_draw
    })

