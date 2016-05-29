
student = ["차경묵","김지훈","손형우","남시욱"]
attendances = []

def attend (date, name):
    if name in student:
        attendances.append(date)
        attendances.append(name)
    else:
        print("대출은 안됩니다.")


def adder (name):
    student.append(name)
