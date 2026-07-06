# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: LessonJournal
def search_journal(query: str) -> list[dict]:
    """Поиск записей журнала по нескольким полям без учёта регистра."""
    if not query or len(query.strip()) < 1:
        return []
    q = query.lower().strip()
    results = []
    for entry in journal_entries:
        fields_to_check = [
            "theme",
            "topic",
            "homework_description",
            "attendance_status",
            "progress_note",
            "student_name",
            "date",
        ]
        found = False
        for field in fields_to_check:
            if q in str(entry.get(field, "")).lower():
                found = True
                break
        if found:
            results.append(entry)
    return results
