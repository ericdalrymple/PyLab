import math
import tinyengine
import tinyengine.math.matrix

class Transform():

    _parent:'Transform' = None

    _local: tinyengine.math.matrix.Matrix33 = tinyengine.math.matrix.identity()

    _x: float = 0.0
    _y: float = 0.0

    _scale_x: float = 1.0
    _scale_y: float = 1.0

    _rotation: float = 0.0

    _dirty: bool = False

    def __init__(self, parent:'Transform'=None, x:float=0.0, y:float=0.0, scale_x:float=1.0, scale_y:float=1.0, rotation:float=0.0):
        self._parent = parent

        self._x = x
        self._y = y
        self._scale_x = scale_x
        self._scale_y = scale_y
        self._rotation = rotation
        self._dirty = True

    
    def get_global(self) -> tinyengine.math.matrix.Matrix33:
        if self._parent is None:
            return self.get_local()
        else:
            parent_m: tinyengine.Matrix33 = self._parent.get_global()
            return parent_m.multiply(self.get_local())

    
    def get_local(self) -> tinyengine.math.matrix.Matrix33:
        if (self._dirty):
            translated = tinyengine.math.matrix.from_position(self._x, self._y)
            rotated = tinyengine.math.matrix.from_rotation(self._rotation)
            scaled = tinyengine.math.matrix.from_scale(self._scale_x, self._scale_y)
            self._local = rotated.multiply(scaled).multiply(translated)
            self._dirty = False

        return self._local

    
    def is_dirty(self) -> bool:
        result: bool = False
        t: 'Transform' = self
        while not t is None:
            if t._dirty:
                return True
            t = t._parent

        return False


    def set_position(self, x:float, y: float):
        self._x = x
        self._y = y
        self._dirty = True
    
    
    def set_rotation(self, degrees:float):
        self._rotation = degrees
        self._dirty = True


    def set_scale(self, x:float, y:float):
        self._scale_x = x
        self._scale_y = y

        if (not math.isclose(self._scale_x, x)) or (not math.isclose(self._scale_y, y)):
            # Only recompute on perceptible change
            self._dirty = True


    def rotate(self, degrees:float):
        self._rotation += degrees

        # Clamp the rotation
        full_rotation_count = (int)(self._rotation / 360)
        self._rotation -= full_rotation_count * 360

        self._dirty = True
    
    
    def scale(self, scale_x:float=1.0, scale_y:float=1.0):
        self._scale_x *= scale_x
        self._scale_y *= scale_y
        self._dirty = True


    def transform(self, xform:'Transform'):
        self._local = self._m.multiply(xform._local)
        self._dirty = True
        

    def translate(self, x:float=0.0, y:float=0.0):
        self._x += x
        self._y += y
        self._dirty = True
