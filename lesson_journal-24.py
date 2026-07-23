# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: LessonJournal
def print_entry(entry):
    if not entry:
        return
    print(f"📅 {entry.get('date', '???')} | Тема: {entry.get('topic', '-')}")
    if entry.get("homework"):
        hw = entry["homework"]
        for i, h in enumerate(hw, 1):
            status = "✅ выполнена" if h.get("done", False) else "❌ не сдана"
            print(f"   {i}. {h.get('title', '-'):30s} — {status}")
    attendance = entry.get("attendance", {})
    present = sum(1 for att in attendance.values() if att == True)
    total = len(attendance)
    if total:
        print(f"   Посещаемость: {present}/{total} ({present/total*100:.0f}%)")
    progress = entry.get("progress", {})
    for key, val in progress.items():
        print(f"   📈 {key}: {val}")

# Пример использования (раскомментируй чтобы протестировать):
# entries = [
#     {"date": "2025-01-13", "topic": "Основы Python", "homework": [{"title": "Упражнение 1"}], "attendance": {"Анна": True, "Борис": False}, "progress": {"score": 85}},
#     {"date": "2025-01-14", "topic": "Циклы", "homework": [{"title": "Упражнение 2"}, {"title": "Упражнение 3"}], "attendance": {"Анна": True, "Борис": True}, "progress": {}},
# ]

# print_entry(entries[0])
