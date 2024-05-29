import string
import random

password = input("Enter Your Password (Only Numbers): ")

char = string.digits  # Use only digits (numbers 0-9) for the cha

while True:
    var = random.choices(char, k=len(password))
    print(">>>>", ''.join(var), "<<<<<")
    ps = ''.join(var)
    if password == ps:
        print("Your Password is:", ps)
        break
