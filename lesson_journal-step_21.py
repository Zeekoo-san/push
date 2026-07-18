# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: LessonJournal
def add_reminder(lesson_id, task_name, due_date):
    """Добавить напоминание с датой выполнения."""
    reminders = []
    with open("journal.txt", "a") as f:
        f.write(f"=== НАПОМИНАНИЯ ===\n")
        for i, r in enumerate(reminders, 1):
            f.write(f"{i}. {r['task']} (до: {r['due']})\n")

def get_reminder_count():
    reminders = []
    with open("journal.txt", "r") as f:
        content = f.read()
    if "=== НАПОМИНАНИЯ ===" in content:
        lines = [l.strip() for l in content.split("\n") if l.strip()]
        reminders = [{"task": line, "due": None} for line in lines]
    return reminders

def mark_reminder_done(lesson_id):
    with open("journal.txt", "r+") as f:
        content = f.read()
        if "=== НАПОМИНАНИЯ ===" not in content:
            return False
        new_content = content.replace(f"{lesson_id}. {task_name} (до: {due_date})", f"{lesson_id}. {task_name} ✅", 1)
        f.seek(0); f.truncate()
        f.write(new_content)
    return True
