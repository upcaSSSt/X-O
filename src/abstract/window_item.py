from src.abstract.widget import Widget


class WindowItem(Widget):
    """Всё что может находиться на окне."""

    @property
    def get_height(self) -> int:
        return self._rect.height

    def set_midtop(self, pos: tuple[int, int]) -> None:
        self._rect.midtop = pos
