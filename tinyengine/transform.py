import tinyengine
import tinyengine.math.matrix22

class Transform():

    _m: tinyengine.math.matrix22.Matrix22 = tinyengine.math.matrix22.identity()

    _x: float = 0.0
    _y: float = 0.0

    _scale_x: float = 1.0
    _scale_y: float = 1.0

    _rotation: float = 0.0

    def __init__(self, x:float=0.0, y:float=0.0, scale_x:float=1.0, scale_y:float=1.0, rotation:float=0.0):
        self._x = x
        self._y = y
        self._scale_x = scale_x
        self._scale_y = scale_y
        self._rotation = rotation

    
    def translate(self, x:float=0.0, y:float=0.0):
        self._x += x
        self._y += y
    
    
    def scale(self, scale_x:float=1.0, scale_y:float=1.0):
        self._scale_x *= scale_x
        self._scale_y *= scale_y
    
    
    def rotate(self, rotation:float=0.0):
        self._rotation += rotation

        # Clamp the rotation
        full_rotation_count = (int)(self._rotation / 360)
        self._rotation -= full_rotation_count * 360
    

    def transform(self, xform:'Transform'):
        self._m = self._m.multiply(xform._m)
        

