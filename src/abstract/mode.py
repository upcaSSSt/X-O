from pygame.image import load

from src.const import path
from src.const import text
from src.abstract.player import Player
from src.abstract.window import Window
from src.static import calibri
from src.static import menu_initializer
from src.human import Human
from src.label import Label
from src.window_switcher import WindowSwitcher
from src.intermediate_window import IntermediateWindow
from src.field import Field
from src.background_randomizer import BackgroundRandomizer


class Mode(Window):
    """"""

    def __init__(self, circle_player: Player):
        """"""
        super(Mode, self).__init__()

        self._cross_player = Human(text.FIRST_PLAYER_NAME, path.CROSS)
        self._circle_player = circle_player

        self._main_field = Field()

        self.blit(load(BackgroundRandomizer().random_path()).convert_alpha(), (0, 0))
        self.blit(self._main_field, (0, 0))

    def handle_click(self, click_pos: tuple[int, int]) -> None:
        raise NotImplementedError

    def _move_player(self, cur_player: Player) -> None:
        """"""
        cur_player.move(self._main_field)
        self.blit(self._main_field, (0, 0))
        self.__set_winner(cur_player)

    def __set_winner(self, cur_player: Player) -> None:
        """"""
        if self._main_field.has_win():
            self._next_window = cur_player.get_win_window
        elif self._main_field.has_draw():
            self._next_window = IntermediateWindow([Label(load(path.HUGGING).convert_alpha()),
                                                    Label(calibri.render(text.DRAW))],
                                                   [WindowSwitcher(calibri.render(text.PLAY_AGAIN),
                                                                   menu_initializer.get_menu())])
