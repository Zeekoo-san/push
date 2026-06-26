# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: LessonJournal
from operator import itemgetter, attrgetter
def sort_entries(entries, key='date', reverse=False):
    if key == 'name': return sorted(entries, key=lambda x: (x.get('priority') or 0, x['topic'].lower()))
    if key == 'priority': return sorted(entries, key=lambda x: (x.get('priority') or 1) * -1)
    if key == 'date': return sorted(entries, key=lambda x: x.get('created_at', ''), reverse=reverse)
    raise ValueError(f"Unknown sort key: {key}")
