print "Welcome to the student checker!"

ls_class = ['Neill', 'Gerrit', 'Nico']

def student_checker(s_student):
    if s_student in ls_class:
        return True
    else:
        return False

while True:
    student = raw_input("Please give me the name of the student (enter 'q' to quit): ")
    if student == 'q':
        print "Goodbye!"
        break
    elif student_checker(student):
        print "Yes, that student is enrolled in the class!"
    else:
        print "No, that student is not in the class."

    