students = []
attendances =[]
class Student:
    def __init__(self,name):
        self.name = name
        students.append(name)

class Attendance(Student):

    def attend(name):
        attendances.append(name)

    def list():
        print("현재 출석자 명단: %s" %attendances)
