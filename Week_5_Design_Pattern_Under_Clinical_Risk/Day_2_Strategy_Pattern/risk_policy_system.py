"""
Clinical Risk Policy System
---------------------------

Design guarantees:
- No hidden thresholds
- No silent version upgrades
- No implicit policy selection
- Full auditability
- Single evaluation logic

If any of these guarantees are weakened, delete this system.
"""

from dataclasses import dataclass
from datetime import date
from typing import Dict, List, Set, Literal


# ============================================================
# Exceptions (Fail Loud, Fail Early)
# ============================================================

class PolicySelectionError(Exception):
    pass


class PolicyEvaluationError(Exception):
    pass


# ============================================================
# Guideline Citation (Evidence, Not Comments)
# ============================================================

@dataclass(frozen=True)
class GuidelineCitation:
    authority: str
    document: str
    version: str
    published_date: date
    url: str

    def reference(self) -> str:
        return f"{self.authority} — {self.document} ({self.version})"


# ============================================================
# Clinical Context (Policy Cannot Be Chosen Without This)
# ============================================================

@dataclass(frozen=True)
class ClinicalContext:
    care_setting: Literal["ED", "ICU", "WARD"]
    patient_population: Literal["ADULT", "PEDIATRIC"]
    condition_focus: Literal["RESPIRATORY"]


# ============================================================
# Risk Policy (Pure Data, Immutable)
# ============================================================

@dataclass(frozen=True)
class RiskPolicy:
    policy_id: str                  # stable lineage ID
    version: str                    # semantic versioning
    criteria: Dict[str, float]      # explicit thresholds
    assumptions: List[str]
    risk_profile: str
    guideline: GuidelineCitation
    allowed_contexts: Set[ClinicalContext]


# ============================================================
# Policy Selection (NO DEFAULTS, NO GUESSING)
# ============================================================

@dataclass(frozen=True)
class PolicySelectorConfig:
    policy_id: str
    allowed_versions: Set[str]


def select_policy(
    policies: List[RiskPolicy],
    context: ClinicalContext,
    config: PolicySelectorConfig
) -> RiskPolicy:
    """
    Explicit policy selection.
    Any ambiguity or absence is a hard failure.
    """

    candidates = [
        p for p in policies
        if p.policy_id == config.policy_id
        and p.version in config.allowed_versions
        and context in p.allowed_contexts
    ]

    if len(candidates) == 0:
        raise PolicySelectionError(
            f"No policy found for ID={config.policy_id}, "
            f"versions={config.allowed_versions}, context={context}"
        )

    if len(candidates) > 1:
        raise PolicySelectionError(
            f"Ambiguous policy selection for ID={config.policy_id}. "
            f"Matched versions: {[p.version for p in candidates]}"
        )

    return candidates[0]


# ============================================================
# Single Evaluator (Logic Lives HERE and ONLY HERE)
# ============================================================

def evaluate_risk(policy: RiskPolicy, patient: Dict[str, float]) -> bool:
    """
    Centralized, auditable evaluation logic.
    Any policy incompatible with this logic is invalid by design.
    """

    try:
        return (
            patient["spo2"] < policy.criteria["spo2_below"]
            and patient["rr"] > policy.criteria["rr_above"]
        )
    except KeyError as e:
        raise PolicyEvaluationError(
            f"Missing required patient field: {e}"
        )


# ============================================================
# Mandatory Audit Record
# ============================================================

def evaluate_with_audit(
    policy: RiskPolicy,
    context: ClinicalContext,
    patient: Dict[str, float]
) -> Dict:
    """
    Evaluation without audit is considered invalid.
    """

    result = evaluate_risk(policy, patient)

    return {
        "policy_id": policy.policy_id,
        "policy_version": policy.version,
        "care_setting": context.care_setting,
        "patient_population": context.patient_population,
        "condition": context.condition_focus,
        "guideline": policy.guideline.reference(),
        "criteria_used": policy.criteria,
        "assumptions": policy.assumptions,
        "risk_profile": policy.risk_profile,
        "result": result
    }


# ============================================================
# Example Guidelines
# ============================================================

WHO_RESP_2023 = GuidelineCitation(
    authority="WHO",
    document="Clinical management of acute respiratory illness",
    version="2023",
    published_date=date(2023, 6, 1),
    url="https://www.who.int/publications/i/item/WHO-ARI-2023"
)

NICE_COPD_2024 = GuidelineCitation(
    authority="NICE",
    document="COPD management",
    version="2024",
    published_date=date(2024, 2, 10),
    url="https://www.nice.org.uk/guidance/copd"
)


# ============================================================
# Contexts
# ============================================================

ED_ADULT_RESP = ClinicalContext(
    care_setting="ED",
    patient_population="ADULT",
    condition_focus="RESPIRATORY"
)


# ============================================================
# Policies (Same ID, Different Versions)
# ============================================================

CONSERVATIVE_RESP_V1 = RiskPolicy(
    policy_id="RESP_RISK",
    version="1.0.0",
    criteria={
        "spo2_below": 94,
        "rr_above": 22
    },
    assumptions=[
        "Adult patient",
        "Room air",
        "Reliable pulse oximetry"
    ],
    risk_profile="High sensitivity; early escalation",
    guideline=WHO_RESP_2023,
    allowed_contexts={ED_ADULT_RESP}
)

PERMISSIVE_RESP_V2 = RiskPolicy(
    policy_id="RESP_RISK",
    version="2.0.0",
    criteria={
        "spo2_below": 90,
        "rr_above": 28
    },
    assumptions=[
        "Known COPD",
        "Chronic hypoxemia baseline",
        "Continuous monitoring available"
    ],
    risk_profile="Lower sensitivity; avoids over-admission",
    guideline=NICE_COPD_2024,
    allowed_contexts={ED_ADULT_RESP}
)


ALL_POLICIES = [
    CONSERVATIVE_RESP_V1,
    PERMISSIVE_RESP_V2
]


# ============================================================
# Example Usage (Intentional, Explicit)
# ============================================================

if __name__ == "__main__":

    patient_data = {
        "spo2": 91,
        "rr": 26
    }

    selector_config = PolicySelectorConfig(
        policy_id="RESP_RISK",
        allowed_versions={"1.0.0"}   # explicit pin
    )

    selected_policy = select_policy(
        policies=ALL_POLICIES,
        context=ED_ADULT_RESP,
        config=selector_config
    )

    audit_record = evaluate_with_audit(
        policy=selected_policy,
        context=ED_ADULT_RESP,
        patient=patient_data
    )

    print(audit_record)
