from pygame import init
from pygame import display
from pygame.image import load

from src.const import settings
from src.const import path

""""""

screen = display.set_mode((settings.SCREEN_SIZE, settings.SCREEN_SIZE))


def init_pygame() -> None:
    """"""
    init()
    display.set_caption(settings.CAPTION)
    display.set_icon(load(path.ICON).convert_alpha())
