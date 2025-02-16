from src.const import path
from src.abstract.mode import Mode
from src.ai import AI


class AIMode(Mode):
    """Игровое окно, вызывающее ходы человека и ИИ."""

    def __init__(self):
        super(AIMode, self).__init__(AI(path.CIRCLE))

    def handle_click(self, click_pos: tuple[int, int]) -> None:
        """Ходит человеком и ИИ, если пользователь попал кликом по свободной клетке.
        click_pos: координаты клика.
        """
        if self._main_field.has_clicked_cell(click_pos):
            AIMode._react_click()
            self._move_player(self._cross_player)
            if self._next_window == self:  # ////
                self._move_player(self._circle_player)
