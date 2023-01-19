import string
import random

def generatePassword(num):
    letters = string.printable
    password = []

    while len(password) < num:
        password.append(random.choice(letters))
    newPass = ''.join(str(x) for x in password)
    print(newPass)
    print(password)

generatePassword(9)