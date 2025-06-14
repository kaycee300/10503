# python code calculating cgpa
no_of_courses = int(input("Input total number of courses : "))
unit_store = []
student_score = []
    #  The loop variable i takes values from 0 to no_of_courses - 1.
for i in range(no_of_courses):
    course_code = input("input course code :")
    unit = input("please input course units : ")
    
    #  Validate input for unit
    #  This block of code ensures that a valid value is inputed before running
    while not unit.isdigit():
        print("Please input a valid number : ")
        unit = input("please input course units : ")

     #  After validating the input, this line converts the value of unit to an integer using int() and appends or adds it to the unit_store list.
    unit = int(unit)
    unit_store.append(unit)
    
    grades = input("input student's score : ")
    
    #  Validate input for grades
    #  Similar to the validation for unit, this block of code ensures that the input for grades is a valid integer.
    while not grades.isdigit():
        print("Please enter a valid number : ")
        grades = input("input student's score : ")

    #  After validating the input, this line converts the value of grades to an integer using int().
    grades = int(grades)
    
    if grades > 70:
        score = 5 * unit
    elif 60 <= grades <= 70:
        score = 4 * unit
    elif 50 <= grades < 60:
        score = 3 * unit
    elif 40 <= grades < 50:
        score = 2 * unit 
    else:
        score = 1 * unit

    #  This line appends the calculated score for the current course to the student_score list.
    student_score.append(score)

# Calculate CGPA
#  These lines calculates the  (CGPA) by dividing the sum of the student's scores by the sum of the course units for all courses.
cgpa = sum(student_score) / sum(unit_store)
print("Your CGPA is " + str(cgpa))

