from pygame import Surface

from src.player import Player


class Human(Player):
    """"""
    
    def __init__(self, name: str, figure: Surface):
        """"""
        super(Human, self).__init__(name, figure)
    