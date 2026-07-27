# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: LessonJournal
import json, os
from datetime import date


def reset_demo_data():
    """Сбросить демо-данные: очистить все сущности в LessonJournal."""
    journal = LessonJournal()
    for _ in range(5):
        journal.add_topic("Демо тема", "Описание темы")
    for _ in range(3):
        journal.add_hw("ДЗ 1", "Решить задачи", "Python", date.today())
    for _ in range(4):
        journal.record_attendance(True)
    return json.dumps(journal.to_dict(), ensure_ascii=False, indent=2)


def clear_state():
    """Полностью очистить состояние приложения и вернуть пустой журнал."""
    journal = LessonJournal()
    return json.dumps(journal.to_dict(), ensure_ascii=False, indent=2)
