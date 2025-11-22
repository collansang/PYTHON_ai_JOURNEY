

class Book:
    def __init__(self, author, book, pages):
        self.author = author
        self.book = book
        self.pages = pages
    
    def __str__(self):#with this dunder we customize printing data. like below we just need to call name of book without necessarily calling the class. makes works easier  print(book1)
            return f"{self.book} by {self.author}"
        
        
    def __eq__(self, value):#this helps us to equate ie we see below if the books are equal. compare
        return self.author == value.author and self.book == value.book
    
    def __lt__(self, value):#less than
        return self.pages < value.pages
        
         
          
book1 = Book("Carl newport", "Deepwork", 192) 
book2 = Book("Anders Ericsson", "Peak", 310)
book6 = Book("Anders Ericsson", "Peak", 310)
book3 = Book("Robert greene" ,"The daily laws", 461)   
book4 = Book("Robert greene" ,"48 laws of power", 460)   
book5 = Book("collan sang" ,"win today", 192)   

print(book1)
print(book2)
print(book3)
print(book4)
print(book5)
print(book2 == book6)#True

print(book5<book4)#True













# class Done:
#     name = "Jenny"
# d = Done()
# print(d)