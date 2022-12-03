import pygame as pg


class Figure:
    """Класс для хранения поверхности, на которой нарисована фигура."""

    def __init__(self, sprite_path: str):
        """Создаёт поверхность, на которую рисуется фигура.
        sprite_path: путь к спрайту с фигурой
        """
        self.__surface = pg.image.load(sprite_path)

    @property
    def get_surface(self):
        return self.__surface
