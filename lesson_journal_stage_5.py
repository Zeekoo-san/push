# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: LessonJournal
def delete_entry(entry_id: int) -> bool:
    if not entries or entry_id <= 0:
        print(f"Ошибка: запись с ID {entry_id} не найдена или идентификатор недопустим.")
        return False
    
    for i, record in enumerate(entries):
        if record['id'] == entry_id:
            deleted = entries.pop(i)
            print(f"Запись удалена: {deleted}")
            return True
    
    print(f"Ошибка: запись с ID {entry_id} не найдена в журнале.")
    return False

def get_entry_by_id(entry_id: int) -> dict | None:
    if not entries or entry_id <= 0:
        return None
        
    for record in entries:
        if record['id'] == entry_id:
            return record
            
    return None
