from pygame import image
from pygame import sprite
from pygame import Surface

from src.const import settings


class Cell(sprite.Sprite):
    """Класс для создания спрайта клетки и реализации его поведения."""

    def __init__(self, pos: tuple):
        """Создаёт поверхность спрайта, на которой будет нарисована фигура, сохраняет прямоугольник поверхности, ставит
            координаты клетки на поверхности сетки, делает поверхность прозрачной.
        pos: координаты, по которым будет располагаться клетка на поверхности сетки
        """
        super().__init__()

        self.image = Surface((settings.CELL_SIZE, settings.CELL_SIZE))
        self.rect = self.image.get_rect()

        self.rect.topleft = pos
        self.image.set_alpha(0)

    def paint(self, painting_grid: Surface):
        """Рисует клетку на переданной поверхности сетки.
        painting_grid: поверхность сетки, на которой надо нарисовать поверхность клетки
        """
        painting_grid.blit(self.image, self.rect)

    def move_handler(self, figure_path: str):
        """Рисует на поверхности клетки изображение фигуры, расположенное по переданному пути.
        figure_path: путь к изображению фигуры, которой походили
        """
        self.image = image.load(figure_path).convert_alpha()
