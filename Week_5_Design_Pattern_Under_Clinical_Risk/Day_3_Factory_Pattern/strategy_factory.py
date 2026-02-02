"""
strategy_factory.py

Factory Pattern — Bias Injection Audit

Design rules:
- NO implicit conditionals (no if/elif ladders deciding policy)
- ALL selection logic must be data, not code
- Strategy choice must be explainable, traceable, and loggable
"""
from dataclasses import dataclass
from typing import Tuple, Dict, Type

class ClinicalStrategy:
    def aname(self) -> str:
        raise NotImplementedError
    def criteria(self) -> Dict:
        raise NotImplementedError
    def assumptions(self) -> list:
        raise  NotImplementedError
    def risk_profile(self) -> str:
        raise NotImplementedError
    
class AdultWard2023Strategy(ClinicalStrategy):
    def name(self):
        return "AdultWard2023"
    def criteria(self):
        return{
            "age_range": ">=18",
            "unit": "ward",
            "policy_year": 2023
        }
        def assumptions(self):
            return[
                "Adult physiology applies",
                "starndard ward monitoring available",
                "2023 national guidelines followed"
            ]
    def risk_profile(self):
        return "Moderate - escalation depend on nursing detection"
    
class PediatricWard2023Strategy(ClinicalStrategy):
    def aname(self) :
        return "PediatricWard2023"
    def criteria(self):
        return {
            "age_range": "<18",
            "unit": "ward",
            "policy_year": 2023
        }
    def assumptions(self):
        return [
            "Pediatric physiology applies"
            "Weight_based risk"
            "Higher variability"
            
        ]
    def risk_profile(self):
        return "High - Deterioration can be rapid"

class ICUAnyage2023Strategy(ClinicalStrategy):
    def name(self):
        return"ICUAnyAge@023"
    def criteria(self):
        return {
            "age_range": "any",
            "unot": "ICU",
            "policy_year": 2023
        }
    def assumptions(self):
        return[
            "Continuos monitoring available",
            "Immediate intervention available"
        ]
        
STRATEGY_MAP:Dict[Tuple[str,str,int], Type[ClinicalStrategy]] = {
    ("adult", "ward", 2023): AdultWard2023Strategy,
    ("pediatric", "ward", 2023): PediatricWard2023Strategy,
    ("any", "ICU", 2023): ICUAnyage2023Strategy}

@dataclass
class StrategySelectionLog:
    input_context: Dict
    lookup_key:Tuple
    selected_strategy:str

@dataclass
class StrategyFactory:
    def __init__(self, mapping_table= STRATEGY_MAP):
        self.mapping_table = mapping_table
        
    def select(self, *, age:int, unit:str, policy_year:int):
        age_group= self._age_to_group(age)
        lookup_key=(age_group, unit, policy_year)
        if lookup_key not in self.mapping_table:
            raise ValueError(f"No strategy for criteria: {lookup_key}")
        strategy_cls= self.mapping_table[lookup_key]
        return strategy_cls()
        
        log = StrategySelectionLog(
            input_context={
                "age": age,
                "unit": unit,
                "policy_year": policy_year
            },
            lookup_key=lookup_key,
            selected_strategy=strategy.name()
        )

        return strategy, log
    @staticmethod
    def _age_to_group(age:int) -> str:
        if age < 18:
            return "pediatric"
        return "adult"
    
        