from art import logo
import os
print(logo)
print("Welcome to the secret auction program.")

clear = lambda: os.system('clear')
auctioneers = {}

name = input("What is your name? ")
bid = int(input("What is your bid? $"))
auctioneers[name] = bid
    
other_bidders= input("Are there any other bidders? Type 'yes' or 'no'. ")
    
while other_bidders == 'yes':
    clear()
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    auctioneers[name] = bid
    other_bidders= input("Are there any other bidders? Type 'yes' or 'no'. ")
  
    max_bidder_name = max(auctioneers, key=auctioneers.get)
    max_bidder_value = auctioneers[max_bidder_name]

    print(f"The highest bidder is: {max_bidder_name}, with a bid of: {max_bidder_value}.")

else:
    highest_bid = max(auctioneers, key= auctioneers.get)
    highest_value = auctioneers[highest_bid]
    print(f'The highest bid is {highest_bid} who bid {highest_value}')
