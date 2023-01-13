from random import randrange

from src.const import text
from src.abstract.player import Player
from src.field import Field


class AI(Player):
    """Класс для создания игрока-компьютера и реализации его поведения."""

    def __init__(self, figure_path: str):
        """"""
        super(AI, self).__init__(text.AI_NAME, figure_path)

    def move(self, field: Field) -> None:
        """"""
        field.move_by_index(randrange(field.get_n_cells), self._figure)
