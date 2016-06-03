#2016.06.03 HW1
#date에는 yyyy-mm-dd 양식으로 입력할 것
from datetime import datetime

students = ['손종국','김재현','홍창우','임재민']
attendances = {'손종국':'2016-01-01'}

def attend(name,date):
    #수강생 확인
    if name in students:
        try:
            attend_date = datetime.strptime(date, "%Y-%m-%d").date()
        except Exception as e:
            print("날짜 양식이 맞지 않습니다.")
        attendances[name] = date
        print("수강생 %s씨는 %s에 출석하였습니다." %(name,attend_date))
    else:
        print("등록된 6기 수강생이 아닙니다.")
        add_student(name)

#수강생 추가
def add_student(name):
    students.append(name)


attend('김재현','2016-05-05')  #출석 추가
print(attendances)             #출석부 확인
attend('홍길동','2016-06-06')  #출석부에 없는 이름
print(attendances)
attend('홍길동','2016-06-06')  #출석부에 없는 이름 재입력
print(attendances)
attend('홍창우','2016-99-99')  #날짜 형식 맞지 않을 경우
