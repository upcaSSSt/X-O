from __future__ import annotations
from abc import abstractmethod

from pygame import SYSTEM_CURSOR_ARROW
from pygame.mouse import set_cursor
from pygame.mixer import Sound

from src.const import settings
from src.const import path
from src.abstract.hover_handler import HoverHandler


class Window(HoverHandler):
    """Окно с возможностью обработки клика по кнопке и переключения на другое окно."""

    @classmethod
    def static_init(cls) -> None:
        cls.__click = Sound(path.CLICK)

    def __init__(self, buttons: list = []):
        super(Window, self).__init__((settings.SCREEN_SIZE, settings.SCREEN_SIZE), buttons)
        self._next_window = self

    @staticmethod
    def _react_click() -> None:
        """"""
        Window.__click.play()
        set_cursor(SYSTEM_CURSOR_ARROW)

    @abstractmethod
    def handle_click(self, click_pos: tuple[int, int]) -> None:
        raise NotImplementedError

    def switch_window(self) -> Window:
        """Возвращает текущее окно приложения, которое могло быть заменено на окно из кликнутого переключателя."""
        return self._next_window
