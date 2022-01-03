# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not a leap year")
  else:
    print("Leap year")
else:
  print("Not a leap year")
  
#outline:
#  if year%4==0:
#   if year%100==0:
#     print("Not a leap year")
#     if year%400==0:
#       print("Leap year")
#   print("Leap year")
# else:
#   print("Not leap year")
