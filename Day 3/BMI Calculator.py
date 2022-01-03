# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI=weight/(height**2)
BMI="{:.0f}".format(BMI)
BMI= int(BMI)
# another way
# BMI= round(weight/(height**2)) -> round to a whole number
if BMI < 18.5:
  print(f"Your BMI is {BMI}, you are  underweight")
elif BMI < 25:
  print(f"Your BMI is {BMI}, you are normal")
elif BMI < 30:
  print(f"Your BMI is {BMI}, you are slightly overweight")
elif BMI < 35:
  print(f"Your BMI is {BMI}, you are obese")
else: 
  print(f"Your BMI is {BMI}, you are clinically obese")
