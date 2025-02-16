from pygame.image import load

from src.const import path
from src.const import text
from src.abstract.player import Player
from src.abstract.window import Window
from src.static import font
from src.static import menu_initializer
from src.human import Human
from src.label import Label
from src.window_switcher import WindowSwitcher
from src.intermediate_window import IntermediateWindow
from src.field import Field


class Mode(Window):
    """Окно для взаимодействия игроков с игровым полем в зависимости от режима и для работы с игровым полем."""

    def __init__(self, circle_player: Player):
        """"""
        super(Mode, self).__init__()

        self._cross_player = Human(text.FIRST_PLAYER_NAME, path.CROSS)
        self._circle_player = circle_player
        self._main_field = Field()

        self._main_field.paint(self._image)

    def handle_hover(self, mouse_pos: tuple[int, int]) -> None:
        """"""
        self._main_field.handle_hover(mouse_pos)
        self._main_field.paint(self._image)

    def _move_player(self, cur_player: Player) -> None:
        """Выполняет все операции, необходимые для хода: вызывает ход игрока в поле, обновляет поле, проверяет поле на
            окончание игры.
        cur_player: игрок, который походил в данный момент.
        """
        cur_player.move(self._main_field)
        self._main_field.paint(self._image)
        self.__set_win_window(cur_player)

    def __set_win_window(self, cur_player: Player) -> None:
        """Присваивает текущему окну приложения окно победы текущего игрока, если на поле заполнен ряд или окно ничьи,
            если на поле ничья.
        cur_player: игрок, который походил в данный момент.
        """
        if self._main_field.has_filled_row():
            self._next_window = cur_player.win_window(self)
        elif self._main_field.has_draw():
            self._next_window = IntermediateWindow([Label(load(path.HUGGING).convert_alpha()),
                                                    Label(font.render(text.DRAW))],
                                                   [WindowSwitcher(font.render(text.VIEW_RESULT), self),
                                                    WindowSwitcher(font.render(text.PLAY_AGAIN),
                                                                   menu_initializer.get_menu())])
