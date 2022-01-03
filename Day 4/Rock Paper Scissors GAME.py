rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

print("Welcome to Rock Paper Scissors GAME")

your_choice= input("What number do you choose: 0 for Rock, 1 for Paper, or 2 for Scissors? Your choice is: ")

#I did not use int(input()) because the program will not work when someone input float number or letter!
#I did not use 0,1,2 comparison because I wanted to be have a general code that could work for different rules.

computer_list= [rock,paper,scissors]
import random
computer_choice=random.choice(computer_list)
index_computer_choice=computer_list.index(computer_choice)

if your_choice== "0" or your_choice== "1" or your_choice== "2":
 
  print("Wow. You have")
  #Another way:
  # if your_choice== "0":
  #   print(rock)
  # elif your_choice== "1":
  #   print(paper)
  # elif your_choice== "2":
  #   print(scissors)
  print(computer_list[int(your_choice)])

  print("The computer plays")
  print(computer_choice)

    
  if index_computer_choice== int(your_choice):
    print("Draw!")
  else:
    if your_choice == "0" and computer_choice==paper:
      print("You lose!")
    elif your_choice == "1" and computer_choice==scissors:
      print("You lose!")
    elif your_choice == "2" and computer_choice==rock:
      print("You lose!")
    else:
      print("You win!")
else: 
  print("Please input a valid number 1, 2, or 3!")


print("Thank you for playing this game!")


# print(index_computer_choice)

#note: computer_choice can be rock, paper, or scissors => compare with rock, paper, and scissors variables
