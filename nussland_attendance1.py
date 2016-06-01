import time

attendances = {}

def attendance(name):
    attendances[name] = time.strftime('%Y-%m-%d %H:%M:%S')

def main():
    students = ['김효성', '박건희', '손종국', '김재현', '홍창우', '임재민', '김지훈', '박문수', '박두철', '설석주', '박근일' ,'김수석']

    for student in students:
        attendance(student)

    print(attendances)

if __name__ == "__main__" :
    main()