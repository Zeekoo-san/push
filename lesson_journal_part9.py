# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: LessonJournal
import json, os, sys
from pathlib import Path

DATA_FILE = "data.json"
def load_initial_data(json_string: str) -> dict:
    """Загружает начальные данные из JSON-строки и возвращает словарь."""
    try:
        data = json.loads(json_string)
        # Валидация обязательных полей для предотвращения ошибок при старте
        required_fields = ["lessons", "students"]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Отсутствует обязательное поле в данных: {field}")
        
        # Преобразование списков уроков и студентов в словари с уникальными ID, если они еще не созданы
        lessons = {}
        for idx, lesson_data in enumerate(data.get("lessons", [])):
            if isinstance(lesson_data, dict):
                lesson_id = lesson_data.get("id") or f"lesson_{idx}"
                lessons[lesson_id] = {**lesson_data, "index": idx}
        
        students = {}
        for idx, student_data in enumerate(data.get("students", [])):
            if isinstance(student_data, dict):
                student_id = student_data.get("id") or f"student_{idx}"
                students[student_id] = {**student_data, "index": idx}
        
        # Сохранение загруженных данных в файл для последующего использования (если не существует)
        if not os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        
        return {"lessons": lessons, "students": students}
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON данных: {e}")
        sys.exit(1)

# Пример использования с тестовой строкой (замените на ваш реальный JSON при запуске)
if __name__ == "__main__":
    initial_json = '''
{
  "lessons": [
    {"id": "math_101", "title": "Основы алгебры", "duration_minutes": 45},
    {"id": "phys_202", "title": "Механика", "duration_minutes": 90}
  ],
  "students": [
    {"id": "s1", "name": "Алексей", "grade": 10},
    {"id": "s2", "name": "Мария", "grade": 10}
  ]
}'''

    loaded_data = load_initial_data(initial_json)
    print(f"Загружено {len(loaded_data['lessons'])} уроков и {len(loaded_data['students'])} студентов.")
