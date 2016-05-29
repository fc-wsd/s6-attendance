#Hw2
students = []
attendances =[]
#이름 students에 저장하기
class Student:
    def __init__(self,name):
        self.name = name
        students.append(name)
#출석확인하고, 명단보여주기
class Attendance(Student):
    def attend(name):
        attendances.append(name)
    def list():
        print("현재 출석자 명단: %s" %attendances)
