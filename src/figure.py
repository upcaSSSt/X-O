import pygame as pg


class Figure:
    """Класс для создания фигуры."""

    def __init__(self, image_path: str):
        """Создаёт поверхность, на которую рисуется фигура.
        sprite_path: путь к изображению фигуры
        """
        self.__surface = pg.image.load(image_path).convert_alpha()

    @property
    def get_surface(self) -> pg.Surface:
        return self.__surface
