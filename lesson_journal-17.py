# === Stage 17: Добавь группировку записей по категориям ===
# Project: LessonJournal
CATEGORY_TAGS = {
    "theme": "📖 Тема",
    "homework": "🏠 Домашнее задание",
    "attendance": "✅ Посещаемость",
    "progress": "🚀 Прогресс",
}


def categorize_entry(entry: dict) -> str:
    """Возвращает название категории для записи, основываясь на её типе."""
    entry_type = entry.get("type") or ""
    for key, label in CATEGORY_TAGS.items():
        if key in entry_type.lower() or entry_type == key:
            return label
    return "📝 Другое"


def group_entries_by_category(entries: list) -> dict[str, list]:
    """Группирует список записей по категориям и возвращает словарь."""
    grouped = {}
    for entry in entries:
        cat = categorize_entry(entry)
        if cat not in grouped:
            grouped[cat] = []
        grouped[cat].append(entry)
    return grouped


def display_grouped_entries(grouped: dict[str, list]) -> str:
    """Формирует читаемый отчёт по группам."""
    lines = ["📊 Группировка записей:\n"]
    for category, items in grouped.items():
        lines.append(f"  {category}\n")
        for item in items:
            title = item.get("title", "Без названия")
            date = item.get("date", "??.??.????")
            lines.append(f"    • [{date}] {title}")
    return "\n".join(lines)
