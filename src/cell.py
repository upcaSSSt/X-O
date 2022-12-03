import pygame as pg

from src.const import settings
from src.const import colors
from src.figure import Figure


class Cell:
    """"""

    def __init__(self, pos: tuple):
        """"""
        self.__pos = pos
        self.__figure = pg.Surface((settings.CELL_SIZE, settings.CELL_SIZE))

        self.__figure.fill(colors.BLACK)

    def paint(self, painting_grid: pg.Surface):
        """Рисует на переданной сетке текущую клетку

            Параметры:
                painting_grid (Surface): сетка, на которую надо нарисовать
                    поверхность текущей фигуры
        """
        painting_grid.blit(self.__figure, self.__pos)

    def move_handler(self, moving_figure: Figure):
        """"""
        self.__figure = moving_figure.get_figure
