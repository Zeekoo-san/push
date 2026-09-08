# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: LessonJournal
import sys

def colorize(text: str, color: str) -> str:
    """Apply ANSI color code to text. Returns unstyled text if colors disabled."""
    if not COLORS_ENABLED:
        return text
    codes = {
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'bold': '\033[1m',
        'reset': '\033[0m',
    }
    return codes.get(color, '') + text + codes['reset']

COLORS_ENABLED = True

def set_colors_enabled(enabled: bool) -> None:
    global COLORS_ENABLED
    COLORS_ENABLED = enabled
