from datetime import datetime


students = ["차경묵","김지훈","손형우","남시욱"]
attendances = {} #key = name , value = time

def attend(name,is_attend):
    if is_attend == 'True':
        attendances[name] = datetime.now()
    else:
        attendances[name] = "출석안함"



for student in students:
    print(student,"님 출석 하셨습니까?")
    is_attend = input("True or False: ")
    attend(student,is_attend)
else:
    print(attendances)
