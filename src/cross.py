import pygame as pg

from const import settings
from src.xo import XO
from figure import Figure


class Cross(Figure):
    """"""

    def __init__(self):
        """"""
        super().__init__()

    def _draw(self):
        pg.draw.line(self.rect, settings.COLOR, (10, 10), (settings.CELL_SIZE - 10, settings.CELL_SIZE - 10), 5)
