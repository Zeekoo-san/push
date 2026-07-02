# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: LessonJournal
import json, os

DATA_FILE = "journal_data.json"

def save_to_file(data):
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except IOError as e:
        print(f"Ошибка сохранения в {DATA_FILE}: {e}")

def load_from_file():
    if not os.path.exists(DATA_FILE):
        return {"lessons": [], "students": {}, "attendance": []}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Восстановление структуры по умолчанию если файл повреждён или старая версия
            if not isinstance(data.get("lessons"), list): data["lessons"] = []
            if not isinstance(data.get("students"), dict): data["students"] = {}
            if not isinstance(data.get("attendance"), list): data["attendance"] = []
            return data
    except (json.JSONDecodeError, IOError) as e:
        print(f"Ошибка чтения {DATA_FILE}: {e}")
        return {"lessons": [], "students": {}, "attendance": []}

def initialize_data():
    if not os.path.exists(DATA_FILE):
        save_to_file({"lessons": [], "students": {}, "attendance": []})
