import pygame as pg

from src.const import settings
from src.const import colors


class Cell:
    """"""

    def __init__(self, pos):
        """"""
        self.__pos = pos
        self.__surface = pg.Surface((settings.CELL_SIZE, settings.CELL_SIZE))

        self.__surface.fill(colors.BLACK)

    def click_handler(self, figure):
        self.__surface = figure

    def blit_me(self, screen):
        screen.blit(self.__surface, self.__pos)
