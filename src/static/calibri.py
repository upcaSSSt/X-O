from pygame import font
from pygame import Surface

from src.const import color

font.init()
instance = font.SysFont("calibri", 48)


def render(text: str) -> Surface:
    """"""
    return instance.render(text, True, color.BLACK)
