import datetime
import random
import copy

class Student:
    _name = ""
    _attended_time = "결석"

    def __init__(self, name):
        self._name = name

    def attend(self, time):
        self._attended_time = time

class Attendance:
    _attendances = {}

    def attend(self, student, time):
        student.attend(time)
        self._attendances[student._name] = student

    def list(self):
        print('{} 출석부 ({}/{})'.format(datetime.date.today(), len(self._attendances), len(students)))
        for student in students:
            print("이름 : ", student._name, ", 출석시간 : ", student._attended_time)



students = []
students.append(Student('박두철'))
students.append(Student('손종국'))
students.append(Student('김재현'))
students.append(Student('홍창우'))
students.append(Student('임재민'))
students.append(Student('김지훈'))
students.append(Student('박문수'))

attendance = Attendance()

for student in students:
    if random.random() <= 0.8:
        time = datetime.datetime.now().time()
        attendance.attend(student, time.strftime('%H:%M:%S'))

students.sort(key=lambda student:student._name)

attendance.list()
