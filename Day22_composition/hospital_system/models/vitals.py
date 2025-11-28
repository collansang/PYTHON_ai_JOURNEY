class VitalSigns:
    def __init__(self, hr=None, bp=None, rr=None, temp=None):
        """Initialize vital signs for a patient."""
        self.__heart_rate = None
        self.__blood_pressure = None
        self.__respiratory_rate = None
        self.__temperature = None
        
        self.heart_rate = hr  # beats per minute
        self.blood_pressure = bp  # mmHg
        self.respiratory_rate = rr  # breaths per minute
        self.temperature = temp  # degrees Celsius
    
    @property
    def heart_rate(self):
        return self.__heart_rate
    
    @heart_rate.setter
    def heart_rate(self, value):
        if value is not None and not (20< value <200):
            raise ValueError("Heart rate must be between 20 and 200 bpm")
        self.__heart_rate = value
        
        
    @property
    def blood_preassure(self):
        return self.__blood_preassure
    
    @blood_pressure.setter
    def blood_pressure(self, value):    
        if value is not None:
            systolic, diastolic = map(int, value.split('/'))
            if not (50 < systolic < 250) or not (30 < diastolic < 150):
                raise ValueError("Blood pressure values are out of realistic range")
        self.__blood_pressure = value
    
    @property
    def respiratory_rate(self):
        return self.__respiratory_rate
    @respiratory_rate.setter
    def respiratory_rate(self, value):
        if value is not None and not (5 < value < 60):
            raise ValueError("Respiratory rate must be between 5 and 60 breaths per minute")
        self.__respiratory_rate = value
        
    @property
    def temperature(self):
        return self.__temperature
    
    @temperature.setter
    def temperature(self, value):
        if value is not None and not (30.0 < value < 45.0):
            raise ValueError("Temperature must be between 30.0 and 45.0 degrees Celsius")
        self.__temperature = value
        
        