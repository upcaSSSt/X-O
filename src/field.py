from typing import Tuple
from typing import List

from pygame.image import load
from pygame import Surface

from src.const import settings
from src.const import path
from src.cell import Cell
from src.counter import Counter


class Field(Surface):
    """Класс для создания игровой сетки и управления её клетками."""

    def __init__(self):
        """Рисует сетку, сохраняет её прямоугольник, создаёт списки для хранения счетчиков каждой фигуры, для хранения
        клеток, по которым кликнули, список клеток, инициализирует клетки, делает пространство с клетками прозрачным."""
        super(Field, self).__init__((settings.SCREEN_SIZE, settings.SCREEN_SIZE))
        self.blit(load(path.GRID).convert_alpha(), (0, 0))

        self.__rect = self.get_rect()

        self.__cur_figure_counters, self.__next_figure_counters, self.__clicked_cells = [], [], []

        counters = [Counter() for _ in range(8)]

        self.__cells = [  # Нечитабельно :(.
            Cell((0, 0), [counters[0], counters[3], counters[6]]),
            Cell((self.__rect.centerx - settings.CELL_SIZE // 2, 0), [counters[1], counters[3]]),
            Cell((self.__rect.topright[0] - settings.CELL_SIZE, 0), [counters[2], counters[3], counters[7]]),
            Cell((0, self.__rect.centery - settings.CELL_SIZE // 2), [counters[0], counters[4]]),
            Cell((self.__rect.centerx - settings.CELL_SIZE // 2, self.__rect.centery - settings.CELL_SIZE // 2),
                 [counters[1], counters[4], counters[6], counters[7]]),
            Cell((self.__rect.midright[0] - settings.CELL_SIZE, self.__rect.centery - settings.CELL_SIZE // 2),
                 [counters[2], counters[4]]),
            Cell((0, self.__rect.bottomleft[1] - settings.CELL_SIZE), [counters[0], counters[5], counters[7]]),
            Cell((self.__rect.centerx - settings.CELL_SIZE // 2, self.__rect.midbottom[1] - settings.CELL_SIZE),
                 [counters[1], counters[5]]),
            Cell((self.__rect.bottomright[0] - settings.CELL_SIZE, self.__rect.bottomright[1] - settings.CELL_SIZE),
                 [counters[2], counters[5], counters[6]])
        ]

        self.set_colorkey(0)

    @property
    def get_n_cells(self) -> int:
        return len(self.__cells)

    def has_clicked_cell(self, click_pos: Tuple[int, int]) -> bool:  # ////nn
        """"""
        self.__clicked_cells = [c for c in self.__cells if c.is_clicked(click_pos)]
        return len(self.__clicked_cells) > 0

    def move_by_click(self, figure: Surface) -> None:
        """Обновляет счётчики клетки, по которой кликнули, передаёт ей поверхность фигуры, которой походили, рисует на
            сетке обновлённую версию клетки, удаляет эту клетку.
        figure: поверхность с фигурой, которой походили
        """
        self.__update_counters(self.__clicked_cells[0].get_counters)
        self.__clicked_cells[0].update(figure)
        self.__clicked_cells[0].paint(self)
        self.__cells.remove(self.__clicked_cells[0])

    def move_by_index(self, index_to_move: int, figure: Surface) -> None:
        """Обновляет счётчики клетки по индексу, передаёт ей поверхность фигуры, которой походили, рисует на сетке
            обновлённую версию клетки, удаляет эту клетку.
        index_to_move: индекс клетки, в которую сделан ход
        figure: поверхность с фигурой, которой походили
        """
        self.__update_counters(self.__cells[index_to_move].get_counters)
        self.__cells[index_to_move].update(figure)
        self.__cells[index_to_move].paint(self)
        del self.__cells[index_to_move]

    def __update_counters(self, cell_counters: List[Counter]) -> None:
        """Добавляет пустые счётчики к счётчикам текущей фигуры и обновляет счётчики клетки, которые относятся к текущей
            фигуре.
        cell_counters: счётчики рядов победы, в которые входит клетка, в которую походили
        """
        self.__cur_figure_counters.extend([c for c in cell_counters if not c.has_figure()])
        for c in cell_counters:
            if c in self.__cur_figure_counters:
                c.add()

    def has_win(self) -> bool:  # ////nn
        """"""
        finish = False
        for counter in self.__cur_figure_counters:
            if counter.is_filled():
                finish = True
                break
        self.__cur_figure_counters, self.__next_figure_counters =\
            self.__next_figure_counters, self.__cur_figure_counters
        return finish

    def has_draw(self) -> bool:  # ////nn
        """"""
        return len(self.__cells) == 0
