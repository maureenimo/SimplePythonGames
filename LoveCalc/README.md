# Love Calculator

## Introduction

The Love Calculator is a program that tests the compatibility between two people by calculating a love score based on the occurrence of specific letters in their names. 

## How It Works

1. Input Names: Enter the names of the two people whose compatibility you want to test.
2. Calculate Love Score:
   - The program checks the number of times the letters in the word "TRUE" occur in both names.
   - It also checks the number of times the letters in the word "LOVE" occur in both names.
   - The program combines these numbers to create a 2-digit love score.
3. Output Messages:
   - For love scores less than 10 or greater than 90, the message will be:
     "Your score is *x*, you go together like coke and mentos."
   - For love scores between 40 and 50, the message will be:
     "Your score is *y*, you are alright together."
   - Otherwise, the message will simply display their love score:
     "Your score is *z*."

## Example

```python
name1 = "Angela Yu"
name2 = "Jack Bauer"

# T occurs 0 times, R occurs 1 time, U occurs 2 times, E occurs 2 times (Total = 5)
# L occurs 1 time, O occurs 0 times, V occurs 0 times, E occurs 2 times (Total = 3)
# Love Score = 53

print("Your score is 53.")
```

## Getting Started

1. Clone the Love Calculator repository to your local machine.
2. Open the main program file.
3. Enter the names of the two people you want to test compatibility for.
4. Run the program to calculate the love score and display the result.

## Contributors
Maureen Murimi - Developer

## Acknowledgments

- Inspired by the concept of love compatibility calculation.

Happy Coding 🚀
