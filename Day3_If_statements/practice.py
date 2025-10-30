# #input and output practice
name = input('What is your name?')
age= input('How old are you?')

print('Hello, ' + name  + '!You are ' + age + ' years old.')

#type casting/ conversion 
word1 = input('Enter your first fav no: ')
word2 = input('Enter your sec fav no: ')

sum = int(word1) + int(word2)

print('Your fav numbers sum is ' + str (sum))

# f strings
fname = input('Enter your first name: ')
sname = input('Enter your second name: ')

print(f'Hello, {fname} {sname}!. Welcome on board.')
