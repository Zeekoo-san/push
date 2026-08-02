# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: LessonJournal
def switch_profile():
    if not current_profiles:
        print("Нет сохранённых профилей. Создайте хотя бы один.")
        return
    name = input(f"Выберите профиль (введите имя или '{get_current_name()}' для возврата): ").strip()
    target = next((p for p in current_profiles if p["name"] == name), None)
    if not target:
        print("Профиль не найден.")
        return
    set_profile(target)
