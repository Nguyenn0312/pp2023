def input_student_info():
    n = int(input("Enter the number of students: "))
    students = []
    for i in range(n):
        id = input("Enter the student ID: ")
        name = input("Enter the student name: ")
        dob = input("Enter the student date of birth: ")
        student = {'id': id, 'name': name, 'dob': dob}
        students.append(student)
    
 
    for student in students:
        for key, value in student.items():
            if not value:
                student[key] = input(f"{key} is missing for student {student['name']}. Please enter it: ")
    
    return students


def input_course_info():
    n = int(input("Enter the number of courses: "))
    courses = []
    for i in range(n):
        id = input("Enter the course ID: ")
        name = input("Enter the course name: ")
        course = {'id': id, 'name': name}
        courses.append(course)
    

    for course in courses:
        for key, value in course.items():
            if not value:
                course[key] = input(f"{key} is missing for course {course['id']}. Please enter it: ")
    
    return courses


def input_course_marks(students, courses):
    course_id = input("Enter the course ID: ")
    for course in courses:
        if course['id'] == course_id:
            course_name = course['name']
            break
    else:
        print("Invalid course ID.")
        return
    print("Enter marks for course", course_name)
    for student in students:
        marks = int(input("Enter marks for student " + student['name'] + ": "))
        student.setdefault('marks', {}).update({course_id: marks})


def list_courses(courses):
    print("List of courses: ")
    for course in courses:
        print("----------------------------\n",course['id'], course['name'])
    print("----------------------------")


def list_students(students):
    print("List of students:")
    for student in students:
        print("----------------------------------\n",student['id'], student['name'], student['dob'])
    print("----------------------------------")


def show_course_marks(students):
    course_id = input("Enter the course ID: ")
    for student in students:
        if 'marks' in student and course_id in student['marks']:
            print(student['name'], student['marks'][course_id])


def main():
    students = input_student_info()
    courses = input_course_info()

    while True:
        print("1. Input marks for a course")
        print("2. List students")
        print("3. List courses")
        print("4. Show student marks for a course")
        print("5. Quit")

        category = int(input("Enter the number of category that you want: "))
        if category == 1:
            input_course_marks(students, courses)
        elif category == 2:
            list_students(students)
        elif category == 3:
            list_courses(courses)
        elif category == 4:
            show_course_marks(students)
        elif category == 5:
            break
        else:
            print("Invalid category.")

if __name__ == '__main__':
    main()
