from sys import exit

import pygame as pg

from src.static.pygame_initializer import screen
from src.static.menu_initializer import get_menu


class XO:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру, создаёт игровые объекты и задаёт фоновое изображение."""
        self.__cur_window = get_menu()

    def run(self) -> None:
        """Запуск основного цикла игры."""
        while True:
            self.__event_handler()
            self.__update_screen()

    def __event_handler(self) -> None:
        """Обрабатывает события мыши."""
        for e in pg.event.get():
            if e.type == pg.MOUSEBUTTONDOWN:
                self.__cur_window.handle_click(pg.mouse.get_pos())
                self.__cur_window = self.__cur_window.switch_window()
            elif e.type == pg.QUIT:
                exit()

    def __update_screen(self) -> None:
        """Обновляет изображения на экране и отображает новый экран."""
        screen.blit(self.__cur_window, (0, 0))
        pg.display.flip()
