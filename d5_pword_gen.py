import random
import random as rd

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t"]
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcom to the PyPassword Gnereator")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols?\n"))
nr_numbers = int(input("How many numbers?\n"))

"""
# nr_letters
password = ""
for char in range(0, nr_letters):
    password += random.choice(letters)

for char in range(0, nr_symbols):
    password += random.choice(symbols)

for char in range(0, nr_numbers):
    password += random.choice(numbers)

print(password)
"""

# nr_letters
password_list = []
for char in range(0, nr_letters):
    password_list += random.choice(letters)

for char in range(0, nr_symbols):
    password_list += random.choice(symbols)

for char in range(0, nr_numbers):
    password_list += random.choice(numbers)

# print(password_list)

random.shuffle(password_list)
# print(password_list)

password = ""

for sym in password_list:
    password += sym

print(f"Your password is: {password}")





