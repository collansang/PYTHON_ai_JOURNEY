from datetime import date
from core.storage import load_logs, save_logs
from ui.input_utils import prompt, prompt_float, prompt_list
from core.metrics import (
    compute_consistency, 
    compute_focus_score, 
    compute_current_streak,
    compute_longest_streak)
from ui.feedback_engine import generate_daily_feedback


def main():
    today = date.today().isoformat()
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
    focus_hours = compute_focus_score(actual_hours, attention)
    consistency = compute_consistency(planned_hours, actual_hours)
    
    
      
    logs[today] = {
        "lessons": lessons,
        "planned_hours": planned_hours,
        "actual_hours": actual_hours,
        "attention_percent": attention,
        "consistency_ratio": consistency,
        "focus_hours": focus_hours
}
    
    save_logs(logs)
    feedback = generate_daily_feedback(consistency,attention,focus_hours)
    
    print("\nDAILY DIAGNOSTICS\n")
    for message in feedback:
        print(message)
        
    current_streak = compute_current_streak(logs)
    longest_streak = compute_longest_streak(logs)
    
    print(f"Current streak: {current_streak} days")
    print(f"Longest streak: {longest_streak} days")

        
if __name__ == "__main__":
    main()