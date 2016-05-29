#HW1 
student = ["차경묵","김지훈","손형우","남시욱"]
attendances = []
#날짜,이름 출석부에 입력하기
def attend (date, name):
    if name in student:
        attendances.append(date)
        attendances.append(name)
    #대출 방지
    else:
        print("대출은 안됩니다.")

#수강생 추가하기
def adder (name):
    student.append(name)
