# - 학생명단이 있는 객체 'students'명단
#  - 6시 실제 수강생 이름으로 구성.
#  - 자료형은 자유
# - 출자는 'attendances' 객체에 저장하며, 출석 일시와 이름은 필수 저장 항목
# - attend() 함수로 출석 처리
# - 클래스로 만들지 말것

students = ["박근일", "홍창우", "김수석", "홍태환", "차경묵"]   # String
attendances = []    # Dictionary

def attend(name, date):
    for name_in_class in students:
        if name_in_class == name:
            attendances.append({"name": name, "date": date})
            break
