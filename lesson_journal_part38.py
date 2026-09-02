# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: LessonJournal
import unittest


class TestErrorEdgeCases(unittest.TestCase):

    def test_empty_topic_name(self):
        from lesson_journal.models.topic import Topic
        topic = Topic(name="", description="test")
        self.assertEqual(topic.name, "")

    def test_topic_with_unicode(self):
        from lesson_journal.models.topic import Topic
        topic = Topic(name="Привет мир 🌍", description="unicode test")
        self.assertEqual(topic.name, "Привет мир 🌍")

    def test_homework_empty_content(self):
        from lesson_journal.models.homework import Homework
        hw = Homework(topic=Topic(name="hw_test"), content="", due_date=None)
        self.assertEqual(hw.content, "")

    def test_homework_no_due_date(self):
        from lesson_journal.models.homework import Homework
        hw = Homework(topic=Topic(name="no_deadline"), content="test", due_date=None)
        self.assertIsNone(hw.due_date)

    def test_attendance_missing_student(self):
        from lesson_journal.models.attendance import Attendance
        att = Attendance(student_name="Absent", topic=Topic(name="missing"))
        self.assertEqual(att.student_name, "Absent")

    def test_progress_zero_days(self):
        from lesson_journal.models.progress import Progress
        prog = Progress(topic=Topic(name="progress_test"), days_completed=0)
        self.assertEqual(prog.days_completed, 0)

    def test_topic_id_generation(self):
        from lesson_journal.models.topic import Topic
        t1 = Topic(name="first")
        t2 = Topic(name="second")
        self.assertNotEqual(t1.id, t2.id)

    def test_homework_id_generation(self):
        from lesson_journal.models.homework import Homework
        hw1 = Homework(topic=Topic(name="hw1"), content="task1")
        hw2 = Homework(topic=Topic(name="hw2"), content="task2")
        self.assertNotEqual(hw1.id, hw2.id)


if __name__ == "__main__":
    unittest.main()
