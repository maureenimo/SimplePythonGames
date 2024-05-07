# Tip calculator
print("Welcome to the tip calculator.")
total_bill = float(input('What was the total bill? $'))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
billed_tip = total_bill * (1 + tip_percentage/100)
noOfPeople = int(input('How many people to split the bill? '))
# calculation
to_pay = billed_tip/noOfPeople 
# Rounding it off
topay_rounded = f"{to_pay:.2f}"
print(f"Each person should pay : ${topay_rounded}")


# # Bonus
print("Welcome to the tip calculator!")
bill = float(input('What was the total bill? $'))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
noOfPeople = int(input('How many people are to split the bill? '))
topay = bill/noOfPeople
totip = (bill * (tip /100)/noOfPeople)

total_amount = topay + totip
# Format 
total_amount_formatted = format(total_amount, '.2f')
print(f"Everyone's share of the total bill is ${topay} plus a ${totip} tip. The total comes to ${total_amount_formatted}")

# Read on https://docs.python.org/3/tutorial/floatingpoint.html - float zero