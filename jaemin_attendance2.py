# 임재민
# 출석부 만들기 2
from datetime import datetime

students = []
attendances = []

class Student(object):
    def __init__(self, name):
        self.name = name

class Attendance(object):
    def attend(self, student):
        if student in students:
            attendances.append(student.name)
            time = datetime.now()
            attendances.append(time)

    def list(self):
        print(attendances)

st1 = Student('임재민')
st2 = Student('손종국')
students.append(st1)
students.append(st2)

a = Attendance()
a.attend(st1)
a.list()
a.attend(st2)
a.list()
