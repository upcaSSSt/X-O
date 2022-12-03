import pygame as pg

from src.const import settings
from src.const import colors
from src.cell import Cell
from src.figure import Figure


class Field:
    """Класс для хранения игровой сетки и управления её клетками."""

    def __init__(self):
        """Создаёт поверхность, на которую рисуется сетка и её клетки,
        список клеток и свободных клеток, сохраняет координаты разных
        частей прямоугольника поверхности сетки, красит поверхность
        сетки."""
        self.__grid = pg.Surface((settings.SCREEN_SIZE, settings.SCREEN_SIZE))
        self.__coordinates = self.__grid.get_rect()

        self.__cells = [
            Cell((0, 0)),
            Cell((self.__coordinates.centerx - settings.CELL_SIZE // 2, 0)),
            Cell((self.__coordinates.topright[0] - settings.CELL_SIZE, 0)),
            Cell((0, self.__coordinates.centery - settings.CELL_SIZE // 2)),
            Cell(tuple(pos - settings.CELL_SIZE // 2
                       for pos in self.__coordinates.center)),
            Cell((self.__coordinates.midright[0] - settings.CELL_SIZE,
                  self.__coordinates.centery - settings.CELL_SIZE // 2)),
            Cell((0, self.__coordinates.bottomleft[1] - settings.CELL_SIZE)),
            Cell((self.__coordinates.centerx - settings.CELL_SIZE // 2,
                  self.__coordinates.midbottom[1] - settings.CELL_SIZE)),
            Cell((self.__coordinates.bottomright[0] - settings.CELL_SIZE,
                  self.__coordinates.bottomright[1] - settings.CELL_SIZE))
        ]
        self.__free_cells = self.__cells.copy()

        self.__grid.fill(colors.VIOLET)

    @property
    def get_n_free_cells(self):
        return len(self.__free_cells)

    def paint(self, painting_surface: pg.Surface):
        """Рисует клетки на поверхности сетки, рисует поверхность сетки
            на переданной поверхности.
        painting_surface: поверхность, на которой надо нарисовать
            поверхность сетки
        """
        for cell in self.__cells:
            cell.paint(self.__grid)
        painting_surface.blit(self.__grid, self.__coordinates)

    def index_move_handler(self, index_to_move: int, moving_figure: Figure):
        """Передаёт клетке по индексу фигуру, которой походили в данный
            момент и удаляет эту клетку из списка свободных.
        index_to_move: индекс клетки, в которую был сделан ход
        moving_figure: фигура, которой походили в данный момент, на её
            поверхности нарисован крестик или нолик
        """
        self.__free_cells[index_to_move].move_handler(moving_figure)
        del self.__free_cells[index_to_move]
