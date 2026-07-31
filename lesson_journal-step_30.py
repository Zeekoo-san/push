# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: LessonJournal
class Profile:
    def __init__(self, name, avatar="👤", grade=0):
        self.name = name
        self.avatar = avatar
        self.grade = grade
    
    def add_score(self, amount):
        self.grade += amount
    
    def reset_grade(self):
        self.grade = 0

class ProfileManager:
    _profiles = {}
    
    @classmethod
    def register(cls, profile):
        cls._profiles[profile.name] = profile
    
    @classmethod
    def get(cls, name):
        return cls._profiles.get(name)
    
    @classmethod
    def list_all(cls):
        return dict(sorted(cls._profiles.items(), key=lambda x: x[1].grade))

def add_profile_menu():
    print("\n--- Управление профилями ---")
    profiles = ProfileManager.list_all()
    if not profiles:
        print("Нет сохранённых профилей. Создайте первый:")
        name = input("Имя профиля: ").strip() or "Студент"
        profile = Profile(name)
        ProfileManager.register(profile)
        print(f"Профиль '{name}' создан.")
    else:
        for p in profiles.values():
            print(f"  [{p.avatar}] {p.name} — баллы: {p.grade}")
        name = input("\n1. Выбрать профиль по имени\n2. Создать новый профиль\nВыбор (1/2): ").strip() or "1"
        if name == "2":
            new_name = input("Имя нового профиля: ").strip() or "Студент"
            profile = Profile(new_name)
            ProfileManager.register(profile)
            print(f"Профиль '{new_name}' создан.")
        else:
            selected = input("Введите имя профиля: ").strip() or list(profiles.keys())[0]
            profile = ProfileManager.get(selected)
            if not profile:
                print("Профиль не найден.")
            else:
                print(f"Текущий профиль: {profile.name} ({profile.avatar}), баллы: {profile.grade}")
