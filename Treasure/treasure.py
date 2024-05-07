# This part is from ASCII art - https://ascii.co.uk/art
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.__" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.__o;   |
|___________________|_| ;     (#) `-.o `"=.`_.__"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.__"    ;o;____/______/______/____
/______/______/______/_"=._o__._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o__._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.__"o.__"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.__""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
# End of ASCI ART

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
print("You're at a crossroad. Where do you want to go?")
# Choices begin
answer = input('Type "left" or "right" ').lower()
if answer == 'left':
    print("You've come to a lake. There is an island in the middle of the lake.")
    ans= input('''Type "wait" to wait for a boat. Type "swim" to swim across. ''')
    if ans == 'wait':
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.")
        color = input('''Which colour do you choose? ''')
        # color of the door
        if color == 'yellow':
            print("You found the treasure! You Win!")
        elif color == 'red':
            print("It's a room full of fire. Game Over.")
        elif color == 'blue':
            print("You entered a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    # swim or anything else
    else:
        print("You get attacked by an angry trout. Game Over.")

# if right or anything else
else: 
    print("Oops you have just fallen into a hole. Game over.")


