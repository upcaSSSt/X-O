from typing import Tuple

from src.const import path
from src.const import text
from src.abstract.mode import Mode
from src.human import Human


class HumanMode(Mode):
    """"""

    def __init__(self):
        """"""
        super(HumanMode, self).__init__(Human(text.SECOND_PLAYER_NAME, path.CIRCLE))
        self.__cur_player = self._cross_player
        self.__next_player = self._circle_player

    def handle_click(self, click_pos: Tuple[int, int]) -> None:
        """"""
        if self._main_field.has_clicked_cell(click_pos):
            self._move_player(self.__cur_player)
            self.__cur_player, self.__next_player = self.__next_player, self.__cur_player
