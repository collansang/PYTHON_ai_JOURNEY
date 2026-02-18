def generate_daily_feedback(consistency, attention, focus_score):
    messages=[]
    if attention <50:
        messages.append("Very LOW attention. Study quality is poor")
    if consistency<0.5:
        messages.append("Major plan failure. Less than half completed")
    if consistency>1.2:
        messages.append("Execution exeeded plan. Capacity maybe higher")
    if attention >=75 and consistency>=0.8:
        messages.append("High quality study day. Planning and focus aligned.")
    if focus_score<1:
        messages.append("Focus extremly low.Deep work nearly absent")
    return messages