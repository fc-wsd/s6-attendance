from datetime import datetime

students = {'박문수': '박문수', '손종국': '손종국', '임재민': '임재민', '김지훈': '김지훈'}
attendances = []


def attend(student, date=datetime.today().date()):
    student = students.get(student)
    date = date
    attendances.append([student, date])
