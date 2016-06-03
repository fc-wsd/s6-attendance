#2016.06.03 HW2
from datetime import datetime

#1번째 조건 : list형 객체
students = ['손종국','김재현','홍창우','임재민']
attendances = {'손종국':'2016-01-01'}

#2번째 조건 : Student 클래스
class Student:
    def __init__(self, name):
        self.name = name

#3번째 조건 : Attendance 클래스
class Attendance:
    def attend(self,s_name):
        #수강생 이름 확인
        name = s_name.name
        if name in students:
            #오늘 날짜 입력
            date = datetime.today()
            attendances[name] = date
            print("수강생 %s씨는 %s에 출석하였습니다." %(name,date))
        else:
            print("%s는(은) 6기 수강생이 아닙니다." %name)

    def list(self):
        print("출석자 명단 ::: %s" %attendances)

name1 = Student('임재민')
name2 = Student('조세호')
name3 = Student('홍창우')
att   = Attendance()

att.attend(name1)
att.list()
att.attend(name2)
att.list()
att.attend(name3)
att.list()
