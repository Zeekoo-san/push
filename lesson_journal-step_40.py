# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: LessonJournal
import argparse

def main():
    parser = argparse.ArgumentParser(description="LessonJournal CLI")
    sub = parser.add_subparsers(dest="command")

    # new-lesson
    p_new = sub.add_parser("new-lesson")
    p_new.add_argument("--topic", required=True)
    p_new.add_argument("--file", default="lessons.json")

    # add-hw
    p_hw = sub.add_parser("add-hw")
    p_hw.add_argument("--lesson", required=True)
    p_hw.add_argument("--task", required=True)

    # mark-attendance
    p_att = sub.add_parser("mark-attendance")
    p_att.add_argument("--lesson", required=True)
    p_att.add_argument("--student", required=True)
    p_att.add_argument("--present", action="store_true")

    # progress
    p_prog = sub.add_parser("progress")
    p_prog.add_argument("--lesson", required=True)
    p_prog.add_argument("--student", required=True)
    p_prog.add_argument("--file", default="progress.json")

    args = parser.parse_args()
    if args.command in ("new-lesson", "add-hw", "mark-attendance", "progress"):
        cmd_map = {
            "new-lesson": new_lesson,
            "add-hw": add_hw,
            "mark-attendance": mark_attendance,
            "progress": show_progress,
        }
        cmd_map[args.command](args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
