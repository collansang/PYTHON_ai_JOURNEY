# substituition cypher encryption programme

import random
import string

chars = " " + string.punctuation+string.digits+string.ascii_letters#original flow of characters
chars_list = list(chars)#copy to be reshuffled
random_chars = chars_list.copy()
random.shuffle(random_chars)

random_chars = ''.join(random_chars)#shuffled flow of characters


#encrypt
def encrypt(message):
    encrypted_message = ""
    for letter in message:
        index = chars.index(letter)
        encrypted_message += random_chars[index]
    return encrypted_message

#decrypt
def decrypt(encrypted_message):
    decrypted_message = ""
    for letter in encrypted_message:
        index = random_chars.index(letter)
        decrypted_message += chars[index]
    return decrypted_message

# Example usage
message = "Hello, My name is Nobody 123"
encrypted = encrypt(message)
print("-------------------------------------")

print(f"Original message: {message}")
print(f"encrypted message: {encrypted}")
print("-------------------------------------")


decrypted = decrypt(encrypted)
print("-------------------------------------")
print(f"encrypted message: {encrypted}")
print(f"decrypted message: {decrypted}")   
print("-------------------------------------")
