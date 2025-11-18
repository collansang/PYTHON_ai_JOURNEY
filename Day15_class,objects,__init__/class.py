#class = (blue print) allows us to logically group our data and functions in a way thats easy to reuse or rebuild (design structure and layout)
#object = bundle of related attributes(variables) and methods(functions)
#you need a clss to define many methods

class Patient:
    month = "December" #class variable share by all petients in Patient class.
    #pass#it will pass and not raise errors
    def __init__(self, f_name, l_name, weight, height,  temperature,):#This is a method (constructor)(dunder method) within a class and recieves instance as the first argument automatically calling it self, after here youn can specify what other arguments you want it to accept.  here (f_name, l_name, temperature)
        self.f_name = f_name
        self.l_name = l_name
        self.weight = weight
        self.height = height
        self.temperature = temperature
        self.email = f_name + '.' + l_name + '@company.com'
        
    def fullname(self):#method()
        return f"{self.f_name} {self.l_name}"
        
    def bmi(self):#method. action that class can perform
        #self.pay = temperature
        bmi1 = float(self.weight / (self.height **2))
        print(bmi1)

pat1 = Patient('Collan', 'Sang' , 49.95, 1.2, 37.4)
pat2 = Patient('Amos', 'Wangila', 57, 1.5, 39)#this 2 are instances(objects) in the class employee
#instance variables
#contains data thats unique(identical) for each instance ( in this case its unique to each employee)emp_1

print(Patient.month)
print()
print(pat1.fullname())
print(pat1.temperature)
print(pat1.bmi())
print()
print(pat2.fullname())
print(pat2.temperature)
print(pat2.bmi())


