import pygame as pg

from src.const import settings
from src.const import colors
from src.figure import Figure


class Cell:
    """Класс для создания клетки и получения фигуры для неё."""

    def __init__(self, pos: tuple):
        """Сохраняет координаты клетки на поверхности сетки, создаёт
            поверхность, на которой будет нарисована фигура и красит её.
        pos: координаты, по которым будет располагаться клетка на
            поверхности сетки
        """
        self.__pos = pos
        self.__figure = pg.Surface((settings.CELL_SIZE, settings.CELL_SIZE))

        self.__figure.fill(colors.BLACK)

    def paint(self, painting_grid: pg.Surface):
        """Рисует клетку на переданной поверхности сетки.
        painting_grid: поверхность сетки, на которой надо нарисовать
            поверхность клетки
        """
        painting_grid.blit(self.__figure, self.__pos)

    def move_handler(self, moving_figure: Figure):
        """Присваивает поверхности клетки поверхность переданной фигуры.
        moving_figure: фигура, которой походили в данный момент, на её
            поверхности нарисован крестик или нолик
        """
        self.__figure = moving_figure.get_surface
