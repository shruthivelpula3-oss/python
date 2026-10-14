from course import Course
from campus import Campus

campus = Campus("Smart Campus")

course = Course("C101", "Python")

campus.add_course(course)

campus.run_system()
