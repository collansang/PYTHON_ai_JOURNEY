class PatintRepository:
    def __init__(self):
        self._data = {}
        
    def add(self, patient):
        self._data.append(patient)
        
    def get_by_id(self, pid):
        return self._data.get(pid)
    
    def list_all(self):
        return list(self.data)
    