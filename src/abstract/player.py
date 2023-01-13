from abc import ABC, abstractmethod

from pygame import Surface
from pygame.image import load

from src.const import text
from src.static import calibri
from src.static import menu_initializer
from src.label import Label
from src.window_switcher import WindowSwitcher
from src.intermediate_window import IntermediateWindow
from src.field import Field


class Player(ABC):
    """"""

    def __init__(self, name: str, figure_path: str):
        """"""
        self.__name = name
        self._figure = load(figure_path).convert_alpha()

    @property
    def get_figure(self) -> Surface:
        return self._figure

    @property
    def get_win_window(self) -> IntermediateWindow:
        return IntermediateWindow([Label(self._figure), Label(calibri.render(self.__name))],
                                  [WindowSwitcher(calibri.render(text.PLAY_AGAIN), menu_initializer.get_menu())])

    @abstractmethod
    def move(self, field: Field) -> None:
        raise NotImplementedError
