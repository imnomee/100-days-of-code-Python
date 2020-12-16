# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
height_total = 0
count_total = 0
for height in student_heights:
    height_total += height
    count_total += 1

average = round(height_total / count_total)
print(average)
# print(height_total)
# print(count_total)
