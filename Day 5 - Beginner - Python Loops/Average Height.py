# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total = 0
students = 0

for i in student_heights:
  total += i
  students += 1
  
print(f"total height = {total}")
print(f"number of students = {students}")
print(f"average height = {round(total / students)}")