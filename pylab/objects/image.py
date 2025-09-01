import pylab
import pylab.entity

class Image(pylab.entity.Entity):

    def __init__(self, x:float=0.0, y:float=0.0, imagePath:str=""):
        super().__init__(x, y, [pylab.ImageDrawable(imagePath)])
