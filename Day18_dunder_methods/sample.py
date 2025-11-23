class Patient:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def __repr__(self):
        return (f"Patient(name={self.name!r}, "
                f"age={self.age!r}, "
                f"weight={self.weight!r})")


# ---- Broken dataset on purpose ----
patients = [
    Patient("Alex", 30, 70),
    Patient("Mary", None, 55),        # BUG: age is None
    Patient("John", "forty", 90),     # BUG: age is a string
    Patient("", 22, 55),              # BUG: empty name
    Patient("Sam", 25, -10),          # BUG: invalid negative weight
]


print("Patients before sorting:")
print(patients)


print("\nTrying to sort by age...")
sorted_patients = sorted(patients, key=lambda p: p.age)  # <---- CRASHES HERE
print(sorted_patients)
