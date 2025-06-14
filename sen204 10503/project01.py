# Input grades and credit units for each course
course1_grade = int(input("Enter the grade for course 1 (0-100): "))
course1_credit = int(input("Enter the credit units for course 1: "))

course2_grade = int(input("Enter the grade for course 2 (0-100): "))
course2_credit = int(input("Enter the credit units for course 2: "))

course3_grade = int(input("Enter the grade for course 3 (0-100): "))
course3_credit = int(input("Enter the credit units for course 3: "))

course4_grade = int(input("Enter the grade for course 4 (0-100): "))
course4_credit = int(input("Enter the credit units for course 4: "))

course5_grade = int(input("Enter the grade for course 5 (0-100): "))
course5_credit = int(input("Enter the credit units for course 5: "))

# Function to convert percentage grades to grade points
def grade_point(percentage):
    # Check the range of the percentage and assign grade points accordingly
    if 90 <= percentage <= 100:
        return 4.0
    elif 80 <= percentage < 90:
        return 3.0
    elif 70 <= percentage < 80:
        return 2.0
    elif 60 <= percentage < 70:
        return 1.0
    else:
        return 0.0

# Calculate grade points for each course
a = grade_point(course1_grade)
b = grade_point(course2_grade)
c = grade_point(course3_grade)
d = grade_point(course4_grade)
e = grade_point(course5_grade)

# Calculate total grade points and total credit units
total_grade_points = (a * course1_credit +
                     b * course2_credit +
                     c * course3_credit +
                     d * course4_credit +
                     e * course5_credit)

total_credit_units = course1_credit + course2_credit + course3_credit + course4_credit + course5_credit

# Calculate CGPA
cgpa = total_grade_points / total_credit_units

# Display CGPA
print("Calculating CGPA... Please wait.")
print("------------------------------")
print("CGPA Calculation Complete!")
print("Here is the breakdown of your grades:")
print(total_grade_points)
print(total_credit_units)
