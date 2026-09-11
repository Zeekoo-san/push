# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: LessonJournal
def backup_data(data_file, backup_dir="backups"):
    """Создаёт резервную копию JSON-данных в указанном каталоге."""
    import os, shutil, datetime

    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"journal_backup_{timestamp}.json")
    shutil.copy2(data_file, backup_path)
    return backup_path
