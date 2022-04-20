student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for name in student_scores:
    student_grade = student_scores[name]
    if student_grade >= 91:
        student_grades[name] = "Outstanding"
    elif student_grade <= 90 and student_grade >= 81:
        student_grades[name] = "Exceeds Expectations"
    elif student_grade <= 80 and student_grade >= 71:
        student_grades[name] ="Acceptable"
    else:
        student_grades[name] = "Fail"


# 🚨 Don't change the code below 👇
print(student_grades)