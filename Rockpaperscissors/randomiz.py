import random

# Generates random whole numbers between the range given
print(random.randint(0,100))
# Generates random float numbers
# random() takes no paremetes so if you want to
# generate no btwn 0 -10 (10 isn't included) you can either do: 

# 1) uniform 
method1 = random.uniform(0, 10)
print(method1)

# Method 2 - give you float no btwn 0 - 1(1 excluded) then multiply
method2 = random.random()  * 10 #btwn 0-10
method = random.random()
print(method2)
print(method * 5) #give you btwn 0-5
        
'''You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
Important, the first letter should be capitalised and spelt exactly like in the example e.g. "Heads", not "heads".
There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out "Heads" or "Tails".
e.g. 1 means Heads 0 means Tails'''

number = random.randint(0, 1)

if number == 0:
  print('Tails')
else:
  print('Heads')