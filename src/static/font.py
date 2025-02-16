from pygame import font
from pygame import Surface

from src.const import color

"""Модуль для инициализации шрифтов и создания основного шрифта."""

font.init()
__calibri = font.SysFont("calibri", 48)


def render(text: str) -> Surface:
    """Возвращает поверхность с надписью в основном шрифте."""
    return __calibri.render(text, True, color.BLACK)
