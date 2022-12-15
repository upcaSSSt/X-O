from random import randrange

from src.player import Player
from src.figure import Figure


class AI(Player):
    """Класс для создания искусственного игрока и реализации логики его ходов."""

    def __init__(self, figure: Figure):
        """"""
        super(AI, self).__init__("Sanakan", figure)

    def move(self, n_free_cells: int) -> int:
        """Возвращает случайный индекс клетки, в которую сделан ход.
        n_free_cells: кол-во свободных клеток, в которые можно ходить
        """
        return randrange(n_free_cells)
