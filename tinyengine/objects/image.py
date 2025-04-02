import tinyengine
import tinyengine.components
import tinyengine.components.imagedrawable
import tinyengine.entity

class Image(tinyengine.entity.Entity):

    def __init__(self, x:float=0.0, y:float=0.0, imagePath:str=""):
        super().__init__(x, y, [tinyengine.ImageDrawable(imagePath)])
