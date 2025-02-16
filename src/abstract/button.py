from abc import abstractmethod

from pygame import Surface

from src.abstract.window_item import WindowItem


class Button(WindowItem):
    """Ячейка окна, выполняющая какие-либо действия при клике."""

    @abstractmethod
    def _hover(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def _reset_hover(self) -> None:
        raise NotImplementedError

    def paint_hover(self, painting_surf: Surface) -> None:
        """"""
        self._hover()
        self.paint(painting_surf)
        self._reset_hover()

    def is_mouse_detected(self, mouse_pos: tuple[int, int]) -> bool:
        """Возвращает True, если обнаруживает мышь на кнопке, иначе False.
        mouse_pos: координаты курсора мыши.
        """
        return self._rect.collidepoint(mouse_pos)
