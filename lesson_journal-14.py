# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: LessonJournal
def generate_summary(journal):
    if not journal:
        return "📋 Журнал пуст."
    
    total_lessons = len(journal)
    attended = sum(1 for l in journal if l.get("attended", False))
    completed_homeworks = sum(1 for l in journal if l.get("homework_completed", False))
    avg_score = (sum(l.get("score", 0) for l in journal) / total_lessons) if total_lessons else 0
    
    topics_covered = set()
    for l in journal:
        if "topic" in l:
            topics_covered.add(l["topic"])
    
    recent_progress = []
    for i, l in enumerate(journal[-5:], 1):
        status = ""
        if l.get("attended", False): status += "✅ "
        if l.get("homework_completed", False): status += "📝 "
        score = l.get("score", "")
        if isinstance(score, (int, float)): status += f"({score:.1f})"
        recent_progress.append(status)
    
    return (
        f"📊 Сводка за {total_lessons} уроков:\n"
        f"   Посещено: {attended}/{total_lessons}\n"
        f"   Дом. задания сдано: {completed_homeworks}/{total_lessons}\n"
        f"   Средний балл: {avg_score:.1f}\n"
        f"   Темы: {', '.join(sorted(topics_covered)) if topics_covered else '—'}\n\n"
        f"📈 Последние 5 занятий:\n" + "\n".join(recent_progress)
    )
