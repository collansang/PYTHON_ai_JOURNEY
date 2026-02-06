from ast import parse



def parse_lab_from_system_a(raw):
    return{
        "value" : raw["val"],
        "unit" : "mg/dl",
        "collected_at": parse(raw["time"]),
        "source": "SystemA",
        "method":"ponit_of_care",
        "known_limitations":[
            "unit forced to mg/dl",
            "bedside device varability"
        ]
    }
    
def parse_lab_from_system_b(raw):
    return {
        "value": raw["result"],
        "unit": raw["unit"],
        "collected_at": parse(raw["timestamp"]),
        "source": "SystemB",
        "method": "central_lab",
        "known_limitations": [
            "delayed processing",
            "transport artifacts possible"
        ]
    }
    
    
def parse_lab(raw):
    if raw["source"]=="SystemA":
        lab = parse_lab_from_system_a(raw)
    elif raw["source"]=="SystemB":
        lab = parse_lab_from_system_b(raw)
    else:
        raise ValueError("unknown lab source")
    return lab


