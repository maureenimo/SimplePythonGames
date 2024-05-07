# You are going to write a program that will mark a spot on a map with an X.
# Your job is to write a program that allows you to mark a square on the map using a letter-number system.

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?

# Finding the position based on input
letter = position[0].lower()
number = int(position[1])

# Find the letter
letters = ['a', 'b', 'c']
letter_spot = letters.index(letter)

# mark spot x
map[number-1][letter_spot] = 'X' 
print(f"{line1}\n{line2}\n{line3}")