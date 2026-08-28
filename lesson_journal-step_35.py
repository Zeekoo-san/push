# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: LessonJournal
def get_recommendations(self):
        rec = []
        if self.lessons and not any(l.completed for l in self.lessons):
            rec.append("Начни с первого урока: 'Введение в Python'")
        if self.lessons and any(l.completed for l in self.lessons):
            rec.append("Продолжай изучение — переходи к следующему уроку")
        if self.lessons and any(l.completed for l in self.lessons) and not any(l.homework_done for l in self.lessons):
            rec.append("Выполни домашние задания по уже пройденным урокам")
        if self.attendance and not any(a.present for a in self.attendance):
            rec.append("Отсутствуешь — не пропусти следующие занятия")
        if self.progress < 100:
            rec.append("Прогресс ещё не достигнут — продолжи практику")
        if self.progress >= 100:
            rec.append("Поздравляю! Все уроки пройдены — готов к новым проектам")
        if not rec:
            rec.append("Нет рекомендаций — всё в порядке")
        return rec
