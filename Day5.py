# Loops

# For Loop

# for item in list_items:
# do something

fruits = ["Apple", "Orange", "Banana"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")

# Average Height

student_heights = input("Input a list of student heights").split()

print(student_heights)
height_total = 0
for height in student_heights:
    height_total += int(height)
    avg = height_total / len(student_heights)
print(f"The average of the entered heights is: {avg}")

# Highest w.o using max function

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()

highest = 0
for score in student_scores:
    if int(score) > highest:
        highest = int(score)
print(highest)

# Range function

# Add numbers 1 - 100
total = 0
for number in range(1, 100):
    total += number
print(total)
