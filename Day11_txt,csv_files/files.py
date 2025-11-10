import os

#r = read                       #c = create
#a = append/update              #r = read
#w = write                      #u = update
#x = create                     #d = delete


#read - error if it doest exist
file = open('names.txt', 'r')# if we dont specifiy r, it automatically read
print(file.read())
print(file.read(4))#will read the forst 4 characters (coll)



print(file.readline())#reads entire fist line of the file only
print(file.readline())#will move to the scond line and read it, a space is left bte line

for line in file:
    print(line)# loops through and prints each line, with space betw each line, just like  readline, but this is more convivient as it reads all the lines. useful if you wanna rrad all the lines.


file.close()#very usefull make sure you close the file.


#error handling
#lets try open a file that does not exist
#we will use try, except, finally

try :
    file = open('names.txt')#we dont have to ,r beecaue its the default in file handling
    print(file.read())

except:
    print('The file you wanna read does not exist')#This way we will get this message if the file doesnt exist

finally:
    file.close()#If the file doesn’t exist, file.close() will cause another error because the file never opened
    #so its better use the convinient method below at the end








#Append- creates a file if it doesnt exist

file = open('names.txt', 'a')#must put the a if you wanna append
file.write('Mandela\n')#\n writes a name(Neil) in a new line.
file.close()

#now lets read after appending to see

file = open('names.txt', 'r')
print(file.read())#notice that when we append we use .write, but when we read we use .read
file.close()







#write - overwrites the  content in a file

file = open('some.txt', 'w')# initially my text contained names of african countries
file.write('All files are deleted')
file.close()

file = open('some.txt', 'r')
print(file.read())
file.close()








# creating a file
# their are two ways 


# 1. creates the file if it does not exist. we use write  'w'

file = open('city.txt', 'w')
file.write('Nairobi')#checks if the file exist, if it does, it overwrites the content, if it does  not it creates the file and input the content.
file.close()



#2. creates a specified file but returns error if it exist
#this means we need to check if it exists first
#fist we import os. we will put at the begining of code, check up

if not os.path.exists('phone_brands.txt'):
    file = open('phone_brands.txt' , 'x')#we use x when creatinga a file
    file.close()




#deleting a file#we can avoid an error if it doest exist

if os.path.exists('phone_brands.txt'):
    os.remove('phone_brands.txt')

else:
    print('The file youre trying to delete does not exist')







#before, or rather above, weve tried handling errors using try, except method
##we dont have to actually, there is a better way to handle errors in file handling

#we use with keyword

with open('more_names.txt') as file:
    content = file.read()

with open('names.txt', 'w') as file:
    file.write(content)# Now understand this   .. we opened our file above and stored in in content variable. and now we are overwritting names.txt and copying the file content from more_names .txt to names.txt


