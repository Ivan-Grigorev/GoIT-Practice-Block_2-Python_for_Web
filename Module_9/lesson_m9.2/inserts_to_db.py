from datetime import date
from faker import Faker
from models import Session, engine, Base
from models import Teacher, Student, Course


fake = Faker()
session = Session()

math_course = Course("Math", fake.text())
physics_course = Course("Physics", fake.text())
geographic_course = Course("Geography", fake.text())
biology_course = Course("Biology", fake.text())

teacher_1 = Teacher(fake.first_name(), fake.last_name(), math_course)
teacher_2 = Teacher(fake.first_name(), fake.last_name(), physics_course)
teacher_3 = Teacher(fake.first_name(), fake.last_name(), geographic_course)
teacher_4 = Teacher(fake.first_name(), fake.last_name(), biology_course)
teacher_5 = Teacher(fake.first_name(), fake.last_name(), math_course)
teacher_6 = Teacher(fake.first_name(), fake.last_name(), physics_course)

student_1 = Student(fake.first_name(), fake.last_name(), fake.date_object(end_datetime=date(2003, 12, 12)))
student_2 = Student(fake.first_name(), fake.last_name(), fake.date_object(end_datetime=date(2003, 12, 12)))
student_3 = Student(fake.first_name(), fake.last_name(), fake.date_object(end_datetime=date(2003, 12, 12)))
student_4 = Student(fake.first_name(), fake.last_name(), fake.date_object(end_datetime=date(2003, 12, 12)))
student_5 = Student(fake.first_name(), fake.last_name(), fake.date_object(end_datetime=date(2003, 12, 12)))
student_6 = Student(fake.first_name(), fake.last_name(), fake.date_object(end_datetime=date(2003, 12, 12)))

math_course.student = [student_6, student_5, student_4, student_3, student_2, student_1]
biology_course.student = [student_1, student_2, student_3]
physics_course.student = [student_1, student_2, student_3, student_4]
geographic_course.student = [student_1, student_6]

teacher_1.student = [student_1, student_2, student_3]
teacher_2.student = [student_1, student_2]
teacher_3.student = [student_1, student_6]
teacher_4.student = [student_1, student_2, student_3]
teacher_5.student = [student_6, student_5, student_4]
teacher_6.student = [student_3, student_4]

session.add(math_course)
session.add(physics_course)
session.add(geographic_course)
session.add(biology_course)

session.add(teacher_1)
session.add(teacher_2)
session.add(teacher_3)
session.add(teacher_4)
session.add(teacher_5)
session.add(teacher_6)

session.add(student_1)
session.add(student_2)
session.add(student_3)
session.add(student_4)
session.add(student_5)
session.add(student_6)

session.commit()
session.close()
