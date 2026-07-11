# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: LessonJournal
from datetime import date, timedelta


def monthly_stats(records: list[dict], months: int = 12) -> dict[str, dict]:
    """Вычисляет статистику по месяцам за N последних месяцев."""
    if not records:
        return {}
    
    today = date.today()
    start_date = today - timedelta(days=30 * months)
    end_date = today
    
    stats = {m.strftime('%Y-%m'): {'total_lessons': 0, 'attended': 0, 'homework_submitted': 0} for m in range(start_date, end_date + timedelta(days=1), timedelta(days=30))}
    
    for record in records:
        lesson_date = record.get('date') or date.fromisoformat(record['date'])
        month_key = lesson_date.strftime('%Y-%m')
        
        if month_key not in stats:
            continue
        
        stats[month_key]['total_lessons'] += 1
        if record.get('attended'):
            stats[month_key]['attended'] += 1
        if record.get('homework_submitted'):
            stats[month_key]['homework_submitted'] += 1
    
    return stats


# Пример использования:
monthly = monthly_stats(lesson_records, months=3)
for month, data in monthly.items():
    print(f"{month}: {data['attended']}/{data['total_lessons']} уроков посетили")
