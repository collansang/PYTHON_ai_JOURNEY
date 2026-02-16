import json
from datetime import date
from pathlib import Path

DATA_DIR = Path("data")
DATA_FILE = DATA_DIR / "logs.json"


def load_logs():
    if not DATA_FILE.exists():
        return {}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_logs(logs):
    DATA_DIR.mkdir(exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=2)


def prompt(text):
    return input(text + "\n> ").strip()


def main():
    today = str(date.today())
    logs = load_logs()

    print(f"\nDaily Study Log — {today}\n")

    lessons = prompt("Lessons studied today (comma-separated)")
    planned_hours = prompt("Planned study hours (number)")
    actual_hours = prompt("Actual study hours (number)")
    attention = prompt("Estimated attentive percentage (0–100)")
    learned = prompt("Key things you learned today (use ; to separate)")
    extra = prompt("Extra research / new insights (optional)")
    confusion = prompt("What confused you or felt weak today")

    logs[today] = {
        "lessons": lessons,
        "planned_hours": planned_hours,
        "actual_hours": actual_hours,
        "attention_percent": attention,
        "learned": learned,
        "extra_research": extra,
        "confusions": confusion
    }

    save_logs(logs)

    print("\nLog saved. Close the laptop.\n")


if __name__ == "__main__":
    main()
