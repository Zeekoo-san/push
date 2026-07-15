# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: LessonJournal
def add_tag_to_lesson(lesson_id, tag):
    for lesson in lessons:
        if lesson.id == lesson_id:
            if tag not in lesson.tags:
                lesson.tags.append(tag)
                return True
            else:
                print(f"Tag '{tag}' already exists for lesson {lesson_id}")
                return False
    return None

def remove_tag_from_lesson(lesson_id, tag):
    for lesson in lessons:
        if lesson.id == lesson_id and tag in lesson.tags:
            lesson.tags.remove(tag)
            return True
        else:
            print(f"Tag '{tag}' not found for lesson {lesson_id}")
            return False
