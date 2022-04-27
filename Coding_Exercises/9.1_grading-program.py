student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆
student_grades = {}
for n in student_scores:
    score = student_scores[n]
    if score > 90 and score <= 100:
        student_grades[n] = 'Outstanding'
    elif score > 80 and score <= 90:
        student_grades[n] = 'Exceeds Expectations'
    elif score > 70 and score <= 80:
        student_grades[n] = 'Acceptable'
    elif score <= 70:
        student_grades[n] = 'Fail'


# 🚨 Don't change the code below 👇
print(student_grades)
