student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
highest = 0
for i in student_scores:
    if i > highest:
        highest = i

print(highest)