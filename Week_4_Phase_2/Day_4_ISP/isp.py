class TemperatureReader:
    def read(self) ->float:
        return 36.0
    
class FeverChecker:
    def has_fever(self, temperature: float) ->bool:
        return temperature >38
    
class MedicationGiver:
    def give(self, has_fever: bool)->str:
        if has_fever:
            return "Administering Medication"
        else:
            return "No medication needed"
        
reader = TemperatureReader()
checker = FeverChecker()
giver = MedicationGiver()

temp = reader.read()
fever  = checker.has_fever(temp)
result = giver.give(fever)
print(result)