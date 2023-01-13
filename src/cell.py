from pygame import Surface

from src.const import settings
from src.abstract.button import Button
from src.counter import Counter


class Cell(Button):
    """Класс для создания спрайта клетки и реализации его поведения."""

    def __init__(self, pos: tuple[int, int], counters: list[Counter]):
        """Создаёт поверхность спрайта, на которой будет нарисована фигура, сохраняет прямоугольник поверхности, ставит
            координаты клетки на поверхности сетки, делает поверхность прозрачной.
        pos: координаты, по которым будет располагаться клетка на поверхности сетки
        """
        super(Cell, self).__init__(Surface((settings.CELL_SIZE, settings.CELL_SIZE)))
        self.rect = self.image.get_rect(topleft=pos)
        self.__counters = counters

    @property
    def get_counters(self) -> list[Counter]:
        return self.__counters

    def update(self, *args: Surface) -> None:  # Надеюсь я правильно понял задумку update.
        """Рисует на поверхности клетки изображение фигуры, расположенное по переданному пути.
        figure_path: путь к изображению фигуры, которой походили"""
        self.image = args[0]
