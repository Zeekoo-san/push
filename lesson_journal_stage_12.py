# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: LessonJournal
def load_from_json(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, dict) and 'lessons' in data:
            for lesson_id, lesson_data in data['lessons'].items():
                add_lesson(lesson_id, **lesson_data)
        return True
    except FileNotFoundError:
        print(f"Файл {filepath} не найден.")
        return False
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON в файле {filepath}: {e}")
        return False
    except Exception as e:
        print(f"Неожиданная ошибка при загрузке данных из {filepath}: {type(e).__name__}: {e}")
        return False
