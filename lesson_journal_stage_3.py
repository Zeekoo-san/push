# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: LessonJournal
import json
from datetime import datetime, timedelta
from typing import Optional, List, Dict, Any

class LessonJournal:
    def __init__(self):
        self._data: Dict[str, Any] = {
            "lessons": [],
            "attendance": {},  # date -> set of student_ids
            "progress": {}     # topic_id -> completion_percentage
        }
    
    def add_lesson(self, topic: str, homework: Optional[str], duration_minutes: int) -> None:
        lesson = {
            "id": len(self._data["lessons"]) + 1,
            "topic": topic,
            "homework": homework or "",
            "duration_minutes": duration_minutes,
            "created_at": datetime.now().isoformat()
        }
        self._data["lessons"].append(lesson)
    
    def mark_attendance(self, student_id: str, date: Optional[datetime] = None) -> None:
        if not date:
            date = datetime.now()
        date_key = date.strftime("%Y-%m-%d")
        if student_id not in self._data["attendance"]:
            self._data["attendance"][student_id] = set()
        self._data["attendance"][student_id].add(date_key)
    
    def update_progress(self, topic: str, completed_items_count: int, total_items: int) -> None:
        if not total_items:
            return
        percentage = round((completed_items_count / total_items) * 100, 2)
        self._data["progress"][topic] = {
            "total": total_items,
            "completed": completed_items_count,
            "percentage": percentage
        }

# Пример использования (необязательно для хранения в памяти):
if __name__ == "__main__":
    journal = LessonJournal()
    journal.add_lesson("Основы Python", "Решить 5 задач на циклы", 60)
    journal.mark_attendance("student_1")
    journal.update_progress("Основы Python", 3, 5)
