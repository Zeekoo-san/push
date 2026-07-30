# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: LessonJournal
CONFIG = {
    "app_name": "LessonJournal",
    "version": 29,
    "features": ["themes", "homework", "attendance", "progress", "config"],
    "max_homework_per_day": 5,
    "default_attendance_days": 10,
    "progress_threshold_percent": 75,
}


def get_config():
    return CONFIG
