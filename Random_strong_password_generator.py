import string
import random

def genrate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

password_lenght = int(input("Enter the length of the password = "))

password = genrate_password(password_lenght)

print("Your Password = ",password)