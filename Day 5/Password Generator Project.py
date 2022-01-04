#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
letter_list=[]
for i in range(0, nr_letters):
  chosen_letter=random.choice(letters)
  letter_list.append(chosen_letter) 
# print(*letter_list,sep = "")

number_list=[]
for n in range(nr_numbers):
  chosen_number=random.choice(numbers)
  number_list.append(chosen_number)
# print(*number_list,sep="")

symbol_list=[]
for e in range(nr_symbols):
  chosen_symbol=random.choice(symbols)
  symbol_list.append(chosen_symbol)
# print(*symbol_list,sep="")

final_list= letter_list + symbol_list + number_list #merging lists
print("Your password number one is: ")
print(*final_list, sep="")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random.shuffle(final_list)
print("Your password number two is: ")
print(*final_list, sep="")
