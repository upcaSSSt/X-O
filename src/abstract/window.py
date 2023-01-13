from abc import ABC, abstractmethod

from pygame import Surface

from src.const import settings


class Window(ABC, Surface):
    """"""

    def __init__(self):
        """"""
        super(Window, self).__init__((settings.SCREEN_SIZE, settings.SCREEN_SIZE))
        self._next_window = self

    @abstractmethod
    def handle_click(self, click_pos: tuple[int, int]) -> None:
        raise NotImplementedError

    def switch_window(self):  # ////
        """"""
        return self._next_window
