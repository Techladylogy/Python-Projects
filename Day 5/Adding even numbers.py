#Write your code below this row 👇
#the sum of all the even numbers from 1 to 100 including 100

sum=0
for i in range(2,102,2):
  #start with 2 and add 2 every time until 100, 102 is not included. if the end number is 101 is fine because it is not included as well. This means [2,102) in math.
  sum+=i
  # print(i)
print(sum)

#Another way
sum1=0
for e in range(1,101):
  if e%2 ==0:
    sum1+=e
print(sum1)
