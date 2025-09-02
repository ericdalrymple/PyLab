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
size = 20

speedX = 1
speedY = 1

def on_start(game):
    game.world.add_objects(MouseDisplay())


def on_draw(game, surface):
    global x, y, size, speedX, speedY

    # Move the ball
    x += speedX
    y += speedY

    if y + size < 0:
        y = 600 + size

    # Bring the ball back to the top
    if y - size > 600:
        y = -size
    
    # Bounce the ball off the sides
    if x - size < 0 or x + size > 800:
        speedX *= -1

    # Draw the blue ball
    draw.filled_circle(surface, x, y, size, (0, 0, 255))



# Show a game window. You can use the same settings as level 11 here if you like.
Game().launch(
    title = "My Game",
    backgroundColor = (0, 0, 0),
    windowSize = (800, 600))

