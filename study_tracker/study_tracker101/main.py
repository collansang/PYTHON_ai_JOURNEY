from datetime import date
from core.storage import load_logs, save_logs
from ui.input_utils import prompt, prompt_float, prompt_list
from core.metrics import compute_consistency, compute_focus_score



def main():
    today = str(date.today())
    logs = load_logs()
    
    print(f"\nDAILY STUDY LOG - {today}\n")

    if today in logs:
        overwrite = prompt("log alredy exists. Overwrite??y/n: ")
        if overwrite.lower() != "y":
            print("Aborted.")
        return
    lessons = prompt_list("Lessons studied (, separated): ")
    planned_hours= prompt_float("Planned study hours: ", 0)
    actual_hours= prompt_float("Actual study hours: ",0)
    attention= prompt_float("Attention percentage (0-100)",0,100)
    consistency = compute_consistency(planned_hours, actual_hours)
    focus_hours = compute_focus_score(actual_hours, attention)
        
    logs[today] = {
        "lessons": lessons,
        "planned_hours": planned_hours,
        "actual_hours": actual_hours,
        "attention_percent": attention,
        "consistency_ratio": consistency,
        "focus_score": focus_hours
}

    save_logs(logs)
        
if __name__ == "__main__":
    main()