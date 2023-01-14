from pygame import init
from pygame import display
from pygame.image import load

from src.const import settings
from src.const import path

"""Модуль для инициализации PyGame и создания окна приложения."""

screen = display.set_mode((settings.SCREEN_SIZE, settings.SCREEN_SIZE))


def init_game() -> None:
    """Инициализирует PyGame и задаёт заголовок и оконку окна приложения."""
    init()
    display.set_caption(settings.CAPTION)
    display.set_icon(load(path.ICON).convert_alpha())
