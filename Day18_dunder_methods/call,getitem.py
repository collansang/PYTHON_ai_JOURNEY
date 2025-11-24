class Patients:
    def __call__(self, height, weight):
        return self.weight / (height **2)



patients= [
    patient(heght = 1.2, weight = 50)
]        