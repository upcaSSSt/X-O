from sys import exit

import pygame as pg

from src.const import settings
from src.const import path
from src.abstract.window import Window
from src.static.menu_initializer import get_menu


class XO:
    """Управляет ресурсами и поведением игры."""

    def __init__(self):
        pg.init()
        self.__screen = pg.display.set_mode((settings.SCREEN_SIZE, settings.SCREEN_SIZE))

        Window.static_init()

        pg.display.set_caption(settings.CAPTION)
        pg.display.set_icon(pg.image.load(path.ICON).convert_alpha())

        self.__clock = pg.time.Clock()
        self.__cur_window = get_menu()

    def run(self) -> None:
        """Запускает основной цикл игры."""
        while True:
            self.__event_handler()
            self.__update_screen()

    def __event_handler(self) -> None:
        """Обрабатывает события мыши???."""
        for e in pg.event.get():
            if e.type == pg.MOUSEMOTION:
                self.__cur_window.handle_hover(pg.mouse.get_pos())
            elif e.type == pg.MOUSEBUTTONDOWN:
                self.__cur_window.handle_click(pg.mouse.get_pos())
                self.__cur_window = self.__cur_window.switch_window()
            elif e.type == pg.KEYDOWN:
                if e.key == pg.K_ESCAPE:
                    self.__cur_window = get_menu()
            elif e.type == pg.QUIT:
                exit()

    def __update_screen(self) -> None:
        """Обновляет изображения на экране и отображает новый экран."""
        self.__cur_window.paint(self.__screen)
        pg.display.flip()  # ////
        self.__clock.tick(settings.FPS)
