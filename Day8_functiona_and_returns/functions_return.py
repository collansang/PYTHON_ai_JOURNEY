#a functtion is a block of code that performa a specific task
#you define it and call it whenever you need it.

def greet():
    print('Good Morning Sir. Welcome to my programme')

greet()


#return: send back a result

def add(x, y):
    return x + y

result = add(4, 8)
print(result)


#combination and complex

def info(name, age, place):
    message = f'Good morning {name}. You are {age} years old, and you stay at {place}'
    return message
print(info('Collan', '21', 'Kutus'))