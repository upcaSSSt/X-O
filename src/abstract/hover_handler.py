from pygame import SYSTEM_CURSOR_ARROW
from pygame import SYSTEM_CURSOR_HAND
from pygame.mouse import set_cursor

from src.abstract.widget import Widget


class HoverHandler(Widget):
    """"""

    def __init__(self, size_or_image, buttons: list = []):
        """"""
        super(HoverHandler, self).__init__(size_or_image)
        self._buttons = buttons  # Чудеса динамической типизации.
        self.__no_hover = True
        self.__hovered_button = self._buttons[0] if self._buttons else None

    def set_buttons(self, buttons: list) -> None:
        self._buttons = buttons
        self.__hovered_button = self._buttons[0]

    def handle_hover(self, mouse_pos: tuple[int, int]) -> None:
        """"""
        if not self.__hovered_button.is_mouse_detected(mouse_pos) and not self.__no_hover:
            set_cursor(SYSTEM_CURSOR_ARROW)
            self.__hovered_button.paint(self._image)
            self.__no_hover = True

        if self.__no_hover:
            for button in self._buttons:
                if button.is_mouse_detected(mouse_pos):
                    set_cursor(SYSTEM_CURSOR_HAND)
                    self.__hovered_button = button
                    button.paint_hover(self._image)
                    self.__no_hover = False
                    break
