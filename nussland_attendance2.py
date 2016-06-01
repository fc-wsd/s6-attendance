import time

class Student:
    students = ['김효성', '박건희', '손종국', '김재현', '홍창우', '임재민', '김지훈', '박문수', '박두철', '설석주', '박근일' ,'김수석']

class Attendance:
    attendances = {}

    def attend(self, name):
        self.attendances[name] = time.strftime("%Y-%m-%d %H:%M:%S")

    def list(self):
        print("[출석자 명단(이름:일시)]")
        for name in self.attendances.keys():
            print(name +": "+self.attendances[name])

def main():
    student = Student()
    attendance = Attendance()

    # 출석 처리
    for name in student.students:
        attendance.attend(name)

    # 출석자 명단
    attendance.list()

if __name__ == "__main__":
    main()