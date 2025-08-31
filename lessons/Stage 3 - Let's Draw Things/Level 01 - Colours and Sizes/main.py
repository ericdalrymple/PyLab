from tinyengine import *

#                     STAGE 3                     #
# =============================================== #
# ======== LESSON 01: Colours and Sizes ========= #
# =============================================== #

# Welcome to Stage 2! Now things are getting really exciting! For the first time, our
# program willdraw something instead of just writing.

# Let's pick a title for our game.
game_title = "My Game"


# Let's pick a background colour for our screen. All colours on a computer can be made
# by mixing red, green, and blue. A colour written this way is called an RGB colour (RedGreenBlue).
#
# The numbers for the red, the green, and the blue are between 0 and 255. You can try to
# mix them to make different colours. Here are some examples:
#
#   BLACK : r=0  , g=0  , b=0
#   WHITE : r=255, g=255, b=255
#   GRAY  : r=127, g=127, b=127
#   YELLOW: r=255, g=255, b=0
#   ORANGE: r=255, g=127, b=0
#
# You can use a colour picker to see the RGB numbers for different colors: https://rgbcolorpicker.com/
#
red = 0
green = 0
blue = 0
colour = (red, green, blue)


# Let's pick a size for our screen. The size of the screen is the number of pixels
# it will take up on your computer screen.
# 
# We usually give the width (how many pixels wide) first, then the height (how many pixels tall).
#
width = 800 #pixels wide
height = 600 #pixels tall
screen_size = (width, height)


# Show a game window using all the variables we set above.
Game().launch(
    title = game_title,
    backgroundColor = colour,
    windowSize = screen_size)


# ======================================================================================= #
# EXERCISE:
#
#   Change the game window:
#       - Change the title, think of a cool name for a game.
#       - Change the background color by changing the 'red' 'green' 'blue' variables, try to make purple.
#       - Change the size, try to make the window the same size as your phone screen. 
#
# ======================================================================================= #