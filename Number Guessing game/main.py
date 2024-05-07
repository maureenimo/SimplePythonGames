from art import logo
import random


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

my_number = random.choice(range(0,100))
print(f"Pssst, the correct answer is {my_number}")
difficulty_type = input("Choose a difficulty. Type 'easy' or 'hard': ")

def guess_the_num():
  # checking difficulty type
  if difficulty_type == 'easy':
    attempts = 10
    print(f"You have {attempts} attempts  to guess the number")
  elif difficulty_type == 'hard': 
    attempts = 5
    print(f"You have {attempts}  attempts to guess the number")
  else:
    print("Invalid choice")
    
  while attempts > 0:
    
    guess_num = int(input('Make a guess:  '))
    if guess_num < my_number:
      attempts-=1
      print(f"Too low.\nGuess again.\nYou have {attempts} attempts remaining to guess the number")
    elif guess_num > my_number:
      attempts -=1
      print(f"Too high.\nGuess again.\nYou have {attempts} attempts remaining to guess the number")
    elif guess_num == my_number:
      print(f"You got it! The answer was {my_number}")
      print("Game over")
      break
    else:
      print("Would you like to start over?")
    if attempts == 0:
      print("You've run out of guesses, you lose.")

guess_the_num()