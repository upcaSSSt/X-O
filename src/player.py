from abc import ABC

from pygame import Surface


class Player(ABC):
    """"""

    def __init__(self, name: str, figure: Surface):
        """"""
        self._name = name
        self._figure = figure

    def victory(self):  # ////nn
        print(f"Победил {self._name}")
