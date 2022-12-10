import pygame as pg

from src.const import settings
from src.const import path
from src.cell import Cell


class Field:
    """Класс для хранения игровой сетки и управления её клетками."""

    def __init__(self):
        """Создаёт поверхность, на которую рисуется сетка и её клетки, список клеток и свободных клеток, сохраняет
        прямоугольник поверхности сетки, красит поверхность сетки."""
        self.__grid = pg.image.load(path.GRID).convert_alpha()
        self.__rect = self.__grid.get_rect()

        self.__cells = [
            Cell((0, 0)),
            Cell((self.__rect.centerx - settings.CELL_SIZE // 2, 0)),
            Cell((self.__rect.topright[0] - settings.CELL_SIZE, 0)),
            Cell((0, self.__rect.centery - settings.CELL_SIZE // 2)),
            Cell(tuple(pos - settings.CELL_SIZE // 2 for pos in self.__rect.center)),
            Cell((self.__rect.midright[0] - settings.CELL_SIZE, self.__rect.centery - settings.CELL_SIZE // 2)),
            Cell((0, self.__rect.bottomleft[1] - settings.CELL_SIZE)),
            Cell((self.__rect.centerx - settings.CELL_SIZE // 2, self.__rect.midbottom[1] - settings.CELL_SIZE)),
            Cell((self.__rect.bottomright[0] - settings.CELL_SIZE, self.__rect.bottomright[1] - settings.CELL_SIZE))
        ]
        self.__free_cells = self.__cells.copy()

        self.__grid.set_colorkey((0, 0, 0))  # ////

    @property
    def get_n_free_cells(self) -> int:
        return len(self.__free_cells)

    def paint(self, painting_surface: pg.Surface):
        """Рисует клетки на поверхности сетки, рисует поверхность сетки на переданной поверхности.
        painting_surface: поверхность, на которой надо нарисовать поверхность сетки
        """
        for cell in self.__cells:
            cell.paint(self.__grid)
        painting_surface.blit(self.__grid, self.__rect)

    def click_move_handler(self, click_pos: tuple, figure_path: str) -> bool:
        """Берёт первую клетку, попавшую под клик пользователя, передаёт ей путь к изображению фигуры, которой походили,
            удаляет эту клетку из списка свободных и возвращает True, если всё удалось, иначе False.
        click_pos: координаты клика
        figure_path: путь к изображению с фигурой, которой походили в данный момент
        """
        clicked_cells = [fc for fc in self.__free_cells if fc.rect.collidepoint(click_pos)]
        if len(clicked_cells) > 0:
            clicked_cells[0].move_handler(figure_path)
            self.__free_cells.remove(clicked_cells[0])
            return True
        return False

    def index_move_handler(self, index_to_move: int, figure_path: str):
        """Передаёт клетке по индексу путь к изображению фигуры, которой походили в данный момент и удаляет эту клетку
            из списка свободных.
        index_to_move: индекс клетки, в которую был сделан ход
        figure_path: путь к изображению с фигурой, которой походили в данный момент
        """
        self.__free_cells[index_to_move].move_handler(figure_path)
        del self.__free_cells[index_to_move]
