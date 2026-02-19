import json
from pathlib import Path

DATA_DIR = Path("data")
DATA_FILE = DATA_DIR/"logs.json"

def load_logs():#read existing data
    if not DATA_FILE.exists():
        return{}#if it doest exist return empty dictionary
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)#reads json,  then converts to py dict
    
def save_logs(logs):
    DATA_DIR.mkdir(exist_ok=True)#ensures folder exist
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(logs,file,indent=4)#writes dictionary to json file
        
    
    