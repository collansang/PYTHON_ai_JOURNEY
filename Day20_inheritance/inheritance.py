#to understand inheritance lets use this case scenario
#to study, or enjoy myself my laptop must be on , charged and have necessary application. so studying and enjoyment can inherit from laptop

class Laptop:
    
    def on(self):
        print("This Laptop is on, ready to use")
       
    
    def charged(self):
        print("The laptop is fully charged.")
        
    def app(self):
        print("I have all the necessary application")
        
    
class Study(Laptop):
    def coding(self):
        print("I am ready to code.")
        
    def cli_med(self):
        print("Start studying clinical medicine")
        
    def pd(self):
        print("You can start on your personal development")
        
    
class Enjoyment(Laptop):
    def music(self):
        print("You mant some music !! sure start with Assinata")
    
    def story(self):
        print("You can now listen stories online for fun")
       
    def shows(self):
        print("Its now time for ome shows")
        
studying = Study()
enjoyment = Enjoyment()

studying.on()#inherited from laptop on attribute
studying.app()
studying.charged()
print()

studying.coding()
studying.cli_med()
studying.pd()
print()

enjoyment.on()
enjoyment.charged()
enjoyment.app()
print()

enjoyment.music()
enjoyment.story()
enjoyment.shows()
        
    