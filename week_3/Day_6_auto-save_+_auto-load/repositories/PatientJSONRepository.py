from repositories.PatientRepository import PatientRepository
import json
import os
import threading
import time

class PatientJSONRepository(PatientRepository):
    def __init__(self, file_path, autosave_interval=5):
        self.file_path = file_path
        self.patients= {}
        self._dirty = False
        
        self.load()
        self.autosave_interval = autosave_interval
        
    def load(self):
        if not os.path.exists(self.file_path):
            return
        with open(self.file_path, "r") as file:
            data = json.load(file)
            self.patients = data
    
    def add(self, patient):
        self.patients[patient.pid] = patient.to_dict()
        self._dirty = True
    
    def get_by_id(self,pid):
        return self.patients.get(pid)
    
    def list_all(self):
        return list(self.patients.values())
    
    
    def _start_autosave_loop(self, interval):
        def loop():#nested for background work forever
            while True:#Never ending loop
                time.sleep(interval)#wait interval seconds
                if self._dirty:#gatekeeper- only save if something changes(dirty)
                    self._save()#data at risk secure it
        thread = threading.thread(target = loop, deamon= True)#guard  target=loop is the job daemon=True means thread dies when app dies
        thread.start()#begin watching now
        
    def _save(self):
        tmp_file = self.file_path + ".tmp"#creates a temporary file. Never write directly to the main file
        with open(tmp_file, "w") as file:#write new data to temp file
            json.dump(self.patients, file, indent=4)#freeze data into json format(readable)
        os.replace(tmp_file, self.file_path)#swap temp file with main file atomically
        self._dirty =False#data safe now not dirty anymore, reset flag