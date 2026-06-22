# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: LessonJournal
def edit_lesson_record(record_id, new_data):
    if not isinstance(new_data, dict) or 'topic' not in new_data:
        raise ValueError("new_data must be a dictionary containing at least 'topic'.")
    
    for i, record in enumerate(lessons_history):
        if record['id'] == record_id:
            lessons_history[i] = {**record, **new_data}
            print(f"Record #{record_id} updated successfully.")
            return True
    
    print(f"No lesson found with ID: {record_id}")
    return False
