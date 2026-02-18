from datetime import date, timedelta
from core.storage import load_logs

def get_last_7_days():
    today = date.today()
    return[str(today - timedelta(days=i)) for i in range(7)]

def weekly_review():
    logs = load_logs()
    days = get_last_7_days()
    entries = [logs[d] for d in days if d in logs]
    if not entries:
        print("\nNo study data found this week.\n")
        return 
    
    total_planned = sum(e["planned_hours"] for e in entries)
    total_actual = sum(e["actual_hours"] for e in entries)
    
    avg_attention = sum(e["attention_percent"] for e in entries)/len(entries)
    avg_consistency = sum(e["consistency_ratio"] for e in entries)/len(entries)
    total_focus = sum(e["focus_score"] for e in entries)
    
    print("\nWEEKLY REVIEW\n")
    print(f"Days logged: {len(entries)} / 7")
    print(f"Total planned hours: {total_planned:.1f}")
    print(f"Total actual hours: {total_actual:.1f}")
    print(f"Average attention: {avg_attention:.1f}%")
    print(f"Average consistency: {avg_consistency:.2f}")
    print(f"Total focus score: {total_focus:.2f}\n")

    if avg_consistency < 0.6:
        print("Chronic overplanning detected. You are lying to your schedule.")
    if avg_attention < 60:
        print("Low attention. Your study hours are mostly ineffective.")
    if total_actual < 10:
        print("Extremely low study volume. This week was largely unproductive.")
    if len(entries) < 4:
        print("Inconsistent logging. Missing data hides real problems.")
    if avg_consistency > 1.2:
        print("Underplanning. Capacity higher than expectations — increase targets.")
    print("\n----------------Review complete.----------------\n")
    
if __name__ == "__main__":
    weekly_review()


