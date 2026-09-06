# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: LessonJournal
def dry_run(operation, payload):
    """Simulate an operation without writing to storage.
    Returns a dict with 'success', 'message', and 'changes'."""
    changes = []
    try:
        if operation in ('add', 'update', 'delete'):
            changes.append({'action': operation, 'payload': payload})
        elif operation in ('read', 'list'):
            changes.append({'action': operation, 'payload': payload})
        return {'success': True, 'message': f'Dry-run: {operation} simulated', 'changes': changes}
    except Exception as e:
        return {'success': False, 'message': f'Dry-run failed: {e}', 'changes': changes}
