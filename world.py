import pygame as pg
from vector import fVector2 as fVec2
from vector import iVector2 as iVec2

class World:
    def __init__(self, size: iVec2, grid_size: int) -> None:
        self.size = size
        self.grid_size = grid_size

        self.surface = pg.Surface((size.x, size.y))

