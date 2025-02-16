from pygame import Surface
from pygame.image import load

from src.const import settings
from src.const import path
from src.abstract.hover_handler import HoverHandler
from src.cell import Cell
from src.counter import Counter


class Field(HoverHandler):
    """Игровое поле и управление его клетками."""

    def __init__(self):
        Cell.paint_bg()
        super(Field, self).__init__((settings.SCREEN_SIZE, settings.SCREEN_SIZE))
        self.set_buttons(self.__init_cells())

        self.__cur_figure_counters = []
        self.__next_figure_counters = []
        self.__clicked_cells = []

        self._image.blit(load(path.GRID).convert_alpha(), (0, 0))

        for cell in self._buttons:
            cell.paint(self._image)

    def __init_cells(self):
        counters = {"left_vertical": Counter(), "middle_vertical": Counter(), "right_vertical": Counter(),
                    "top_horizontal": Counter(), "middle_horizontal": Counter(), "bottom_horizontal": Counter(),
                    "principal_diagonal": Counter(), "secondary_diagonal": Counter()}
        return [
            Cell((0, 0), [counters["left_vertical"], counters["top_horizontal"], counters["principal_diagonal"]]),
            Cell((self._rect.centerx - settings.CELL_SIZE // 2, 0),
                 [counters["middle_vertical"], counters["top_horizontal"]]),
            Cell((self._rect.topright[0] - settings.CELL_SIZE, 0),
                 [counters["right_vertical"], counters["top_horizontal"], counters["secondary_diagonal"]]),
            Cell((0, self._rect.centery - settings.CELL_SIZE // 2),
                 [counters["left_vertical"], counters["middle_horizontal"]]),
            Cell((self._rect.centerx - settings.CELL_SIZE // 2, self._rect.centery - settings.CELL_SIZE // 2),
                 [counters["middle_vertical"], counters["middle_horizontal"], counters["principal_diagonal"],
                  counters["secondary_diagonal"]]),
            Cell((self._rect.midright[0] - settings.CELL_SIZE, self._rect.centery - settings.CELL_SIZE // 2),
                 [counters["right_vertical"], counters["middle_horizontal"]]),
            Cell((0, self._rect.bottomleft[1] - settings.CELL_SIZE),
                 [counters["left_vertical"], counters["bottom_horizontal"], counters["secondary_diagonal"]]),
            Cell((self._rect.centerx - settings.CELL_SIZE // 2, self._rect.midbottom[1] - settings.CELL_SIZE),
                 [counters["middle_vertical"], counters["bottom_horizontal"]]),
            Cell((self._rect.bottomright[0] - settings.CELL_SIZE, self._rect.bottomright[1] - settings.CELL_SIZE),
                 [counters["right_vertical"], counters["bottom_horizontal"], counters["principal_diagonal"]])
        ]

    @property
    def get_n_cells(self) -> int:
        return len(self._buttons)

    def has_clicked_cell(self, click_pos: tuple[int, int]) -> bool:
        """Сохраняет клетку(и), по которой кликнул пользователь. Возвращает True, если есть хоть одна кликнутая клетка,
            иначе False.
        click_pos: координаты клика.
        """
        self.__clicked_cells = [c for c in self._buttons if c.is_mouse_detected(click_pos)]  # ////
        return len(self.__clicked_cells) > 0

    def move_by_click(self, figure: Surface) -> None:
        """Передаёт кликнутой клетке поверхность фигуры, которой походили, рисует на сетке обновлённую версию клетки,
            обновляет счётчики, удаляет эту клетку./////
        figure: поверхность с фигурой, которой походили.
        """
        self.__clicked_cells[0].update(figure)
        self.__clicked_cells[0].paint(self._image)
        self.__update_counters(self.__clicked_cells[0].get_counters)
        self._buttons.remove(self.__clicked_cells[0])

    def move_by_index(self, index_to_move: int, figure: Surface) -> None:
        """Передаёт клетке по индексу поверхность фигуры, которой походили, рисует на сетке обновлённую версию клетки,
            обновляет счётчики, удаляет эту клетку.
        index_to_move: индекс клетки, в которую сделан ход.
        figure: поверхность с фигурой, которой походили.
        """
        self._buttons[index_to_move].update(figure)
        self._buttons[index_to_move].paint(self._image)
        self.__update_counters(self._buttons[index_to_move].get_counters)
        del self._buttons[index_to_move]

    def __update_counters(self, cell_counters: list[Counter]) -> None:
        """Добавляет пустые счётчики, к которым относится текущая клетка, к счётчикам текущей фигуры и обновляет
            счётчики текущей фигуры, к которым относится текущая клетка.
        cell_counters: счётчики рядов победы, в которые входит клетка, в которую походили.
        """
        self.__cur_figure_counters.extend([c for c in cell_counters if c.has_not_figure()])
        for counter in cell_counters:
            if counter in self.__cur_figure_counters:
                counter.add()

    def has_filled_row(self) -> bool:  # ////nn
        """Возвращает True, если на поле есть заполненный ряд с текущей фигурой, иначе переключает счётчики для
        следующей фигуры и возвращает False."""
        for counter in self.__cur_figure_counters:
            if counter.is_filled():
                self._buttons.clear()
                return True
        self.__cur_figure_counters, self.__next_figure_counters =\
            self.__next_figure_counters, self.__cur_figure_counters
        return False

    def has_draw(self) -> bool:  # ////nn
        """Возвращает True, если игрокам больше некуда ходить, иначе False."""
        return len(self._buttons) == 0
