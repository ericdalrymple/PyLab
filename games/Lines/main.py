import pylab
import pylab.draw as draw
import pylab.drawing.colours as colours


Title = "Lines"

# ---------------- (red,   green, blue)
BackgroundColour = (46,    46,    46)

# ---------- (width, height)
WindowSize = (800,   600)


# Use this code to draw things on the screen.
def on_draw(game, surface):

    # Draw a blue line.
    colour = (128, 128, 255)
    point1 = (300, 250)
    point2 = (500, 430)
    draw.line(surface, colour, point1, point2)

    draw.test(surface)















# ======================================================================================= #
# Launch the game.
# ======================================================================================= #
def on_start(game):
    # Add something to show us the mouse position
    game.world.add_objects(pylab.MouseDisplay())
    return

IconPath = pylab.res_path("res/icons/pylab.png")
pylab.Game().launch(
    title=Title,
    backgroundColor = BackgroundColour,
    windowSize = WindowSize,
    iconPath = IconPath)
