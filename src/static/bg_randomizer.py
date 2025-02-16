from glob import glob
from random import choice

from pygame import Surface
from pygame.image import load

from src.const import path

"""Модуль для выбора случайного фона."""

__bg_paths = glob(f'{path.BACKGROUNDS_FOLDER}/*.png')


def random_bg() -> Surface:
    """Возвращает поверхность со случайно выбранным фоновым изображенем."""
    return load(choice(__bg_paths)).convert_alpha()
