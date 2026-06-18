# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: LessonJournal
class ValidationError(Exception): pass

def validate_topic(topic: str) -> str:
    if not topic or len(topic.strip()) > 100: raise ValidationError("Тема должна быть непустой и до 100 символов.")
    return topic.strip()

def validate_homework(homework: str, max_lines: int = 5) -> tuple[str, bool]:
    if not homework or len(homework.splitlines()) > max_lines: raise ValidationError(f"ДЗ не может превышать {max_lines} строк.")
    return homework.strip(), True

def validate_attendance(status: str) -> bool:
    valid_statuses = {"present", "absent", "late"}
    if status.lower() not in valid_statuses: raise ValidationError(f"Статус посещаемости должен быть одним из: {', '.join(valid_statuses)}.")
    return status.lower() == "present"

def validate_progress(progress: float) -> float:
    if progress < 0 or progress > 100: raise ValidationError("Прогресс должен быть от 0 до 100.")
    return round(progress, 2)
