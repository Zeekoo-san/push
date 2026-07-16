# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: LessonJournal
def archive_lessons(journal_data):
    """Archive completed or old lessons into a separate dict."""
    archived = []
    active = []
    for entry in journal_data:
        if entry.get("status") in ("completed", "archived"):
            entry_copy = dict(entry)
            entry_copy["archive_date"] = datetime.now().isoformat()
            archived.append(entry_copy)
        else:
            active.append(entry)
    journal_data["lessons"] = active
    return {"active": active, "archived": archived}
