import pygame.draw
import pygame.gfxdraw
from pygame.math import Vector2 as Vector2

# Unified interface for drawing primitives.

def circle(surface: pygame.Surface, color: pygame.Color, centerPoint: Vector2, radius: int, thickness: int = 1):
    if (thickness > 1):
        pygame.gfxdraw.aacircle(surface, int(centerPoint.x), int(centerPoint.y), radius, color)
        pygame.gfxdraw.aacircle(surface, int(centerPoint.x) - 1, int(centerPoint.y) - 1, radius - thickness + 1, color)
        pygame.draw.circle(surface, color, (int(centerPoint.x), int(centerPoint.y)), radius + 1, thickness)
    else:
        pygame.gfxdraw.aacircle(surface, int(centerPoint.x), int(centerPoint.y), int(radius), color)


def filled_circle(surface: pygame.Surface, color: pygame.Color, centerPoint: Vector2, radius: int):
    pygame.gfxdraw.aacircle(surface, int(centerPoint.x), int(centerPoint.y), radius, color)
    pygame.gfxdraw.filled_circle(surface, int(centerPoint.x), int(centerPoint.y), radius, color)


def ellipse(surface: pygame.Surface, color: pygame.Color, centerPoint: Vector2, radiusX: int, radiusY: int, thickness: int = 1):
    if (thickness > 1):
        pygame.gfxdraw.aaellipse(surface, int(centerPoint.x), int(centerPoint.y), radiusX, radiusY, color)
        pygame.gfxdraw.aaellipse(surface, int(centerPoint.x) - 1, int(centerPoint.y) - 1, radiusX - thickness + 2, radiusY - thickness + 2, color)
        pygame.draw.ellipse(surface, color, (int(centerPoint.x - radiusX), int(centerPoint.y - radiusY), radiusX * 2 + 1, radiusY * 2 + 1), thickness)
    else:
        pygame.gfxdraw.aaellipse(surface, int(centerPoint.x), int(centerPoint.y), radiusX, radiusY, color)


def filled_ellipse(surface: pygame.Surface, color: pygame.Color, centerPoint: Vector2, radiusX: int, radiusY: int):
    pygame.gfxdraw.aaellipse(surface, int(centerPoint.x), int(centerPoint.y), radiusX, radiusY, color)
    pygame.gfxdraw.filled_ellipse(surface, int(centerPoint.x), int(centerPoint.y), radiusX + 1, radiusY + 1, color)


def line(surface: pygame.Surface, color: pygame.Color, startPoint: Vector2, endPoint: Vector2, thickness: int = 1):
    if (thickness > 1):
        pygame.draw.line(surface, color, startPoint, endPoint, thickness)
    else:
        pygame.draw.aaline(surface, color, (startPoint.x, startPoint.y), (endPoint.x, endPoint.y))


def lines(surface: pygame.Surface, color: pygame.Color, points: list[Vector2], thickness: int = 1):
    if (thickness > 1):
        pygame.draw.lines(surface, color, False, points, thickness)
    else:
        pygame.draw.aalines(surface, color, False, points)


def pixel(surface: pygame.Surface, color: pygame.Color, point: Vector2):
    pygame.gfxdraw.pixel(surface, int(point.x), int(point.y), color)


def polygon(surface: pygame.Surface, color: pygame.Color, points: list[Vector2], thickness: int = 1):
    if (thickness > 1):
        pygame.draw.polygon(surface, color, points, thickness)
    else:
        pygame.gfxdraw.aapolygon(surface, points, color)


def filled_polygon(surface: pygame.Surface, color: pygame.Color, points: list[Vector2]):
    pygame.gfxdraw.aapolygon(surface, points, color)
    pygame.gfxdraw.filled_polygon(surface, points, color)


def rectangle(surface: pygame.Surface, color: pygame.Color, topLeftPoint: Vector2, width: int, height: int, thickness: int = 1):
    pygame.draw.rect(surface, color, (int(topLeftPoint.x), int(topLeftPoint.y), width, height), thickness)


def filled_rectangle(surface: pygame.Surface, color: pygame.Color, topLeftPoint: Vector2, width: int, height: int):
    pygame.gfxdraw.box(surface, (int(topLeftPoint.x), int(topLeftPoint.y), width, height), color)


def test(surface: pygame.Surface):
    x = 0
    y = 0
    w = 80
    h = 80
    hw = w >> 1
    hh = h >> 1
    qw = hw >> 1
    qh = hh >> 1

    c = (255, 255, 255)
    
    circle(surface, c, Vector2(x + hw, y + hh), hw)
    x += w

    circle(surface, c, Vector2(x + hw, y + hh), hw, qw)
    x += w

    filled_circle(surface, c, Vector2(x + hw, y + hh), hw)
    x = 0
    y += h

    ellipse(surface, c, Vector2(x + hw, y + hh), hw, qh)
    x += w

    ellipse(surface, c, Vector2(x + hw, y + hh), hw, qh, qh >> 1)
    x += w

    filled_ellipse(surface, c, Vector2(x + hw, y + hh), hw, qh)
    x = 0
    y += h

    line(surface, c, Vector2(x, y), Vector2(x + w, y + h))
    x += w

    line(surface, c, Vector2(x + 5, y), Vector2(x + w - 5, y + h), 10)
    x += w

    lines(surface, c, (Vector2(x + hw, y), Vector2(x, y + hh), Vector2(x + hw, y + w), Vector2(x + w, y + hh)))
    x += w

    lines(surface, c, (Vector2(x + hw, y), Vector2(x + 5, y + hh), Vector2(x + hw, y + w), Vector2(x + w - 5, y + hh)), 10)
    x = 0
    y += h

    pixel(surface, c, Vector2(x + hw, y + hh))
    x += w

    polygon(surface, c, (
        Vector2(x + hw, y),
        Vector2(x + qw*1.5, y + qh*1.5),
        Vector2(x, y + hh),
        Vector2(x + qw*1.5, y + hh + qh*0.5),
        Vector2(x + hw, y + h),
        Vector2(x + hw + qw*0.5, y + hh + qh*0.5),
        Vector2(x + w, y + hh),
        Vector2(x + hw + qw*0.5, y + qw*1.5)
    ))
    x += w

    polygon(surface, c, (
            Vector2(x + hw, y),
            Vector2(x + qw*1.5, y + qh*1.5),
            Vector2(x + 3, y + hh),
            Vector2(x + qw*1.5, y + hh + qh*0.5),
            Vector2(x + hw, y + h),
            Vector2(x + hw + qw*0.5, y + hh + qh*0.5),
            Vector2(x + w - 3, y + hh),
            Vector2(x + hw + qw*0.5, y + qw*1.5)
        ),
        10)
    x += w

    filled_polygon(surface, c, (
        Vector2(x + hw, y),
        Vector2(x + qw*1.5, y + qh*1.5),
        Vector2(x, y + hh),
        Vector2(x + qw*1.5, y + hh + qh*0.5),
        Vector2(x + hw, y + h),
        Vector2(x + hw + qw*0.5, y + hh + qh*0.5),
        Vector2(x + w, y + hh),
        Vector2(x + hw + qw*0.5, y + qw*1.5)
    ))
    x = 0
    y += h

    rectangle(surface, c, Vector2(x+5, y+5), w-10, h-10)
    x += w

    rectangle(surface, c, Vector2(x+5, y+5), w-10, h-10, 10)
    x += w

    filled_rectangle(surface, c, Vector2(x+5, y+5), w-10, h-10)
    x = 0
    y += h
