'''
    학생 명단이 있는 `list`형 객체 `students`명단.
    학생은 `Student` 클래스로 생성.
        ~ 필수 정보 : 이름
    출석부는 `Attendance` 클래스로 생성한 객체
        ~ `attend()` 인스턴스 메서드로 출석 처리하며, 인자는 `Student` 클래스로 만든 학생 객체
        ~ `list()` 인스턴스 메서드로 출석자 명단 출력
'''
from datetime import datetime

CODE_SUCCESS = 200
CODE_OVERLAP = 500

result_msg = {
    CODE_SUCCESS : '출석에 성공하셨습니다.',
    CODE_OVERLAP : '이미 출석을 하셨습니다.'
}

students = []

class Student(object):
    _name = ''
    def __init__(self, name):
        self._name = name
        if name not in students:
            students.append(name)

    def get_name(self):
        return self._name

class Attendance(object):
    _attend = {'설석주' : [ '2016-05-21', '2016-05-28' ],}

    def attend(self, student):
        name = student.get_name()
        if name not in self._attend:
            self._attend.setdefault(name, [])

        current_date = str(datetime.now().date())
        name_attend = self._attend[name]

        if current_date in name_attend:
            return CODE_OVERLAP
        else:
            name_attend.append(current_date)
            return CODE_SUCCESS

    def list(self):
        print('-' * 10, '<전체 리스트>', '-' * 10)
        for item in self._attend.items():
            print('{line}<{name}님의 출석리스트>{line}'.format(line = ('-' * 10), name = item[0]))
            for time in item[1]:
                print(time);

def print_result(result_code, student):
    print('{name}님 {msg}'.format(name = student.get_name(), msg = result_msg[result_code]));

attendance = Attendance()

student_1 = Student('설석주')
student_2 = Student('사람1')
student_3 = Student('사람2')
student_4 = Student('사람3')
student_5 = Student('사람4')
student_6 = Student('설석주')

print_result(attendance.attend(student_1), student_1)
print_result(attendance.attend(student_2), student_2)
print_result(attendance.attend(student_3), student_3)
print_result(attendance.attend(student_4), student_4)
print_result(attendance.attend(student_5), student_5)
print_result(attendance.attend(student_6), student_6)
print('')

attendance.list()
