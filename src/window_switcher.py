from pygame import Surface

from src.abstract.window import Window
from src.abstract.button import Button


class WindowSwitcher(Button):
    """"""

    def __init__(self, image: Surface, window_to_switch: Window):
        """"""
        super(WindowSwitcher, self).__init__(image)
        self.__window_to_switch = window_to_switch

    @property
    def get_mode_to_switch(self) -> Window:
        return self.__window_to_switch
