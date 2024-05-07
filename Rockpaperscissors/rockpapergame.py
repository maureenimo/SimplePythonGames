import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print('Welcome to Rock paper scissors.')
# this input is coming in string form
# How you will store the user's input.
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
# How you will generate a random choice for the computer.
computer_choice = str(random.randint(0, 2))

# Make a list of the images
game_images = [rock, paper, scissors]

# Print the choices - typecasting
print(f"You choice: {game_images[int(user_choice)]}")
print(f"The computer's choice: {game_images[int(computer_choice)]}")

# How you will compare the user's and the computer's choice to determine the winner (or a draw).
# And also how you will give feedback to the player.
# guidelines = rock > scissors > paper > rock

if user_choice not in ['0', '1', '2'] :
    print('Invalid choice. Try again.')
elif int(user_choice) == 0 and int(computer_choice)== 2:
    print("You won.")
elif int(computer_choice) == 0 and int(user_choice) == 2:
    print("You lost.Better luck next time.")
elif int(user_choice) == int(computer_choice):
    print("It's a tie. Play another round.")
elif user_choice > computer_choice:
    print("Way to go. You won. ")
else:
    print('You lose')