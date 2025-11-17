#class = allows us to logically group our data and functions in a way thats easy to reuse or rebuild

class employee:
    raise_amt = 1.04
    #pass#it will pass and not raise errors
    def __init__(self, f_name, l_name, temperature):#This is a method within a class and recieves instance as the first argument automatically calling it self, after here youn can specify what other arguments you want it to acceptn here (first, last)
        self.f_name = f_name
        self.l_name = l_name
        self.temperature = temperature
        self.email = f_name + '.' + l_name + '@company.com'
        
    def fullname(self):
        return f"{format(self.f_name)} {format(self.l_name)}"
    
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


emp_1 = employee('Collan', 'Sang' , 37.4)
emp_2 = employee('Amos', 'Wangila', 39)#this 2 are instances(objects) in the class employee
#instance variables
#contains data thats unique for each instance ( in this case its unique to each employee)

print(emp_1.fullname())
print(emp_1.raise_amt())



