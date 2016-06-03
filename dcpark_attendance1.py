import datetime
import random
import copy

students = ['박두철', '손종국', '김재현', '홍창우', '임재민', '김지훈', '박문수']
attendances = {}

def attend(student, time):
    attendances[student] = time

def show_result():
    print('{} 출석부 ({}/{})'.format(datetime.date.today(), len(attendances), len(students)))
    for student in students:
        attend_time = attendances.get(student, '결석')
        print("이름 : ", student, ", 출석시간 : ", attend_time)

for student in students:
    if random.random() <= 0.8:
        time = datetime.datetime.now().time()
        attend(student, time.strftime('%H:%M:%S'))

students.sort()
show_result()
