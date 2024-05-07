print("The Love Calculator is calculating your score...")
name1 = input("What is your name?")  
name2 = input("What is their name?") #\ 
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
both_names = (name1 + name2).lower()

f_word = 'true'
l_word = "love"

love_count = 0
true_count = 0

for word in both_names:
  if word in f_word:
    true_count +=1

for words in both_names:
  if words in l_word:
    love_count +=1

love_score = int(str(true_count) + str(love_count))

if love_score<10 or love_score >90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >=40 and love_score <=50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
    