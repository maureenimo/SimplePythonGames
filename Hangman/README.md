
# Hangman Game

## Introduction

Hangman is a classic word-guessing game where players try to guess a hidden word by suggesting letters within a limited number of attempts. 

## How to Play

1. Start the Hangman game by running the main game script.
2. The game will randomly select a word from a predefined list of words. This word is the "chosen word" that the player needs to guess.
3. The player's objective is to guess the chosen word by suggesting letters.
4. For each letter in the chosen word, an underscore ('_') is displayed initially in the "display" to represent hidden letters.
5. The player enters a letter guess.
6. If the guessed letter matches any letter in the chosen word, those letters are revealed in the display at their respective positions.
   - Example: If the chosen word is "apple" and the player guesses "p", the display will show ["_", "p", "p", "_", "_"].
7. If the guessed letter is not in the chosen word, the player loses a life.
8. The game continues until the player correctly guesses the word or runs out of lives.

## Game Mechanics

- The game uses a predefined list of words as the pool of words to choose from.
- The player has a limited number of lives, typically represented as "hangman" body parts (e.g., head, body, arms, legs).
- Each incorrect guess results in the display of additional hangman body parts until the player runs out of lives (loses) or correctly guesses the word (wins).

## Getting Started

1. Clone the Hangman repository to your local machine.
2. Navigate to the project directory.
3. Run the main game script to start playing.

## Dependencies

- Python 3.x

## Contributors

Maureen Murimi - Developer

## Acknowledgments

- Inspired by the classic Hangman game.

Happy Coding 🚀


