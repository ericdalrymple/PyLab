import pylab
import pylab.draw as draw

#                     STAGE 3                     #
# =============================================== #
# ======= LESSON 02: Shapes and Positions ======= #
# =============================================== #

# We learned how to show a screen, but now lets see if we can draw
# something a little more interesting. The screen will now show the mouse
# position to help you know the positions on the screen.

# ======================================================================================= #
# Here is where we can put objects in our game.
# ======================================================================================= #
def on_start(game):
    game.world.add_objects(pylab.MouseDisplay())

def on_draw(game, surface):

    # Draw a blue circle of radius 20 at x=400 and y=300
    draw.filled_circle(surface, (0, 0, 255), (400, 300), 20)

    # Draw a green circle of radius 32 at x=0 and y=500
    draw.circle(surface, (0, 255, 0), (0, 500), 32)

    # Draw a red 50x50 square at x=100 and y=200
    draw.rectangle(surface, (255, 0, 0), (100, 200), 50, 50)


# Show a game window. You can use the same settings as level 11 here if you like.
pylab.Game().launch(
    title = "My Game",
    backgroundColor = (0, 0, 0),
    windowSize = (800, 600))

