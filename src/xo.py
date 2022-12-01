import pygame as pg

from src.window import Window


class XO:
    """"""

    def __init__(self):
        """"""
        pg.init()

        self.__main_window = Window()

    def run(self):
        """"""
        while True:
            self.__event_handler()
            self.__main_window.update()

    def __event_handler(self):
        """"""
        for e in pg.event.get():
            if e.type == pg.QUIT:
                Window.close()
