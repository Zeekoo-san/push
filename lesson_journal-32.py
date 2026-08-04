# === Stage 32: Добавь журнал действий пользователя ===
# Project: LessonJournal
class ActionLog:
    def __init__(self):
        self.entries = []

    def log(self, user: str, action: str, details: str = ""):
        entry = {
            "user": user,
            "action": action,
            "details": details,
            "timestamp": time.time(),
        }
        self.entries.append(entry)

    def get_log(self):
        return self.entries.copy()

    def clear_log(self):
        self.entries.clear()


# Примеры использования:
log = ActionLog()
log.log("Admin", "created_topic", "Topic: Algebra 101")
log.log("Student_42", "completed_homework", "Homework: #5, Score: 95/100")
log.log("Teacher_Alice", "updated_attendance", "Marked Student_7 absent today")

print(f"Total actions logged: {len(log.get_log())}")
