import sys

import pygame as pg

from src.const import settings
from src.const import path
from src.ai import AI
from src.field import Field


class XO:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создаёт игровые объекты."""
        pg.init()

        self.__screen = pg.display.set_mode((settings.SCREEN_SIZE, settings.SCREEN_SIZE))

        self.__ai = AI()
        self.__field = Field()

        pg.display.set_caption(settings.CAPTION)

    def run(self):
        """Запуск основного цикла игры."""
        while True:
            self.__event_handler()
            self.__update_screen()

    def __event_handler(self):
        """Обрабатывает события мыши."""
        for e in pg.event.get():
            if e.type == pg.QUIT:
                sys.exit()
            if e.type == pg.MOUSEBUTTONDOWN:
                if self.__field.click_move_handler(pg.mouse.get_pos(), path.CROSS):
                    if self.__field.get_n_free_cells > 0:  # убрать////
                        self.__field.index_move_handler(self.__ai.move(self.__field.get_n_free_cells), path.NOUGHT)

    def __update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        self.__field.paint(self.__screen)
        pg.display.flip()
