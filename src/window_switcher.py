from pygame import Surface
from pygame import Rect
from pygame.draw import rect

from src.const import color
from src.abstract.window import Window
from src.abstract.button import Button


class WindowSwitcher(Button):
    """Кнопка для переключения окна приложения при клике."""

    def __init__(self, content: Surface, window_to_switch: Window):
        """content: часть переключателя, на которой расположен текст либо картинка.
        window_to_switch: окно, которое появится при клике по переключателю.
        """
        super(WindowSwitcher, self).__init__((content.get_width() + 25, content.get_height() + 5))
        self.__content = content
        self.__window_to_switch = window_to_switch
        self._image.set_colorkey(0)
        self._reset_hover()

    @property
    def get_window_to_switch(self) -> Window:
        return self.__window_to_switch

    def __paint_rect(self, bg_color: tuple[int, ...]) -> None:
        """"""
        rect(self._image, bg_color, Rect(0, 0, self._image.get_width(), self._image.get_height()), border_radius=10)
        self._image.blit(self.__content, self.__content.get_rect(center=self._image.get_rect().center))

    def _hover(self) -> None:
        """"""
        self.__paint_rect(color.LIGHT_BLUE)

    def _reset_hover(self) -> None:
        """"""
        self.__paint_rect(color.BLUE)
