# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total_day = 365*90
total_week= 52*90
total_month= 12*90

age= int(age)

age_day= age*365
age_week= age*52
age_month= age*12

day_left= total_day - age_day
month_left= total_month - age_month
week_left= total_week - age_week

print(f"You have {day_left} days, {week_left} weeks,and {month_left} months left")

 
#Another way age_left = 90 - age => work with age_left
