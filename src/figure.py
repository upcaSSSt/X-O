import pygame as pg


class Figure:
    """"""

    def __init__(self, sprite_path: str):
        """"""
        self.__figure = pg.image.load(sprite_path)

    @property
    def get_figure(self):
        return self.__figure
