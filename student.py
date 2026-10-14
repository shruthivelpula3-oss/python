class Student:
    total_students = 0
    def __init__(self, student_id, name, branch, year, biometric_id):
        self.student_id = student_id
        self.name = name
        self.branch = branch
        self.year = year
        self.biometric_id = biometric_id
        self.attendance = []

        Student.total_students += 1

    def student_info(self):
        print("\nID:", self.student_id)
        print("Name:", self.name)
        print("Branch:", self.branch)
        print("Year:", self.year)

    def verify_biometric(self, biometric_id):
        return self.biometric_id == biometric_id

    def add_attendance(self, record):
        self.attendance.append(record)

    def view_attendance(self):
        if not self.attendance:
            print("No attendance records")
            return

        for record in self.attendance:
            record.attendance_info()

    def percentage(self, course):
        if course.total_classes == 0:
            return 0

        present = 0

        for record in self.attendance:
            if record.course == course and record.status == "Present":
                present += 1

        return present / course.total_classes * 100
