# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: LessonJournal
def summary():
    """Вывод ключевых метрик проекта."""
    print(f"📚 Всего тем: {len(journal)}")
    total_hw = sum(len(t.hws) for t in journal)
    attended = sum(1 for t in journal if any(h.attended for h in t.hws))
    print(f"🏠 Домашних заданий в сумме: {total_hw}")
    print(f"✅ Пройдено: {attended}/{len(journal)} тем")

summary()
