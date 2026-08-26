# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: LessonJournal
TEMPLATES = {
    "daily": {
        "title": "Урок: {date}",
        "fields": {
            "date": "строка",
            "topic": "строка",
            "attendance": "bool",
            "homework": "строка",
        },
    },
    "weekly": {
        "title": "Неделя: {week}",
        "fields": {
            "week": "строка",
            "summary": "строка",
            "attendance": "int",
            "homework": "строка",
        },
    },
}

def apply_template(template_name, data):
    if template_name not in TEMPLATES:
        raise ValueError(f"Неизвестный шаблон: {template_name}")
    tpl = TEMPLATES[template_name]
    filled = tpl["title"].format(**data)
    for field, value in data.items():
        if field in tpl["fields"]:
            filled += f"\n{field}: {value}"
    return filled
