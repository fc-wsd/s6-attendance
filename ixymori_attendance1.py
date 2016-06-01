from datetime import datetime

CODE_SUCCESS = 200              # 성공
CODE_OVERLAP = 500              # 중복 출석체크
CODE_NOT_FOUND_STUDENT = 400    # 리스트상 존재하지 않는 사람

students = (
    '설석주', '손종국', '김재현', '홍창우', '임재민',
    '김지훈', '박문수', '박두철', '박근일', '김수석',
)

attendance = {
    '설석주' : [ '2016-05-21', '2016-05-28' ]
}

# 결과 메시지
result_msg = {
    CODE_SUCCESS : '출석에 성공하셨습니다.',
    CODE_OVERLAP : '이미 출석을 하셨습니다.',
    CODE_NOT_FOUND_STUDENT : '학생 리스트에 존재하지 않는 사람입니다.'
}

def attend(name):
    if name in students:
        if name not in attendance:
            attendance.setdefault(name, [])
    else:
        return { 'result_code' :  CODE_NOT_FOUND_STUDENT, 'name' : name }

    current_date = str(datetime.now().date())
    name_attend = attendance[name]

    if current_date in name_attend:
        return { 'result_code' : CODE_OVERLAP, 'name' : name, 'attend_date' : current_date }
    else:
        name_attend.append(current_date)
        return { 'result_code' : CODE_SUCCESS, 'name' : name, 'attend_date' : current_date }

def printResult(result):
    msg = result_msg[result['result_code']]
    print(result['name'], msg)
    pass

printResult(attend('설석주'))
printResult(attend('설석주'))
printResult(attend('박문수'))
printResult(attend('사람1'))
