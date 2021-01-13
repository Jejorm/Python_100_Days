student_scores = input("Input a list of student scores ").split()
max_number = 0

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])


for student_score in student_scores:
    if max_number < student_score:
        max_number = student_score

print(f"The highest score in the class is: {max_number}")