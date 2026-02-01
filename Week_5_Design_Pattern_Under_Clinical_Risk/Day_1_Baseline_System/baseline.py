"""Baseline Clinical Decision System (CDS) module.
Purpose:
    -Preserve explicit clinical reasoning
    -Preserve priority ordering
    -improve explainability over raw if/else statements
    remain fully auditable in single file
"""

#clinicak rules

def rule_severe_hypoxia(inputs):
    '''rule: Severe Hypoxia
    clinical rationalle:
    oxygen saturation below 90% risks tissue hypoxia and organ failure
    immediate ICU_level care is required'''
    if inputs['oxygen_saturation'] < 90:
        return {
                "decision": "ICU",
                "reason": "SpO2 <90% indicates severe hypoxia"}
        
def rule_Borderline_hypoxia_with_tachypnea(inputs):
    '''rule: Borderline Hypoxia with Tachypnea
    clinical rationale:
    oxygen saturation between 90-94% with respiratory rate above 20
    indicates impending respiratory failure requiring hospital admission for close monitoring and possible intervention'''
    boderline_SpO2 = 90<= inputs["oxygen_saturation"] <=94
    tachypnea = inputs["respiratory_rate"] > 20
    if boderline_SpO2 and tachypnea:
        return {
                "decision": "ADMIT",
                "reason": f"SpO2 ({inputs['oxygen_saturation']}%) with RR ({inputs['respiratory_rate']} bpm) indicates borderline hypoxia"}

def rule_hypotension(inputs):
    '''rule: Hypotension
    clinical rationale:
    systolic blood pressure below 90 mmHg indicates shock state or poor perfusion
    requiring hospital admission for hemodynamic stabilization and monitoring'''
    if inputs['systolic_bp'] < 90:
        return {
                "decision": "ADMIT",
                "reason": f"Systolic BP ({inputs['systolic_bp']} mmHg) indicates hypotension"}
        
def rule_altered_mental_status(inputs):
    '''rule: Altered Mental Status
    clinical rationale:
    Glasgow Coma Scale (GCS) below 15 indicates altered mental status
    requiring hospital admission for neurological evaluation and monitoring'''
    if inputs['gcs'] < 15:
        return {
                "decision": "ADMIT",
                "reason": f"GCS ({inputs['gcs']}) indicates altered mental status"}
        
def rule_supected_sepsis(inputs):
    '''rule: Suspected Sepsis
    clinical rationale:
    abnormal temperaturs with elevated heart rate (>100 bpm)
    indicates possible sepsis requiring hospital admission for evaluation and treatment'''
    abnormal_temperatures = (
        inputs['temperature'] > 38 or inputs['temperature'] < 36)
    tachycardia = inputs['heart_rate'] > 100
    if abnormal_temperatures and tachycardia:
        return {
                "decision": "ADMIT",
                "reason": f"abnormal temperatures ({inputs['temperature']} ℃) with HR ({inputs['heart_rate']} bpm) indicates suspected sepsis"}
        
def rule_low_grade_fever(inputs):
    '''rule: Low-grade Fever
    clinical rationale:
    temperature between 37.5-38 ℃
    may indicate mild infection or inflammation
    generally manageable with outpatient care and symptomatic treatment'''
    low_grade_fever = 37.5 <= inputs['temperature'] <= 38
    if low_grade_fever:
        return {
                "decision": "OBSERVE",
                "reason": f"Temperature ({inputs['temperature']} ℃) indicates low-grade fever"}
        
#decission engine
def clinical_decision_system(inputs):
    '''Clinical Decission System (CDS) engine
    evaluates clinical rules in priority order
    returns first matching decission'''
    rules = [
        rule_severe_hypoxia,
        rule_Borderline_hypoxia_with_tachypnea,
        rule_hypotension,
        rule_altered_mental_status,
        rule_supected_sepsis,
        rule_low_grade_fever
    ]
    
    for rule in rules:
        result = rule(inputs)
        if result is not None:
            return result
    
    return {
        "decision": "DISCHARGE",
        "reason": "No concerning clinical findings; safe for discharge"
    }
    
    
#EXAMPLE

if __name__ == "__main__":
    #example patient inputs
    patient_inputs = {
        "oxygen_saturation": 92,
        "respiratory_rate": 22,
        "systolic_bp": 120,
        "gcs": 15,
        "temperature": 37.8,
        "heart_rate": 95
    }
    
    #get clinical decision
    decision = clinical_decision_system(patient_inputs)
    
    #print result
    print(f"Clinical Decision: {decision['decision']}")
    print(f"Reason: {decision['reason']}")