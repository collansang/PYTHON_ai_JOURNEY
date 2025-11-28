class VitalSigns:
    def __init__(self, hr=None, bp=None, rr=None, temp=None):
        self.heart_rate = hr  # beats per minute
        self.blood_pressure = bp  # mmHg
        self.respiratory_rate = rr  # breaths per minute
        self.temperature = temp  # degrees Celsius
    
class Patient:
    def __init__(self, name, age,):
        self.name = name
        self.age = age
        self.vital = VitalSigns()
        
p= Patient("Collan", 21)
p.vital = VitalSigns(22, 55, "120/80", 37.3)


print(f"name: {p.name}")
print(f"heart rate: : {p.vital.heart_rate}")
print(f"blood_pressure: {p.vital.blood_pressure}")

print()
