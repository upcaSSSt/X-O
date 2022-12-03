import sys

import pygame as pg

from src.const import settings
from src.const import path
from src.ai import AI
from src.field import Field
from src.figure import Figure


class XO:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """"""
        pg.init()

        self.__screen = pg.display.set_mode(
            (settings.SCREEN_SIZE, settings.SCREEN_SIZE))
        pg.display.set_caption(settings.CAPTION)

        self.__ai = AI()

        self.__field = Field()

        self.__cross = Figure(path.CROSS)
        self.__nought = Figure(path.NOUGHT)

        self.__field.press_handler(self.__ai.move(self.__field.get_n_cells),
                                   self.__cross)
        self.__field.press_handler(self.__ai.move(self.__field.get_n_cells),
                                   self.__nought)

    def run(self):
        """Запуск основного цикла игры"""
        while True:
            self.__event_handler()
            self.__update_screen()

    def __event_handler(self):
        """Обрабатывает события мыши"""
        for e in pg.event.get():
            if e.type == pg.QUIT:
                sys.exit()

    def __update_screen(self):
        """Обновляет изображения на экране и отображает новый экран"""
        self.__field.paint(self.__screen)
        pg.display.flip()
