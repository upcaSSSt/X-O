from abc import ABC

from pygame import SRCALPHA
from pygame import Surface


class Widget(ABC):
    """"""

    def __init__(self, size_or_image, top_left: tuple[int, int] = (0, 0), is_alpha: bool = False):
        """"""
        if isinstance(size_or_image, tuple):
            if is_alpha:
                self._image = Surface(size_or_image, SRCALPHA)
            else:
                self._image = Surface(size_or_image)
        elif isinstance(size_or_image, Surface):
            self._image = size_or_image

        self._rect = self._image.get_rect(topleft=top_left)

    def paint(self, painting_surf: Surface) -> None:
        """Рисует поверхность спрайта на переданной поверхности.
        painting_surf: поверхность, на которой надо нарисовать спрайт.
        """
        painting_surf.blit(self._image, self._rect)
