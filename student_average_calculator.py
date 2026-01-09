print("Student Marks Average Calculator")
num_students = int(input("Enter number of students: "))

total = 0

for i in range(1, num_students + 1):
    marks = float(input(f"Enter marks for student {i}: "))
    total += marks

average = total / num_students
print(f"Average marks of {num_students} students is: {average}")