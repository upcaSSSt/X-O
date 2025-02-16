from src.abstract.player import Player
from src.field import Field


class Human(Player):
    """Игрок - человек."""

    def move(self, field: Field) -> None:
        """Передаёт свою фигуру в игровое поле.
        field: игровое поле.
        """
        field.move_by_click(self._figure)
