import time

attendances = {}

def attend(name):
    attendances[name] = time.strftime('%Y-%m-%d %H:%M:%S')
    print(name +"님 "+ attendances[name] + " 에 출석.")

def main():
    students = ['김효성', '박건희', '손종국', '김재현', '홍창우', '임재민', '김지훈', '박문수', '박두철', '설석주', '박근일' ,'김수석']

    # 출석 처리
    for student in students:
        attend(student)

if __name__ == "__main__" :
    main()