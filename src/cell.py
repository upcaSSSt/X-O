from pygame import sprite
from pygame import image
from pygame import Surface

from src.const import settings


class Cell(sprite.Sprite):
    """Класс для создания клетки и получения фигуры для неё."""

    def __init__(self, pos: tuple):
        """Сохраняет координаты клетки на поверхности сетки, создаёт поверхность, на которой будет нарисована фигура и
            красит её.
        pos: координаты, по которым будет располагаться клетка на поверхности сетки
        """
        super().__init__()

        self.image = Surface((settings.CELL_SIZE, settings.CELL_SIZE))
        self.rect = self.image.get_rect()

        self.image.set_alpha(0)
        self.rect.topleft = pos

    def paint(self, painting_grid: Surface):
        """Рисует клетку на переданной поверхности сетки.
        painting_grid: поверхность сетки, на которой надо нарисовать поверхность клетки
        """
        painting_grid.blit(self.image, self.rect)

    def move_handler(self, figure_path: str):
        """Рисует на поверхности клетки изображение фигуры, расположенное по переданному пути.
        figure_path: путь к изображению фигуры, которой походили в данный момент
        """
        self.image = image.load(figure_path).convert_alpha()
