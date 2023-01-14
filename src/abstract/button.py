from typing import Tuple

from pygame import Surface

from src.abstract.window_item import WindowItem


class Button(WindowItem):
    """"""

    def __init__(self, image: Surface):
        """"""
        super(Button, self).__init__(image)

    def is_clicked(self, click_pos: Tuple[int, int]) -> bool:
        """"""
        return self.rect.collidepoint(click_pos)
