class Course:

    total_courses = 0

    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name
        self.students = []
        self.total_classes = 0

        Course.total_courses += 1

    def add_student(self, student):
        self.students.append(student)

    def conduct_class(self):
        self.total_classes += 1
        print("Class conducted")

    def course_info(self):
        print("\nCourse ID:", self.course_id)
        print("Course:", self.course_name)
        print("Total Classes:", self.total_classes)
