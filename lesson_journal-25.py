# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: LessonJournal
def parse_date(date_str):
    """Parse date string in DD.MM.YYYY or YYYY-MM-DD format."""
    import re
    if not isinstance(date_str, str) or len(date_str.strip()) == 0:
        return None
    try:
        cleaned = date_str.strip()
        # Try DD.MM.YYYY
        if re.match(r'^\d{2}\.\d{2}\.\d{4}$', cleaned):
            parts = cleaned.split('.')
            day, month, year = int(parts[0]), int(parts[1]), int(parts[2])
        else:
            # Try YYYY-MM-DD
            if re.match(r'^\d{4}-\d{2}-\d{2}$', cleaned):
                parts = cleaned.split('-')
                day, month, year = int(parts[2]), int(parts[1]), int(parts[0])
            else:
                return None
        # Validate ranges
        if not (1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2100):
            return None
        return date_str.strip()
    except Exception:
        return None
