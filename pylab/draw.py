import pylab
import pygame.draw
import pygame.gfxdraw
from pygame.math import Vector2 as Vector2

# Unified interface for drawing primitives.

def circle(surface: pylab.Surface, colour: pylab.Colour, centerPoint: pylab.Point, size: int, thickness: int = 1):
    radius = size >> 1
    if (thickness > 1):
        pygame.gfxdraw.aacircle(surface, centerPoint[0], centerPoint[1], radius, colour)
        pygame.gfxdraw.aacircle(surface, centerPoint[0] - 1, centerPoint[1] - 1, radius - thickness + 1, colour)
        pygame.draw.circle(surface, colour, (centerPoint[0], centerPoint[1]), radius + 1, thickness)
    else:
        pygame.gfxdraw.aacircle(surface, centerPoint[0], centerPoint[1], int(radius), colour)


def filled_circle(surface: pylab.Surface, colour: pylab.Colour, centerPoint: pylab.Point, size: int):
    radius = size >> 1
    pygame.gfxdraw.aacircle(surface, centerPoint[0], centerPoint[1], radius, colour)
    pygame.gfxdraw.filled_circle(surface, centerPoint[0], centerPoint[1], radius, colour)


def ellipse(surface: pylab.Surface, colour: pylab.Colour, centerPoint: pylab.Point, width: int, height: int, thickness: int = 1):
    radiusX = width >> 1
    radiusY = height >> 1
    if (thickness > 1):
        pygame.gfxdraw.aaellipse(surface, centerPoint[0], centerPoint[1], radiusX, radiusY, colour)
        pygame.gfxdraw.aaellipse(surface, centerPoint[0] - 1, centerPoint[1] - 1, radiusX - thickness + 2, radiusY - thickness + 2, colour)
        pygame.draw.ellipse(surface, colour, (centerPoint[0] - radiusX, centerPoint[1] - radiusY, radiusX * 2 + 1, radiusY * 2 + 1), thickness)
    else:
        pygame.gfxdraw.aaellipse(surface, centerPoint[0], centerPoint[1], radiusX, radiusY, colour)


def filled_ellipse(surface: pylab.Surface, colour: pylab.Colour, centerPoint: pylab.Point, width: int, height: int):
    radiusX = width >> 1
    radiusY = height >> 1
    pygame.gfxdraw.aaellipse(surface, centerPoint[0], centerPoint[1], radiusX, radiusY, colour)
    pygame.gfxdraw.filled_ellipse(surface, centerPoint[0], centerPoint[1], radiusX + 1, radiusY + 1, colour)


def line(surface: pylab.Surface, colour: pylab.Colour, startPoint: pylab.Point, endPoint: pylab.Point, thickness: int = 1):
    if (thickness > 1):
        sp = pygame.Vector2(startPoint[0], startPoint[1])
        ep = pygame.Vector2(endPoint[0], endPoint[1])
        pygame.draw.line(surface, colour, sp, ep, thickness)
    else:
        pygame.draw.aaline(surface, colour, (startPoint[0], startPoint[1]), (endPoint[0], endPoint[1]))


def lines(surface: pylab.Surface, colour: pylab.Colour, points: list[pylab.Point], thickness: int = 1):
    pts = list(map(pygame.Vector2, points))
    if (thickness > 1):
        pygame.draw.lines(surface, colour, False, pts, thickness)
    else:
        pygame.draw.aalines(surface, colour, False, pts)


def pixel(surface: pylab.Surface, colour: pylab.Colour, point: pylab.Point):
    pygame.gfxdraw.pixel(surface, point[0], point[1], colour)


def polygon(surface: pylab.Surface, colour: pylab.Colour, points: list[pylab.Point], thickness: int = 1):
    pts = list(map(pygame.Vector2, points))
    if (thickness > 1):
        pygame.draw.polygon(surface, colour, pts, thickness)
    else:
        pygame.gfxdraw.aapolygon(surface, pts, colour)


def filled_polygon(surface: pylab.Surface, colour: pylab.Colour, points: list[pylab.Point]):
    pts = list(map(pygame.Vector2, points))
    pygame.gfxdraw.aapolygon(surface, pts, colour)
    pygame.gfxdraw.filled_polygon(surface, pts, colour)


def rectangle(surface: pylab.Surface, colour: pylab.Colour, topLeftPoint: pylab.Point, width: int, height: int, thickness: int = 1):
    pygame.draw.rect(surface, colour, (topLeftPoint[0], topLeftPoint[1], width, height), thickness)


def filled_rectangle(surface: pylab.Surface, colour: pylab.Colour, topLeftPoint: pylab.Point, width: int, height: int):
    pygame.gfxdraw.box(surface, (topLeftPoint[0], topLeftPoint[1], width, height), colour)


def test(surface: pylab.Surface):
    x = 0
    y = 0
    w = 80
    h = 80
    hw = w >> 1
    hh = h >> 1
    qw = hw >> 1
    qh = hh >> 1

    c = (255, 255, 255)
    
    circle(surface, c, (x + hw, y + hh), w)
    x += w

    circle(surface, c, (x + hw, y + hh), w, qw)
    x += w

    filled_circle(surface, c, (x + hw, y + hh), w)
    x = 0
    y += h

    ellipse(surface, c, (x + hw, y + hh), w, hh)
    x += w

    ellipse(surface, c, (x + hw, y + hh), w, hh, qh >> 1)
    x += w

    filled_ellipse(surface, c, (x + hw, y + hh), w, hh)
    x = 0
    y += h

    line(surface, c, (x, y), (x + w, y + h))
    x += w

    line(surface, c, (x + 5, y), (x + w - 5, y + h), 10)
    x += w

    lines(surface, c, ((x + hw, y), (x, y + hh), (x + hw, y + w), (x + w, y + hh)))
    x += w

    lines(surface, c, ((x + hw, y), (x + 5, y + hh), (x + hw, y + w), (x + w - 5, y + hh)), 10)
    x = 0
    y += h

    pixel(surface, c, (x + hw, y + hh))
    x += w

    polygon(surface, c, (
            (x + hw, y),
            (x + qw*1.5, y + qh*1.5),
            (x, y + hh),
            (x + qw*1.5, y + hh + qh*0.5),
            (x + hw, y + h),
            (x + hw + qw*0.5, y + hh + qh*0.5),
            (x + w, y + hh),
            (x + hw + qw*0.5, y + qw*1.5)
        )
    )
    x += w

    polygon(surface, c, (
            (x + hw, y),
            (x + qw*1.5, y + qh*1.5),
            (x + 3, y + hh),
            (x + qw*1.5, y + hh + qh*0.5),
            (x + hw, y + h),
            (x + hw + qw*0.5, y + hh + qh*0.5),
            (x + w - 3, y + hh),
            (x + hw + qw*0.5, y + qw*1.5)
        ),
        10
    )
    x += w

    filled_polygon(surface, c, (
            (x + hw, y),
            (x + qw*1.5, y + qh*1.5),
            (x, y + hh),
            (x + qw*1.5, y + hh + qh*0.5),
            (x + hw, y + h),
            (x + hw + qw*0.5, y + hh + qh*0.5),
            (x + w, y + hh),
            (x + hw + qw*0.5, y + qw*1.5)
        )
    )
    x = 0
    y += h

    rectangle(surface, c, (x+5, y+5), w-10, h-10)
    x += w

    rectangle(surface, c, (x+5, y+5), w-10, h-10, 10)
    x += w

    filled_rectangle(surface, c, (x+5, y+5), w-10, h-10)
    x = 0
    y += h
