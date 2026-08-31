# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: LessonJournal
import unittest


class TestLessonJournal(unittest.TestCase):
    def test_add_topic(self):
        j = LessonJournal()
        j.add_topic("Математика")
        j.add_topic("Физика")
        self.assertEqual(len(j.topics), 2)
        self.assertIn("Математика", j.topics)
        self.assertIn("Физика", j.topics)

    def test_add_homework(self):
        j = LessonJournal()
        j.add_topic("Математика")
        j.add_homework("Математика", "Решить 10 задач")
        self.assertEqual(len(j.homeworks), 1)
        self.assertEqual(j.homeworks[0]["subject"], "Математика")
        self.assertEqual(j.homeworks[0]["task"], "Решить 10 задач")

    def test_add_attendance(self):
        j = LessonJournal()
        j.add_topic("Математика")
        j.add_attendance("Математика", "Иванов", "present")
        self.assertEqual(len(j.attendances), 1)
        self.assertEqual(j.attendances[0]["student"], "Иванов")
        self.assertEqual(j.attendances[0]["status"], "present")

    def test_progress(self):
        j = LessonJournal()
        j.add_topic("Математика")
        j.add_homework("Математика", "Решить 10 задач")
        j.add_attendance("Математика", "Иванов", "present")
        j.add_attendance("Математика", "Петров", "absent")
        progress = j.get_progress()
        self.assertEqual(progress["total_topics"], 1)
        self.assertEqual(progress["total_students"], 2)
        self.assertEqual(progress["attendance_rate"], 0.5)


if __name__ == "__main__":
    unittest.main()
