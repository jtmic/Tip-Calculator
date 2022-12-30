#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the tip calculator")
#Each person should pay (150.00 / 5) * 1.12 = 33.6
bill = float(input("What was the total bill? $"))
Tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))
#Format the result to 2 decimal places = 33.60
bill_with_tip = Tip / 100 * bill + bill

tip_as_percent = Tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay $ {final_amount} ")


#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇