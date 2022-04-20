# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
# Don't use the min() and max()
high_score = 0
for n in student_scores:
    if n > high_score:
        high_score = n
print(f'The highest score in the class is: {high_score}')
