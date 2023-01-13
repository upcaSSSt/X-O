from src.abstract.player import Player
from src.field import Field


class Human(Player):
    """"""
    
    def __init__(self, name: str, figure_path: str):
        """"""
        super(Human, self).__init__(name, figure_path)

    def move(self, field: Field) -> None:
        """"""
        field.move_by_click(self._figure)
