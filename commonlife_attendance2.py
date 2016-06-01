# - 학생 명단이 있는 list 형 객체 'students' 명단
# - 학생은 student 클래스로 생성
#  - 필수 정보 : 이름
# - 출석부는 attendance 클래스로 생성한 객체
#  - attend() 인스턴스 메소드로 출석처리하며, 인자는 'Student' 클래스로 만든 학생 객체
#  - list() 인스턴스 메소드로 출석자 명단 출력

students = ["박근일", "홍창우", "김수석", "홍태환", "차경묵"]   # String
attendances = []    # Dictionary

class Student:
    name = ""

    def __init__(self, name):
        self.name = name

class Attendance:
    def attend(self, student, date):
        for name_in_class in students:
            if name_in_class == student.name:
                attendances.append({"name": student.name, "date": date})
                break

    def list(self):
        for attended in attendances:
            print(attended["name"])


s1 = Student("박근일")
s2 = Student("홍창우")
s3 = Student("김수석")
s4 = Student("홍태환")
s5 = Student("차경묵")

attend_list = Attendance()
attend_list.attend(s1, "20160601")
attend_list.attend(s2, "20160601")
attend_list.attend(s3, "20160601")
attend_list.attend(s4, "20160601")
attend_list.attend(s5, "20160601")

attend_list.list()
