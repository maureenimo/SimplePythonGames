# Blackjack Project

## Our Blackjack House Rules
- The deck is unlimited in size.
- There are no jokers.
- The Jack/Queen/King all count as 10.
- The Ace can count as 11 or 1.
- Use the following list as the deck of cards: `cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]`
- The cards in the list have equal probability of being drawn.
- Cards are not removed from the deck as they are drawn.
- The computer is the dealer.

### Hints
- Hint 1: Visit [this website](https://games.washingtonpost.com/games/blackjack/) and try out the Blackjack game.
- Hint 2: Read the [program requirements breakdown](http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF) and create a flowchart for the program.
- Hint 3: Download and study the [flowchart](https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt) provided.

### Getting Started
To get started with the Blackjack project, follow these steps:

1. Create a `deal_card()` function that returns a random card from the deck.
2. Deal two cards each to the user and the computer using `deal_card()` and append them to their respective lists (`user_cards` and `computer_cards`).
3. Create a `calculate_score()` function that calculates the score of a given hand.
   - Check for a blackjack (ace + 10) and return 0 if found.
   - Check for an ace (11) and replace it with 1 if the score is over 21.
4. Call `calculate_score()` to check for blackjack or bust. If found, end the game.
5. Ask the user if they want to draw another card. If yes, deal another card and re-calculate the score.
6. If the user stands (doesn't draw more cards), let the computer play by drawing cards until its score is at least 17.
7. Compare the final scores of the user and the computer to determine the winner.

### Additional Notes
- The game should provide options for the user to restart after each round.
- Use the provided hints and flowchart to guide you through the implementation process.

Feel free to reach out if you have any questions or need further assistance. Enjoy coding! 🚀