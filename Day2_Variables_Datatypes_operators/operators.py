#1. Arithmetic operators: + (add), 
    # -(sub), 
    # *(mult),
    # /(devide), 
    # //(floor devide), 
    # %(modulus), **(exponentiation).

a = 10
b = 4

print('addition', a + b)
print('subtraction', a - b)
print('division', a / b)
print('multiplication', a * b)
print('modulus', a % b)
print('floor division', a //b)
print('exponentiation', a ** b)

#2; comparison/ relational operators:
#  == equal to, != not equal to, > greater than, < less than, 
# >= greater than or equal to, <= less than or equal to

x= 12
y = 9

print('x == y', x == y)
print('x != y', x !=y)
print('x < y', x < y)
print('x >= y', x >= y)
print('x < y', x < y)
print('x <= y', x <= y)

#3; logical operators: used to combine multiple conditions
#and (if both conditions are true),
# , or( if one condition is true)
#  , not(REVERSES TRUE/FALSE VALUE)


c = 10
d = 7
e = 5

print('c > d and d > e', c > d and d > e)
print ('d < c or e > c',d < c or e > c)
print('not(c > d)', not(c > d))


#4 asignment operators:
# =, +=, -=, *=, /=, %=, //=, **=
f = 22
g = 5

f += g #f = f + g
f -= g # f = f - g
f *= g #f = f * g

f /= g # f = f / g
print('after /= ', f)

f %= g #f = f % g
print('after %= ', f) 

f = 22
g = 5
f ** g # f = f // g
print('after ** ', f)

f //= g # f = f // g
print('after //=', f )

f **= g # f = f ** g
print('after **', f)


#5: string operators
# + joins the string (concatenation)
# * repeats the string
fname =  'Collan'
lname = 'Sang'
welcome = 'welcome to Python + AI programming sessions'

print('Good Morning ' + fname +' ' + lname + ' '  + welcome)
print((fname + lname) * 7)