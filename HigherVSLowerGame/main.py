import os
from art import logo, vs
from game_data import data
import random

print(logo)
print("Who has more followers?\nA frustratingly addictive game of higher or lower using instragram followers.")

clear = lambda: os.system('clear')

# checking values
count = 0
for item in data:
  follower_count = item["follower_count"]
  if follower_count > count:
    count = follower_count
  
def play():
  game_over = False
  score = 0
  profile1, profile2 = random.sample(data, 2)
  while not game_over:
    
    print(f"Compare A:{profile1['name']} a {profile1['description']} from {profile1['country']}")
    print(vs)
    print(f"Against B:{profile2['name']} a {profile2['description']} from {profile2['country']}")
    choose = input("Who has more followers. Type 'A' or 'B': ").upper()
  
    if choose == 'A' and profile1['follower_count'] >  profile2['follower_count'] or choose == 'B' and profile2['follower_count'] > profile1['follower_count']:
      score += 1
      print(f"You have {score} point")
      if choose == "A":
        profile2 = random.choice(data)
      else:
        profile1 = profile2
        profile2 = random.choice(data)
      continue
    else:
      game_over = True
    standard_score = 5
  
    if score == 0:
      print(f"You scored:{score}\nThat‘s a terrible score.\nThe average score is {standard_score}. Put some effort into it :)")
    elif score == 1 or score == 2:
      print(f"You scored:{score} \nDid we make this too hard for you?\nThe average score is {standard_score}.\nWe‘re pretty embarrassed for you right now.")
    elif score >= 3 and score < standard_score:
      print(f"You scored:{score}. \nOh dear!!! That’s an embarrassing score isn’t it?\nThe average score is {standard_score}\nLet‘s pretend that never happened!")
    elif score >= standard_score and score <= 10:
      print("You scored:{score}.\nGood effort!\nKeep trying...")
    elif score > 10:
      print(f"You scored:{score}. \n90% of people who play this score less than you! \nWe’re impressed!.")
      
    # play again
    play_again = input("Do you want to play again. Type 'y' to play again or 'n' to go back to the menu.")
  
    if play_again == 'n':
      game_over = True
      print("Bye.See you next time")
  
    
    else:
        clear()
        play()
        
play()