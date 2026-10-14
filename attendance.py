from datetime import datetime


class Attendance:

    total_attendance = 0

    def __init__(self, student, course):
        self.student = student
        self.course = course

        now = datetime.now()
        self.date = now.strftime("%d-%m-%Y")
        self.time = now.strftime("%I:%M:%S %p")
        self.status = "Not Marked"

    def take_attendance(self, biometric_id):

        if not self.student.verify_biometric(biometric_id):
            print("Biometric verification failed")
            return

        for record in self.student.attendance:
            if record.course == self.course and record.date == self.date:
                print("Attendance already marked today")
                return

        self.status = "Present"
        self.student.add_attendance(self)

        Attendance.total_attendance += 1

        print("Biometric verified")
        print("Attendance marked successfully")
        print("Date:", self.date)
        print("Time:", self.time)

    def attendance_info(self):
        print(
            self.course.course_name,
            self.date,
            self.time,
            self.status
        )
