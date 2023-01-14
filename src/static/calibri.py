from pygame import font
from pygame import Surface

from src.const import color

"""Модуль для инициализации шрифтов и создания основного шрифта."""

font.init()
instance = font.SysFont("calibri", 48)


def render(text: str) -> Surface:
    """Возвращает поверхность с надписью в основном шрифте."""
    return instance.render(text, True, color.BLACK)
