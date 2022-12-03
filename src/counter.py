from src.const import settings


class Counter:
    """Класс для подсчёта кол-ва одинаковых фигур в рядах, заполнив
    которые можно победить."""

    def __init__(self):
        """Создаёт счётчик одинаковых фигур в рядах победы."""
        self.__count = 0

    def add(self):
        """Прибавляет к счётчику новую фигуру в ряду победы."""
        self.__count += 1

    def is_filled(self):
        """Проверяет заполненность ряда победы."""
        return self.__count >= settings.N_TO_FILL_ROW
