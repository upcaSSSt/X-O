from pygame import Surface

from src.const import settings
from src.const import color
from src.abstract.button import Button
from src.static.bg_randomizer import random_bg
from src.counter import Counter


class Cell(Button):
    """Клетка на сетке."""

    @classmethod
    def paint_bg(cls) -> None:
        bg = random_bg()
        bg_rect = bg.get_rect()
        central_part = (bg_rect.centerx - settings.HALF_SCREEN, bg_rect.centery - settings.HALF_SCREEN,
                        settings.SCREEN_SIZE, settings.SCREEN_SIZE)
        cls.__general_bg = bg.subsurface(central_part)

    def __init__(self, top_left: tuple[int, int], counters: list[Counter]):
        """pos: координаты, по которым будет располагаться клетка на поверхности сетки.
        counters: счётчики рядов победы, в которые входит данная клетка.
        """
        super(Cell, self).__init__((settings.CELL_SIZE, settings.CELL_SIZE), top_left, True)
        self.__counters = counters
        self.__local_bg = Cell.__general_bg.subsurface(self._rect)
        self.update(self.__local_bg)

    @property
    def get_counters(self) -> list[Counter]:
        return self.__counters

    def _hover(self) -> None:
        """"""
        self._image.fill(color.GRANDMA_APPLES)

    def _reset_hover(self) -> None:
        """"""
        self.update(self.__local_bg)

    def update(self, *args: Surface) -> None:
        """Присваивает поверхности клетки поверхность фигуры, которой походили.
        args[0]: поверхность с фигурой, которой походили.
        """
        self._image.blit(args[0], (0, 0))
