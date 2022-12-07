import pygame as pg

from src.const import settings
from src.const import colors


class Cell(pg.sprite.Sprite):
    """Класс для создания клетки и получения фигуры для неё."""

    def __init__(self, pos: tuple):
        """Сохраняет координаты клетки на поверхности сетки, создаёт
            поверхность, на которой будет нарисована фигура и красит её.
        pos: координаты, по которым будет располагаться клетка на
            поверхности сетки
        """
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface((settings.CELL_SIZE, settings.CELL_SIZE))
        self.rect = self.image.get_rect()

        self.image.fill(colors.BLACK)
        self.rect.topleft = pos

    def paint(self, painting_grid: pg.Surface):
        """Рисует клетку на переданной поверхности сетки.
        painting_grid: поверхность сетки, на которой надо нарисовать
            поверхность клетки
        """
        painting_grid.blit(self.image, self.rect)

    def move_handler(self, figure_path: str):
        """Рисует на поверхности клетки изображение фигуры,
            расположенное по переданному пути.
        figure_path: путь к изображению фигуры, которой походили в
            данный момент
        """
        self.image = pg.image.load(figure_path)
