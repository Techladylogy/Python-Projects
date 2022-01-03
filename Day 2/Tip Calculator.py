#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
bill= float(input("What was the total bill? $"))
tip= int(input("How much tip would you like to give? 10, 12, or 15? "))

#Another way:
# if tip== 10:
#   tip = bill*0.1
#   bill+= tip
# elif tip== 12:
#   tip = bill*0.12
#   bill +=tip
# elif tip==15:
#   tip = bill*0.15
#   bill += tip
# else:
#   print("Please input a valid number")

tip= bill*(tip/100)
bill += tip

people_number= int(input("How many people to split the bill? "))

split_bill= round(bill/(people_number),2)
split_bill= "{:.2f}".format(split_bill)
print(f"Each person should pay ${split_bill}")

