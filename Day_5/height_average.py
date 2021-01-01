student_heights = input("Input a list of student heights ").split()
height_sum = 0
students = 0


for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])


for student_height in student_heights:
    height_sum += student_height


for student in student_heights:
    students += 1

average = round(height_sum / students)
print(average)