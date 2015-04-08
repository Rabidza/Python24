student_grades = {}

while True:
    student_name = raw_input("Please give me the name of the student (q to quit): ")
    if student_name == 'q':
        break
    student_grade = raw_input("Please give me their grade: ")
    student_grades[student_name] = student_grade

print "Okay, printing grades!"
print "Student\t\tGrade"
for key, value in student_grades.iteritems():
    print key, '\t\t', value
