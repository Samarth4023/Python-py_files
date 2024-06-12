# Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

def find_second_lowest_grade_students():
    students = []
    
    # Input number of students
    num_students = int(input("Enter the number of students: "))
    
    # Input student names and grades
    for _ in range(num_students):
        name = input("Enter student name: ")
        grade = float(input("Enter student grade: "))
        students.append([name, grade])
        print(students)
    
    # Extract all grades and find the unique sorted grades
    grades = sorted({student[1] for student in students})
    print(grades)
    
    # Find the second lowest grade
    second_lowest_grade = grades[1]
    print(second_lowest_grade)
    
    # Find all students with the second lowest grade
    second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]
    print(second_lowest_students)
    
    # Sort the names alphabetically
    second_lowest_students.sort()
    print(second_lowest_students)
    
    # Print the names of the students with the second lowest grade
    for student in second_lowest_students:
        print(student)

# Call the function
find_second_lowest_grade_students()
