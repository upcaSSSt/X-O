from typing import Tuple
from typing import List

from pygame import Surface

from src.const import settings
from src.abstract.button import Button
from src.counter import Counter


class Cell(Button):
    """Класс для создания клетки и реализации её поведения."""

    def __init__(self, pos: Tuple[int, int], counters: List[Counter]):
        """(Устарело) Создаёт поверхность спрайта, на которой будет нарисована фигура, сохраняет прямоугольник
            поверхности, ставит координаты клетки на поверхности сетки, делает поверхность прозрачной.
        pos: координаты, по которым будет располагаться клетка на поверхности сетки
        """
        super(Cell, self).__init__(Surface((settings.CELL_SIZE, settings.CELL_SIZE)))
        self.rect = self.image.get_rect(topleft=pos)
        self.__counters = counters

    @property
    def get_counters(self) -> List[Counter]:
        return self.__counters

    def update(self, *args: Surface) -> None:  # Надеюсь я правильно понял задумку update.
        """Присваивает поверхности клетки поверхность фигуры, которой походили.
        args[0]: поверхность с фигурой, которой походили
        """
        self.image = args[0]
