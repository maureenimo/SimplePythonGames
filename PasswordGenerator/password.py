import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Python Password Generator!")
letter_choice = int(input("How many letters would you like in your password?\n"))
symbol_choice = int(input("How many symbols would you like?\n"))
number_choice = int(input("How many numbers would you like in your password?\n"))

# Easy level
# my_pass = ""
# for letter in range(0, letter_choice):
#     letts = random.choice(letters)
#     my_pass += letts
    
# for num in range(1, number_choice + 1):
#     nums = random.choice(numbers)
#     my_pass += nums
    

# for _ in range(1, symbol_choice + 1):
#     sy = random.choice(symbols)
#     my_pass += sy

# print(f"Password is {my_pass}")
    
# Hard level
myPass= []
for _ in range(symbol_choice):
    symbols_pass = random.choice(symbols)
    myPass.append(symbols_pass)
    
for _ in range(number_choice):
    number_pass = random.choice(numbers)
    myPass.append(number_pass)
    
for _ in range(letter_choice):
    letter_pass = random.choice(letters)
    myPass.append(letter_pass)

random.shuffle(myPass)
password = ''.join(myPass)
print(f"Here is your password:{password}")
