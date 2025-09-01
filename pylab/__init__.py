# Core
import pylab.abstractentity
import pylab.component
import pylab.entity
import pylab.game
import pylab.input
import pylab.transform
import pylab.world

AbstractEntity = pylab.abstractentity.AbstractEntity
Component = pylab.component.Component
Entity = pylab.entity.Entity
Game = pylab.game.Game
InputListener = pylab.input.InputListener
InputDispatcher = pylab.input.InputDispatcher
Transform = pylab.transform.Transform
World = pylab.world.World


# Components
import pylab.components.arrowmovable
import pylab.components.defaultdrawable
import pylab.components.imagedrawable


ArrowMovable = pylab.components.arrowmovable.ArrowMovable
DefaultDrawable = pylab.components.defaultdrawable.DefaultDrawable
ImageDrawable = pylab.components.imagedrawable.ImageDrawable


# Math
import pylab.math.matrix

Matrix33 = pylab.math.matrix.Matrix33


# Object
import pylab.objects.button
import pylab.objects.image
import pylab.objects.mousedisplay

Button = pylab.objects.button.Button
Image = pylab.objects.image.Image
MouseDisplay = pylab.objects.mousedisplay.MouseDisplay

# Resource path mapping
import os
import sys
__module_dir = os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__))
__base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(".")))
__root_dir = os.path.join(__base_path, __module_dir)

def res_path(relative_path):
    return os.path.join(__root_dir, relative_path)
