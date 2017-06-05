student_score = int(input("Please enter the student's score. -> "))

if(student_score < 10):
    print("Grade: F")
elif((student_score >= 10) and (student_score < 20)):
    print("Grade: D")
elif((student_score >= 20) and (student_score < 30)):
    print("Grade: C")
elif((student_score >= 30) and (student_score < 40)):
    print("Grade: B")
else:
    print("Grade: A")
