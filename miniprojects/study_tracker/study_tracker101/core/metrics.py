from datetime import date,timedelta

def compute_consistency(planned, actual):
    if planned == 0:
        return 0
    return round(actual/planned, 2)

def compute_focus_score(actual_hours, attention_percent):
    return round(actual_hours*(attention_percent/100),2)

def compute_current_streak(logs):
    if not logs:
        return 0
    dates = sorted(logs.keys(),reverse=True)
    
    streak = 0
    today = date.today()
    
    while True:
        key =today.isoformat()
        if key in logs:
            streak +=1
            today -= timedelta(days=1)
        else:
            break
    return streak

def compute_longest_streak(logs):
    if not logs:
        return 0
    dates = sorted(date.fromisoformat(d) for d in logs.keys())
    longest=1
    current=1
    for i in range(1,len(dates)):
        diff = (dates[i]-dates[i-1]).days
        
        if diff==1:
            current +=1
            longest=max(longest,current)
        else:
            current=1
    return longest

def rolling_average(logs, key, days=7):
    if not logs:
        return 0
    
    today = date.today()
    start_date = today - timedelta(days=days-1)
    
    values = []
    
    for i in range(days):
        d = (start_date+timedelta(days=i)).isoformat()
        
        if d in logs and key in logs[d]:
            values.append(logs[d][key])
            
    if not values:
        return 0
    
    return round(sum(values)/len(values),2)
        
        
    