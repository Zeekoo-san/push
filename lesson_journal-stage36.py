# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: LessonJournal
def verify_and_repair():
    """Check data integrity and repair simple problems."""
    issues = []
    if not isinstance(journal, dict):
        print("Error: journal must be a dict")
        return
    if 'topics' not in journal or 'homework' not in journal or 'attendance' not in journal:
        print("Error: missing required sections")
        return
    for topic in journal['topics']:
        if 'title' not in topic:
            topic['title'] = 'Untitled'
            issues.append('Topic missing title')
    for hw in journal['homework']:
        if 'title' not in hw:
            hw['title'] = 'Untitled Homework'
            issues.append('Homework missing title')
        if 'status' not in hw:
            hw['status'] = 'pending'
            issues.append('Homework missing status')
    if 'attendance' not in journal['attendance']:
        journal['attendance'] = {}
        issues.append('Attendance section missing')
    for student in journal.get('attendance', {}):
        if 'name' not in student:
            student['name'] = 'Unknown'
            issues.append('Attendance entry missing name')
    print(f"Data integrity check complete. Issues found and fixed: {len(issues)}")
    return issues
