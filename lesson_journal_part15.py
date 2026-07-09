# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: LessonJournal
import calendar
from datetime import date, timedelta


def weekly_stats(dates_list):
    """Return dict: week_start -> (weekdays_set, homework_counts)."""
    stats = {}
    for d in dates_list:
        if isinstance(d, str):
            y, m, dd = map(int, d.split('-'))
            d = date(y, m, dd)
        iso = d.isocalendar()  # (year, week, weekday)
        key = (iso[0], iso[1])
        if key not in stats:
            stats[key] = {'weekdays': set(), 'hw_counts': {}}
        stats[key]['weekdays'].add(iso[2])

    result = {}
    for week, info in stats.items():
        total_hw = sum(info['hw_counts'].values())
        result[week] = {
            'year': week[0],
            'iso_week': week[1],
            'start_date': date(week[0], 1),
            'end_date': date(week[0], calendar.monthrange(week[0], 12)[1]),
            'total_days': (info['end_date'] - info['start_date']).days + 1,
            'lesson_days': len(info['weekdays']),
            'total_hw': total_hw,
        }
    return result
