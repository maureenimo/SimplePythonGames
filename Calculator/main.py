import os 
clear = lambda: os.system('clear')
from art import logo
# add
def add(n1,n2):
  return n1 + n2

# subtract
def subtract(n1,n2):
  return n1 - n2

# divide
def divide(n1,n2):
  return n1 / n2
  
# multiply
def multiply(n1,n2):
  return n1 * n2

def exponent(n1,n2):
  return n1 ** n2
  
# dictionary
operators = {
  "+":add,
  '-': subtract,
  '*': multiply,
  '/': divide,
  '**': exponent
  }
# Inputs
# recursion - function calls itself
def calculator():
  print(logo)
  num1 = float(input('Enter a number? '))

  for key in operators:
    print(key)
  
  arithmetic_calc = False
  # while starts
  while not arithmetic_calc:
      operation_sign = input("Pick an operation: ")
      if operation_sign not in operators:
          print("Invalid operation!")
          continue
          
      next_num = float(input('What is the next number? '))
      fun_calc = operators[operation_sign]
      prev_answer = fun_calc(num1, next_num)
      print(f'{num1} {operation_sign} {next_num} = {prev_answer}')
      
      to_continue = input(f"Type 'y' to continue with {prev_answer}, or type 'c' to start a new calculation or type 'n' to exit: ")
      if to_continue == 'y':
        num1 = prev_answer
      elif to_continue == 'c':
        clear()
        to_continue = False
        calculator()
      elif to_continue == 'n':
        print(f'The answer is {prev_answer}')
        break
      else:
        print('Invalid')
        
calculator()
  