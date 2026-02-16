def compute_consistency(planned, actual):
    if planned == 0:
        return 0
    return round(actual/planned, 2)

def compute_focus_score(actual_hours, attention_percent):
    return round(actual_hours*(attention_percent/100),2)