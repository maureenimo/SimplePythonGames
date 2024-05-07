from art import logo
import random
import os

input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
print(logo)

clear = lambda: os.system('clear')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer = random.sample(cards, 2)
user = random.sample(cards, 2)

def blackjack():
    user_score = sum(user)
    computer_score = sum(computer)

    print(f"Your cards: {user}, current score: {user_score}")
    print(f"Computer's first card: {computer[0]}")

    while user_score < 21:
        answer = input("Type 'y' to get another card, type 'n' to pass: ")
        if answer == 'y':
            user.append(random.choice(cards))
            user_score = sum(user)
            print(f"Your cards: {user}, current score: {user_score}")
        elif answer == 'n':
            break

    while computer_score < 17:
        computer.append(random.choice(cards))
        computer_score = sum(computer)

    print(f"Your final hand: {user}, final score: {user_score}")
    print(f"Computer's final hand: {computer}, final score: {computer_score}")

    if user_score > 21:
        print("You went over. You lose.")
    elif computer_score > 21 or user_score > computer_score:
        print("You win!")
    elif user_score < computer_score:
        print("You lose!")
    else:
        print("It's a draw!")

    restart = input("Would you like to play again? Type 'y' for yes and 'n' for no: ")
    if restart == 'y':
        clear()
        blackjack()

blackjack()
