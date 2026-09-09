# === Stage 43: Добавь пагинацию длинных списков ===
# Project: LessonJournal
def show_page(data, page_size=10):
    pages = [data[i:i+page_size] for i in range(0, len(data), page_size)]
    for page in pages:
        print(f"--- Страница ---")
        for item in page:
            print(item)
    print(f"Всего страниц: {len(pages)}")
