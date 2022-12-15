from abc import ABC, abstractmethod

from src.figure import Figure


class Player(ABC):
    """"""

    def __init__(self, name: str, figure: Figure):
        """"""
        self._name = name
        self._figure = figure

    def victory(self):  # ////
        print(f"Победил {self._name}")
