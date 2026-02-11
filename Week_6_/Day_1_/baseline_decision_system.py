"""
Baseline Clinical Decision System (NO PATTERNS)

"""

from datetime import datetime


# -------------------------
# Logging utilities
# -------------------------

def log_event(event_type, payload):
    """
    Centralized logging function.
    This is NOT a pattern — just a helper to avoid print chaos.

    Why this exists:
    - Clinical systems must preserve a timeline of reasoning
    - Logs are medico-legal artifacts, not debug noise
    """
    timestamp = datetime.utcnow().isoformat()
    print(f"[{timestamp}] {event_type.upper()}: {payload}")


# -------------------------
# Decision logic
# -------------------------

def assess_patient(
    oxygen_saturation,
    respiratory_rate,
    systolic_bp,
    consciousness_level
):
    """
    Main clinical assessment function.

    Inputs:
    - oxygen_saturation (%)
    - respiratory_rate (breaths/min)
    - systolic_bp (mmHg)
    - consciousness_level (string: 'alert', 'confused', 'unresponsive')

    Output:
    - dict containing decision and rationale
    """

    log_event("input", {
        "oxygen_saturation": oxygen_saturation,
        "respiratory_rate": respiratory_rate,
        "systolic_bp": systolic_bp,
        "consciousness_level": consciousness_level
    })

    # -------------------------
    # Decision path starts here
    # -------------------------

    # Rule 1: Severe hypoxia
    # Clinical rationale:
    # Oxygen saturation below 90% significantly increases risk of
    # tissue hypoxia, organ failure, and cardiac arrest.
    if oxygen_saturation < 90:
        log_event("decision_path", "oxygen_saturation < 90 → severe hypoxia")

        decision = {
            "acuity": "critical",
            "action": "immediate ICU admission",
            "reason": "Severe hypoxia"
        }

        log_event("output", decision)
        return decision

    # Rule 2: Impending respiratory failure
    # Clinical rationale:
    # Respiratory rate > 30 suggests exhaustion or failure
    # even if oxygen saturation is temporarily preserved.
    if respiratory_rate > 30:
        log_event("decision_path", "respiratory_rate > 30 → respiratory distress")

        decision = {
            "acuity": "high",
            "action": "urgent respiratory support",
            "reason": "Severe tachypnea"
        }

        log_event("output", decision)
        return decision

    # Rule 3: Hypotension
    # Clinical rationale:
    # Systolic BP < 90 mmHg indicates shock until proven otherwise.
    if systolic_bp < 90:
        log_event("decision_path", "systolic_bp < 90 → hypotension")

        decision = {
            "acuity": "high",
            "action": "fluid resuscitation and monitoring",
            "reason": "Hypotension"
        }

        log_event("output", decision)
        return decision

    # Rule 4: Altered mental status
    # Clinical rationale:
    # Changes in consciousness may reflect hypoxia, hypoperfusion,
    # infection, metabolic derangement, or CNS pathology.
    if consciousness_level in ["confused", "unresponsive"]:
        log_event(
            "decision_path",
            f"consciousness_level == {consciousness_level} → altered mental status"
        )

        decision = {
            "acuity": "high",
            "action": "urgent neurological evaluation",
            "reason": "Altered mental status"
        }

        log_event("output", decision)
        return decision

    # Rule 5: No immediate red flags
    # Clinical rationale:
    # Absence of critical thresholds does NOT mean safe —
    # it means no *immediate* life-threatening indicators detected.
    log_event("decision_path", "no critical thresholds met")

    decision = {
        "acuity": "moderate",
        "action": "standard monitoring",
        "reason": "No immediate life-threatening findings"
    }

    log_event("output", decision)
    return decision


# -------------------------
# Manual test execution
# -------------------------

if __name__ == "__main__":
    # This is intentionally crude.
    # Real systems do not get the luxury of pretty test harnesses.

    assess_patient(
        oxygen_saturation=88,
        respiratory_rate=22,
        systolic_bp=110,
        consciousness_level="alert"
    )

    assess_patient(
        oxygen_saturation=95,
        respiratory_rate=35,
        systolic_bp=120,
        consciousness_level="alert"
    )

    assess_patient(
        oxygen_saturation=96,
        respiratory_rate=18,
        systolic_bp=85,
        consciousness_level="confused"
    )
