#Write your code below this row 👇

#Your program should print each number from 1 to 100 in turn.When the number is divisible by 3 then instead of printing the number it should print "Fizz". When the number is divisible by 5, then instead of printing the number it should print "Buzz". When the number is divisible by 5, then instead of printing the number it should print "Buzz". And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"


for i in range (1,101):
  #my logic: a number should be checked for %3==0 and %5 ==0 before going to the next two conditions because if that number is checked for %3 or %5 first, if statement will skip %3 and %5 ==0 condition due to the previous statisfaction of if statement. 
  if i%3==0 and i%5==0:
    print("FizzBuzz")
  elif i%3==0:
    print("Fizz")
  elif i%5==0:
    print("Buzz")
  else:
    print(i)
