# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: LessonJournal
def print_table(journal):
    """Компактный вывод журнала уроков в таблицу."""
    rows = []
    for entry in journal:
        rows.append({
            "Тема": entry["topic"],
            "ДЗ": entry.get("homework", ""),
            "Дата": entry.get("date", ""),
            "Посещённость": "✅" if entry.get("attended", False) else "❌",
            "Прогресс": f"{entry.get('progress', 0)}%",
        })

    headers = ["Тема", "ДЗ", "Дата", "Посещённость", "Прогресс"]
    widths = [len(h) for h in headers]
    for row in rows:
        for i, val in enumerate(row.values()):
            widths[i] = max(widths[i], len(str(val)))

    sep = "─" * (sum(widths) + 3 * (len(rows) - 1))
    header_line = "│" + "┌" + "──" + "┬" + "".join(["──" for _ in range(len(headers)-1)]) + "┐"

    print(sep)
    print(header_line)
    print("│", end="")
    for i, h in enumerate(headers):
        print(f" {h:<{widths[i]}} │", end="")
    print()
    print("│", end="")
    for i, _ in enumerate(headers):
        print("─" * widths[i], end="│")
    print()

    for idx, row in enumerate(rows):
        if idx > 0:
            print("│", end="")
            for i, _ in enumerate(headers):
                print("├" + "──" + "┼", end="")
            print()
        print("│", end="")
        for i, val in enumerate(row.values()):
            print(f" {val:<{widths[i]}} │", end="")
        print()

    print(sep)
