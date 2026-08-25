# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: LessonJournal
def undo_last(self):
        if not self._undo_stack:
            print("Нет действий для отката.")
            return
        action = self._undo_stack.pop()
        if isinstance(action, LessonCreated):
            self._lessons.pop(action.lesson_id)
        elif isinstance(action, TopicCreated):
            topic = self._topics.pop(action.topic_id)
            self._lessons = {lid: l for lid, l in self._lessons.items() if topic.topic_id not in l.topics}
        elif isinstance(action, HomeworkCreated):
            self._homeworks.pop(action.homework_id)
        elif isinstance(action, AttendanceRecorded):
            self._attendance.pop(action.student_id)
        elif isinstance(action, ProgressUpdated):
            self._progress = action.previous_progress
        else:
            print(f"Неизвестное действие: {action}")
            return
        print(f"Отменено: {action}")
