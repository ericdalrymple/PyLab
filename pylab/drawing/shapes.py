import pylab.drawing.colours as colours
import pylab.draw as draw

from pygame import Vector2

class Shape():

    colour: tuple = colours.black

    def draw(self, surface, x: float, y: float):
        return



class Circle(Shape):

    filled: bool = True
    radius: float = 1.0
    outline: int = 1

    def draw(self, surface, x: float, y: float):
        if self.filled:
            draw.filled_circle(surface, self.colour, Vector2(x, y), self.radius)
        else:
            draw.circle(surface, self.colour, Vector2(x, y), self.radius, self.outline)



class Ellipse(Shape):
    
    filled: bool = True
    width: float = 1.0
    height: float = 1.0
    outline: int = 1

    def draw(self, surface, x: float, y: float):
        if self.filled:
            draw.filled_ellipse(surface, self.colour, Vector2(x, y), (self.width >> 1), (self.height >> 1))
        else:
            draw.ellipse(surface, self.colour, Vector2(x, y), (self.width >> 1), (self.height >> 1), self.outline)



class Line(Shape):

    thickness: int = 1
    end_point: Vector2 = (1.0, 1.0)

    def draw(self, surface, x: float, y: float):
        draw.line(surface, self.colour, Vector2(x, y), Vector2(self.end_point.x, self.end_point.y), self.thickness)


    
class Rectangle(Shape):

    filled: bool = True
    width: float = 1.0
    height: float = 1.0
    outline: int = 1

    def draw(self, surface, x: float, y: float):
        if self.filled:
            draw.filled_rectangle(surface, self.colour, Vector2(x, y), self.width, self.height)
        else:
            draw.rectangle(surface, self.colour, Vector2(x, y), self.width, self.height, self.outline)
