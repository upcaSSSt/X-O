from os import listdir
from random import choice

from src.const import path


class BackgroundRandomizer:
    """Класс для выбора случайного фона."""

    def __init__(self):
        """Сохраняет список имён фоновых изображений."""
        self.__bg_paths = listdir(path.BACKGROUNDS)

    def random_path(self) -> str:
        """Возвращает путь к случайно выбранному фоновому изображению."""
        return f"{path.BACKGROUNDS}{choice(self.__bg_paths)}"
