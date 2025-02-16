from random import randrange

from src.const import text
from src.abstract.player import Player
from src.field import Field


class AI(Player):
    """Игрок-компьютер."""

    def __init__(self, figure_path: str):
        """figure_path: путь к изображению фигуры, которой будет играть игрок."""
        super(AI, self).__init__(text.AI_NAME, figure_path)

    def move(self, field: Field) -> None:
        """Выбирает случайную клетку из свободных, передаёт её индекс и свою фигуру в игровое поле.
        field: игровое поле.
        """
        field.move_by_index(randrange(field.get_n_cells), self._figure)
