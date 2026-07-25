# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: LessonJournal
def demo():
    """Compact manual-testing helpers for LessonJournal."""
    from lesson_journal import (Lesson, Topic, Homework, Attendance,
                                Progress, Journal)

    # ── topics & lessons ────────────────────────────────
    t1 = Topic("Functions", "2024-09-01")
    t2 = Topic("Classes", "2024-09-08")
    t3 = Topic("OOP", "2024-09-15")

    l1a = Lesson(t1, [Homework("draw a function diagram"),
                       Homework("read chapter 3")])
    l1b = Lesson(t1, [])
    l2a = Lesson(t2, [])
    l3a = Lesson(t3, [Homework("design a class hierarchy")])

    # ── attendance (auto-filled if missing) ─────────────
    for L in [l1a, l1b, l2a, l3a]:
        Attendance(L)

    # ── progress snapshot ───────────────────────────────
    progress = Progress()
    progress.total_lessons = 4
    progress.attended_count = 3
    progress.avg_score = 8.5
    progress.current_topic_idx = 1

    # ── demo journal (single object, read-only) ─────────
    j = Journal()
    for T in [t1, t2, t3]:
        j.add_topic(T)
    for L in [l1a, l1b, l2a, l3a]:
        j.add_lesson(L)

    # ── output helpers (printable summaries) ────────────
    def header(): print("=" * 60)
    def topics_summary():
        print(f"Topics: {len(j.topics)}")
        for T in j.topics:
            lessons = [L for L in j.lessons if L.topic == T]
            attended = sum(1 for A in Attendance.objects if A.lesson in lessons)
            print(f"  • {T.name} ({T.date}) – {len(lessons)} lessons, "
                  f"{attended} attended")

    def lessons_summary():
        print(f"\nLessons: {len(j.lessons)}")
        for L in j.lessons:
            hw = [H.text for H in L.homeworks] if L.homeworks else []
            att = "✓" if any(A.lesson == L for A in Attendance.objects) else "✗"
            print(f"  • {L.topic.name}/{L.number} – {att}")

    def progress_summary():
        print(f"\nProgress:")
        print(f"  lessons: {progress.total_lessons}, attended: {progress.attended_count}, avg score: {progress.avg_score}")
        print(f"  current topic: {j.topics[progress.current_topic_idx].name if progress.current_topic_idx < len(j.topics) else '—'}")

    # ── run all demos ───────────────────────────────────
    header()
    topics_summary()
    lessons_summary()
    progress_summary()
