sum=0
average=0
number_of_students=0

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
  sum+=student_heights[n]
  number_of_students += 1


average = sum/number_of_students
print(round(average))

#this code requires that no len() or sum() will be used
#total=sum(student_heights)
#number=len(student_heights)
#Another way: using for loop twice
