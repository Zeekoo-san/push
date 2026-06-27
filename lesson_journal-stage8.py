# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: LessonJournal
import sys, os

def print_menu():
    print("\n=== Меню LessonJournal ===")
    print("1. Показать все уроки")
    print("2. Добавить новый урок")
    print("3. Редактировать урок по ID")
    print("4. Удалить урок по ID")
    print("5. Вывести статистику посещаемости")
    print("6. Сохранить и выйти")
    print("=========================\n")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите число.")

def main():
    if not os.path.exists('journal.json'):
        with open('journal.json', 'w') as f:
            json.dump([], f)
    
    while True:
        print_menu()
        choice = get_int("Выберите действие (1-6): ")
        
        if choice == 1:
            lessons = load_data()
            for i, l in enumerate(lessons, 1):
                print(f"{i}. {l['topic']}: посещений={len(l.get('attendance', []))}, прогресс={l.get('progress', 0)}%")
        
        elif choice == 2:
            topic = input("Тема урока: ")
            hw = input("Домашнее задание (опционально): ") or ""
            lessons = load_data()
            new_id = max([l['id'] for l in lessons], default=0) + 1
            lesson = {'id': new_id, 'topic': topic, 'hw': hw, 'attendance': [], 'progress': 0}
            lessons.append(lesson)
            save_data(lessons)
            print("Урок добавлен.")
        
        elif choice == 3:
            try:
                lesson_id = get_int("ID урока для редактирования: ")
                if not any(l['id'] == lesson_id for l in load_data()):
                    print("Урок не найден.")
                    continue
                topic = input(f"Новая тема (или Enter): {input('Тема урока: ')}") or None
                hw = input(f"Новое ДЗ (или Enter): ") or ""
                lessons = load_data()
                for l in lessons:
                    if l['id'] == lesson_id:
                        if topic: l['topic'] = topic
                        if hw: l['hw'] = hw
                        break
                save_data(lessons)
            except Exception as e:
                print(f"Ошибка редактирования: {e}")

        elif choice == 4:
            try:
                lesson_id = get_int("ID урока для удаления: ")
                lessons = load_data()
                if any(l['id'] == lesson_id for l in lessons):
                    lessons[:] = [l for l in lessons if l['id'] != lesson_id]
                    save_data(lessons)
                    print("Урок удален.")
            except Exception as e:
                print(f"Ошибка удаления: {e}")

        elif choice == 5:
            lessons = load_data()
            total_attendance = sum
