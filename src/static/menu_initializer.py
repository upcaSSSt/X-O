from src.const import settings
from src.const import text
from src.static import font
from src.ai_mode import AIMode
from src.human_mode import HumanMode
from src.intermediate_window import IntermediateWindow
from src.window_switcher import WindowSwitcher

"""Модуль для создания игрового меню и его инициализации."""


def get_menu() -> IntermediateWindow:
    """Возвращает окно игрового меню."""
    return IntermediateWindow([], [WindowSwitcher(font.render(text.AI_GAME), AIMode()),
                                   WindowSwitcher(font.render(text.HUMAN_GAME), HumanMode())],
                              settings.SCREEN_SIZE // 2.7)
