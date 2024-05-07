from hangmanart import stages,logo
from words import word_list
import random

print(logo)
chosen_word = random.choice(word_list)
end_game = False
lives = 6
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []

for letter in chosen_word:
    display += '_'

while not end_game:
    guess = input('Enter a letter?')
    
    if guess in display:
        print(f'You already guessed {guess}. Kindly guess another letter')
        
    if guess in chosen_word:
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter in guess:
                display[position] = letter
        
        if "_" not in display:
            end_game = True
            print("Great job. You are amazing. You win.")
                
    if guess not in chosen_word:
        lives -=1
        print(f"{stages[lives]}")
        
        if lives == 0:
            end_game = True   
            print("You lose")
        
    print(''.join(display))   


