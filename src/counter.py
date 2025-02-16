from src.const import settings


class Counter:
    """Класс для подсчёта кол-ва одинаковых фигур в рядах, заполнив которые можно победить."""

    def __init__(self):
        """Создаёт счётчик одинаковых фигур в рядах победы."""
        self.__count = 0

    def add(self) -> None:
        """Обновляет счётчик."""
        self.__count += 1

    def has_not_figure(self) -> bool:
        """Проверяет наличие фигур в ряду победы.???"""
        return self.__count == 0

    def is_filled(self) -> bool:
        """Проверяет заполненность ряда победы."""
        return self.__count >= settings.N_CELLS_IN_ROW
