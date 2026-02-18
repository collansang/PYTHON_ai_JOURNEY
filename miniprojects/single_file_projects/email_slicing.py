email = input("enter your email: ")

index = email.index("@")

user_name = email[:index]
domain = email[index + 1:]

print("Your username is: ", user_name)
print("Your domain is: ", domain)
