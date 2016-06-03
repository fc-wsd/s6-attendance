from datetime import datetime
from django.db import models

students = ['박문수', '손종국', '임재민', '김지훈']


class Student:

    def __init__(self, name):
        for student_name in students:
           if name == student_name:
                self.name = name
           else:
               Exception('not in students list')


class Attendance:
    attendance = []

    def attend(self, name, date=datetime.today().date()):
        for student_name in students:
           if name == student_name:
               self.attendance.append([name, date])

    def list(self):
        attendance_list = []
        for student in self.attendance:
            attendance_list.append(student[0])
        return attendance_list



