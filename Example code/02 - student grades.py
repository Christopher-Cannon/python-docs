student_grade = int(input("Please enter the student's grade. -> "))

if(student_grade < 10):
    print("Grade: F")
elif((student_grade >= 10) and (student_grade < 20)):
    print("Grade: D")
elif((student_grade >= 20) and (student_grade < 30)):
    print("Grade: C")
elif((student_grade >= 30) and (student_grade < 40)):
    print("Grade: B")
else:
    print("Grade: A")
