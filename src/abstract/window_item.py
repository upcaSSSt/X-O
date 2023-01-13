from abc import ABC

from pygame import Surface
from pygame.sprite import Sprite


class WindowItem(ABC, Sprite):
    """"""
    
    def __init__(self, image: Surface):
        """"""
        super(WindowItem, self).__init__()
        self.image = image
        self.rect = self.image.get_rect()

    def paint(self, painting_surf: Surface) -> None:
        """Рисует клетку на переданной поверхности сетки.
        painting_grid: поверхность сетки, на которой надо нарисовать поверхность клетки
        """
        painting_surf.blit(self.image, self.rect)
