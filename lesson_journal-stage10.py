# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: LessonJournal
def export_to_json():
    import json
    from datetime import datetime
    state = {
        "version": 1,
        "timestamp": datetime.utcnow().isoformat(),
        "lessons": lessons_data,
        "students": students_data,
        "settings": settings_data
    }
    return json.dumps(state, ensure_ascii=False, indent=2)
