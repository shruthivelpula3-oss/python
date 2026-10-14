from student import Student
from attendance import Attendance
class Campus:
    total_campus = 0
    def __init__(self, name):
        self.name = name
        self.students = []
        self.courses = []
        Campus.total_campus += 1
        self.students.append(
            Student("S101", "Shruti", "CSE AI-ML", 4, "BIO101")
        )
        self.students.append(
            Student("S102", "Priya", "CSE AI-ML", 4, "BIO102")
        )
        self.students.append(
            Student("S103", "Anjali", "CSE AI-ML", 4, "BIO103")
        )
    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)

        for student in self.students:
            course.add_student(student)

    def search_student(self):
        sid = input("Enter Student ID: ")

        for student in self.students:
            if student.student_id == sid:
                student.student_info()
                return

        print("Student not found")

    def biometric_attendance(self):
        biometric_id = input("Scan Biometric ID: ")

        for student in self.students:

            if student.biometric_id == biometric_id:

                course = self.courses[0]

                record = Attendance(
                    student,
                    course
                )

                record.take_attendance(
                    biometric_id
                )

                return

        print("Biometric ID not found")

    def view_attendance(self):
        sid = input("Enter Student ID: ")

        for student in self.students:

            if student.student_id == sid:
                student.view_attendance()
                return

        print("Student not found")

    def attendance_percentage(self):
        sid = input("Enter Student ID: ")

        for student in self.students:

            if student.student_id == sid:

                course = self.courses[0]

                percentage = student.percentage(course)

                print(
                    "Attendance:",
                    round(percentage, 2),
                    "%"
                )

                if percentage < 50:
                    print("WARNING: Low attendance")
                else:
                    print("Attendance is above 50%")

                return

        print("Student not found")

    def run_system(self):

        while True:

            print("\nSMART CAMPUS")
            print("1. Add Student")
            print("2. Search Student")
            print("3. View Students")
            print("4. Conduct Class")
            print("5. Biometric Attendance")
            print("6. View Attendance")
            print("7. Attendance Percentage")
            print("8. Course Information")
            print("9. Exit")

            choice = input("Enter choice: ")

            if choice == "1":

                student = Student(
                    input("Student ID: "),
                    input("Name: "),
                    input("Branch: "),
                    input("Year: "),
                    input("Biometric ID: ")
                )

                self.add_student(student)
                self.courses[0].add_student(student)

                print("Student added successfully")

            elif choice == "2":

                self.search_student()

            elif choice == "3":

                if not self.students:
                    print("No students available")

                else:
                    for student in self.students:
                        student.student_info()

            elif choice == "4":

                self.courses[0].conduct_class()

            elif choice == "5":

                self.biometric_attendance()

            elif choice == "6":

                self.view_attendance()

            elif choice == "7":

                self.attendance_percentage()

            elif choice == "8":

                self.courses[0].course_info()

            elif choice == "9":

                print("Thank you")
                break

            else:

                print("Invalid choice")
