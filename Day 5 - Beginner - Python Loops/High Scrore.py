# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

  # Write your code below this row 👇
min = 0
max = 0
for number in student_scores:
  if number >= max:
    max = number

    
print(f"The highest score in the class is: {max}")