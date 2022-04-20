# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
# Don't use len() and sum()
student_heights_sum = 0
student_heights_len = 0
for n in student_heights:
    student_heights_sum += n
    student_heights_len += 1

print(round(student_heights_sum / student_heights_len))
