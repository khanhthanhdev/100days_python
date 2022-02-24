student_heights = input("Input a list of student heights ").split()
sum=0
average = 0
for i in student_heights:
    sum += int(i)

average = sum/len(student_heights)
print(round(average))