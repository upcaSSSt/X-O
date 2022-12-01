import pygame as pg

from src.const import settings
from src.const import colors
from src.cell import Cell


class Field:
    """"""

    def __init__(self):
        """"""
        self.__surface = pg.Surface((settings.SCREEN_SIZE, settings.SCREEN_SIZE))
        self.__rect = self.__surface.get_rect()

        self.__cells = [
            Cell((0, 0)),
            Cell((self.__rect.centerx - settings.CELL_SIZE // 2, 0)),
            Cell((self.__rect.topright[0] - settings.CELL_SIZE, 0)),
            Cell((0, self.__rect.centery - settings.CELL_SIZE // 2)),
            Cell(tuple(pos - settings.CELL_SIZE // 2
                       for pos in self.__rect.center)),
            Cell((self.__rect.midright[0] - settings.CELL_SIZE,
                  self.__rect.centery - settings.CELL_SIZE // 2)),
            Cell((0, self.__rect.bottomleft[1] - settings.CELL_SIZE)),
            Cell((self.__rect.centerx - settings.CELL_SIZE // 2,
                  self.__rect.midbottom[1] - settings.CELL_SIZE)),
            Cell((self.__rect.bottomright[0] - settings.CELL_SIZE,
                  self.__rect.bottomright[1] - settings.CELL_SIZE))
        ]

        self.__surface.fill(colors.VIOLET)

    def click_handler(self, figure):
        pass

    def blit_me(self, screen):
        """"""
        for cell in self.__cells:
            cell.blit_me(self.__surface)
        screen.blit(self.__surface, (0, 0))
