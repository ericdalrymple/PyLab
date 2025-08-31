# Core
import tinyengine.abstractentity
import tinyengine.component
import tinyengine.entity
import tinyengine.game
import tinyengine.input
import tinyengine.transform
import tinyengine.world

AbstractEntity = tinyengine.abstractentity.AbstractEntity
Component = tinyengine.component.Component
Entity = tinyengine.entity.Entity
Game = tinyengine.game.Game
InputListener = tinyengine.input.InputListener
InputDispatcher = tinyengine.input.InputDispatcher
Transform = tinyengine.transform.Transform
World = tinyengine.world.World


# Components
import tinyengine.components.arrowmovable
import tinyengine.components.defaultdrawable
import tinyengine.components.imagedrawable


ArrowMovable = tinyengine.components.arrowmovable.ArrowMovable
DefaultDrawable = tinyengine.components.defaultdrawable.DefaultDrawable
ImageDrawable = tinyengine.components.imagedrawable.ImageDrawable


# Math
import tinyengine.math.matrix

Matrix33 = tinyengine.math.matrix.Matrix33


# Object
import tinyengine.objects.button
import tinyengine.objects.image
import tinyengine.objects.mousedisplay

Button = tinyengine.objects.button.Button
Image = tinyengine.objects.image.Image
MouseDisplay = tinyengine.objects.mousedisplay.MouseDisplay

# Resource path mapping
import os
import sys
__module_dir = os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__))
__base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(".")))
__root_dir = os.path.join(__base_path, __module_dir)

def res_path(relative_path):
    return os.path.join(__root_dir, relative_path)
