class Identity:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Student(Identity):
    def __init__(self, id, name, dob):
        super().__init__(id, name)
        self.dob = dob
        self.marks = {}

class Course(Identity):
    def __init__(self, id, name):
        super().__init__(id, name)

def input_student_info():
    n = int(input("Enter the number of students: "))
    students = []
    for i in range(n):
        id = input("Enter the student ID: ")
        name = input("Enter the student name: ")
        dob = input("Enter the student date of birth: ")
        student = Student(id, name, dob)
        students.append(student)
    
    return students


def input_course_info():
    n = int(input("Enter the number of courses: "))
    courses = []
    for i in range(n):
        id = input("Enter the course ID: ")
        name = input("Enter the course name: ")
        course = Course(id, name)
        courses.append(course)
    
    return courses


def input_course_marks(students, courses):
    course_id = input("Enter the course ID: ")
    for course in courses:
        if course.id == course_id:
            course_name = course.name
            break
    else:
        print("Invalid course ID.")
        return
    print("Enter marks for course", course_name)
    for student in students:
        marks = input(f"Enter marks for student {student.name}: ")
        while not marks.isdigit():
            marks = input(f"Invalid input. Please enter marks for student {student.name} again: ")
        student.marks[course_id] = int(marks)


def list_courses(courses):
    print("List of courses: ")
    for course in courses:
        print("----------------------------\n",course.id, course.name)
    print("----------------------------")


def list_students(students):
    print("List of students:")
    for student in students:
        print("------------------------------------\n",student.id, student.name, student.dob)
    print("------------------------------------")


def show_course_marks(students):
    course_id = input("Enter the course ID: ")
    for student in students:
        if course_id in student.marks:
            print(student.name, student.marks[course_id])


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

if __name__ =='__main__':
    main()
