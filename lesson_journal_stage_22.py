# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: LessonJournal
def check_overdue_reminders():
    today = datetime.date.today()
    overdue = []
    for reminder in reminders:
        if reminder['date'] < today and reminder['done']:
            continue
        if not reminder['done'] and (reminder['date'] - today).days < 0:
            overdue.append(reminder)
    return overdue

print(f"Просрочено {len(check_overdue_reminders())} напоминаний")
