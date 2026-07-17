# === Stage 20: Добавь восстановление записей из архива ===
# Project: LessonJournal
import json, os

def restore_from_archive(archive_path):
    """Восстанавливает записи из архива .json"""
    if not archive_path or not os.path.exists(archive_path):
        print("Архив не найден")
        return 0
    try:
        with open(archive_path, "r", encoding="utf-8") as f:
            records = json.load(f)
        if isinstance(records, list):
            count = len(records)
            for rec in records:
                print(f"Restored: {rec.get('topic', 'unknown')}")
            return count
        elif isinstance(records, dict):
            count = sum(1 for v in records.values() if isinstance(v, str))
            print(f"Restored {count} entries from dictionary format")
            return count
        else:
            print("Invalid archive format")
            return 0
    except Exception as e:
        print(f"Ошибка восстановления: {e}")
        return 0

def save_to_archive(records, archive_path):
    """Сохраняет записи в архив .json"""
    if not records:
        print("Нет данных для сохранения")
        return False
    try:
        with open(archive_path, "w", encoding="utf-8") as f:
            json.dump(records, f, ensure_ascii=False, indent=2)
        print(f"Архив сохранён в {archive_path}")
        return True
    except Exception as e:
        print(f"Ошибка сохранения архива: {e}")
        return False

# Пример использования
if __name__ == "__main__":
    archive_file = "journal_archive.json"
    backup_data = [
        {"topic": "Физика", "grade": 5, "date": "2024-01-15"},
        {"topic": "Математика", "grade": 4, "date": "2024-01-16"},
    ]
    save_to_archive(backup_data, archive_file)
    restored_count = restore_from_archive(archive_file)
    print(f"Восстановлено записей: {restored_count}")
