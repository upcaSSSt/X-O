from typing import Tuple
from typing import List
from statistics import mean

from src.const import settings
from src.const import color
from src.abstract.window import Window
from src.label import Label
from src.window_switcher import WindowSwitcher


class IntermediateWindow(Window):
    """"""

    def __init__(self, labels: List[Label], switchers: List[WindowSwitcher],
                 padding_top: int = settings.SCREEN_SIZE // 8):
        """"""
        super(IntermediateWindow, self).__init__()
        self.__rect = self.get_rect()

        self.__labels = labels
        self.__switchers = switchers
        self.__padding_top = padding_top

        self.fill(color.WHITE)
        self.__paint_items()

    def __paint_items(self) -> None:
        """"""
        items = self.__labels + self.__switchers
        # А почему? У них общий родитель window_item и тут только его функционал.
        row_gap = mean([i.rect.height for i in items])

        if len(items) > 0:
            items[0].rect.midtop = (self.__rect.centerx, self.__padding_top)
            items[0].paint(self)

        for i in range(1, len(items)):
            items[i].rect.midtop = (self.__rect.centerx, items[i - 1].rect.bottom + row_gap)
            items[i].paint(self)

    def handle_click(self, click_pos: Tuple[int, int]) -> None:
        """"""
        for button in self.__switchers:
            if button.is_clicked(click_pos):
                self._next_window = button.get_mode_to_switch
