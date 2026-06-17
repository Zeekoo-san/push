# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: LessonJournal
import json
from datetime import date, timedelta
from typing import Optional

class LessonJournal:
    def __init__(self):
        self._lessons: list[dict] = []
        self._students: dict[str, dict] = {}
        self._config_path: str = "journal.json"

    def _load(self) -> None:
        try:
            with open(self._config_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self._lessons = data.get('lessons', [])
                self._students = {k: v for k, v in data.get('students', {}).items()}
        except FileNotFoundError:
            pass

    def _save(self) -> None:
        with open(self._config_path, 'w', encoding='utf-8') as f:
            json.dump({'lessons': self._lessons, 'students': self._students}, f, ensure_ascii=False, indent=2)

    def add_lesson(self, topic: str, homework: Optional[str] = None) -> dict:
        lesson_id = len(self._lessons) + 1
        now = date.today().isoformat()
        entry = {
            'id': lesson_id,
            'topic': topic,
            'homework': homework,
            'date': now,
            'attendance': {}
        }
        self._lessons.append(entry)
        self._save()
        return entry

    def register_attendance(self, student_name: str, lesson_id: int, status: bool = True) -> None:
        if not self._students.get(student_name):
            self._students[student_name] = {'name': student_name}
        for lesson in self._lessons:
            if lesson['id'] == lesson_id and 'attendance' in lesson:
                lesson['attendance'][student_name] = status

    def get_progress(self, student_name: str) -> dict:
        total_lessons = len(self._lessons)
        attended = sum(1 for l in self._lessons if student_name in l.get('attendance', {}) and l['attendance'][student_name])
        return {'name': student_name, 'attended': attended, 'total': total_lessons}

    def get_all_data(self) -> dict:
        return {'lessons': self._lessons, 'students': self._students}
