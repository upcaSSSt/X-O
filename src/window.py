import sys

import pygame as pg

from src.const import settings
from src.field import Field


class Window:
    """"""

    def __init__(self):
        """"""
        self.__screen = pg.display.set_mode(
            (settings.SCREEN_SIZE, settings.SCREEN_SIZE))
        pg.display.set_caption(settings.CAPTION)

        self.__field = Field()

    @staticmethod
    def close():
        """"""
        sys.exit()

    def update(self):
        """"""
        self.__field.blit_me(self.__screen)
        pg.display.flip()
