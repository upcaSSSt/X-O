from abc import ABC, abstractmethod

from pygame import Surface
from pygame.image import load

from src.const import text
# from src.abstract.mode import Mode //////
from src.static import font
from src.static import menu_initializer
from src.label import Label
from src.window_switcher import WindowSwitcher
from src.intermediate_window import IntermediateWindow
from src.field import Field


class Player(ABC):
    """"""

    def __init__(self, name: str, figure_path: str):
        """name: имя игрока.
        figure_path: путь к изображению фигуры, которой будет играть игрок.
        """
        self.__name = name
        self._figure = load(figure_path).convert_alpha()

    @property
    def get_figure(self) -> Surface:
        return self._figure

    @abstractmethod
    def move(self, field: Field) -> None:
        raise NotImplementedError

    def win_window(self, result_window) -> IntermediateWindow:
        return IntermediateWindow([Label(self._figure), Label(font.render(self.__name))],
                                  [WindowSwitcher(font.render(text.VIEW_RESULT), result_window),
                                   WindowSwitcher(font.render(text.PLAY_AGAIN), menu_initializer.get_menu())])
