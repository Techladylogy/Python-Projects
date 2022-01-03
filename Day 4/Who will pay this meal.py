# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
number_of_people=len(names) - 1 
random_number=random.randint(0,number_of_people)
chosen_person= names[random_number]
print(f"{chosen_person} is going to buy the meal today!")

#better way: random.choice(names)
