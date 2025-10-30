#Data types
#1. Numbers: Integers(stores whole numbers), floats(decimals) and 
# complex numbers(numbers with imaginary parts like letters)

a = 10 #integer
b = 10.5 #float
c = 12j #complex

print(a, type(a))
print(b, type(b))
print(c, type(c))


#2. strings str (store text, double or single quotes)
greetings = 'Hello Sir'
name = "Collan"
place = 'Keru'
print(greetings, type(greetings))
print(name, type(name))
print(place, type(place))


#3. boolean bool (True or False)
with_purpose = True
is_tired = False
Is_serious = True

print(with_purpose, type(with_purpose))
print(is_tired, type(is_tired))
print(Is_serious, type(Is_serious))

#4. Nonetypes (None)
is_happy = None

print(is_happy, type(is_happy))



#5conversions between data types
d = str(10) #10 an interger is converted to string
e = float(5) #5 an integer is converted to float
f = int(1.2) # a float is converted to integer
print(int('100') + 35) #100 is converted to an interger beforer adding to 35

print(d, type(d))
print(e, type(e))
print(f, type(f))


x = 10
y = 4.14
z = 'Day 2 of learning python'
Is_short = True 

print(x, type(x))
print(y, type(y))
print(z, type(z))
print(Is_short, type(Is_short))