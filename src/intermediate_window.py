from src.const import settings
from src.const import color
from src.abstract.window import Window
from src.label import Label
from src.window_switcher import WindowSwitcher


class IntermediateWindow(Window):
    """Неигровое окно."""

    def __init__(self, labels: list[Label], switchers: list[WindowSwitcher], pad_top: int = settings.SCREEN_SIZE // 8,
                 gap: int = 40):
        """labels: лейблы окна.
        switchers: кнопки переключения окна.
        padding_top: координата по y, на которой расположится вершина каждой ячейки, изначально равен координате для
            первой ячейки.
        """
        super(IntermediateWindow, self).__init__(switchers)

        self.__labels = labels
        self.__pad_top = pad_top
        self.__gap = gap

        self._image.fill(color.WHITE)
        self.__paint_items()

    def __paint_items(self) -> None:
        """Рисует на на окне лейблы и кнопки - переключатели окон. Первая ячейка рисуется после верхнего отступа,
        расстояние между остальными равно среднему арифметическому высоты всех ячеек."""
        items = self.__labels + self._buttons

        for item in items:
            item.set_midtop((self._rect.centerx, self.__pad_top))
            item.paint(self._image)
            self.__pad_top += item.get_height + self.__gap

    def handle_click(self, click_pos: tuple[int, int]) -> None:
        """Присваивает текущему окну приложения окно, которое было сохранено в переключателе, по которому кликнули.
        click_pos: координаты клика.
        """
        for switcher in self._buttons:
            if switcher.is_mouse_detected(click_pos):
                IntermediateWindow._react_click()
                self._next_window = switcher.get_window_to_switch
