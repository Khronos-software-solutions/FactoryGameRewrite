import pygame as pg
from vector import fVector2 as vec2

class Player:
    pos: vec2 = vec2(0, 0)
    size: vec2 = vec2(800, 600)
    def __init__(self, pos: vec2, size: vec2) -> None:
        self.pos = pos
        self.size = size
        self.rect = pg.Rect((pos.x, pos.y), (size.x, size.y))

    def move(self, fac: vec2):
        self.pos = self.pos + fac
    
