from random import randrange


class AI:
    """Класс для создания искусственного игрока и реализации логики его ходов."""

    def move(self, n_free_cells: int) -> int:
        """Возвращает случайный индекс клетки, в которую сделан ход.
        n_free_cells: кол-во свободных клеток, в которые можно ходить
        """
        return randrange(n_free_cells)
