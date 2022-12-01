from abc import ABC, abstractmethod

import pygame as pg

from const import settings


class Figure(ABC):
    """"""

    def __init__(self):
        """"""
        self.rect = pg.Rect((0, 0, settings.CELL_SIZE, settings.CELL_SIZE))#////
        self._draw()

    @abstractmethod
    def _draw(self):
        pass
