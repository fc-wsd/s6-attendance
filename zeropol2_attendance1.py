# 홍창우
# class를 쓰지 않는 출석부

# 상수 정의
USER_ACTION_PRINT = 1
USER_ACTION_ATTEND = 2
USER_ACTION_EXIT = 3

# 변수 정의
user_action = 0
attendance = {'박근일': False, '홍창우': False, '김수석': False, '홍태환': False, '차경묵': False}


def print_menu():
    print('=================')
    print('다음 중 선택해 주세요')
    print('1: 출석부 보기')
    print('2: 출석 처리')
    print('3: 끝내기')
    print('=================')


def input_user_action():
    try:
        return int(input())
    except TypeError:
        return -1
    except ValueError:
        return -1


def resolve_user_action(action):
    if USER_ACTION_PRINT == action:
        print_attendance()
    elif USER_ACTION_ATTEND == action:
        attend()
    elif USER_ACTION_EXIT == action:
        pass
    else:
        print('제대로 입력해 주세요!!')


def print_attendance():
    # TODO 항상 같은 순서로 나오게 정렬 필요
    for attendee in attendance.items():
        status = '결석'
        if attendee[1]:
            status = '출석'

        print('{name} : {status}'.format(name=attendee[0], status=status))


def attend():
    print('이름을 입력하세요')
    name = input()
    if name in attendance.keys():
        attendance[name] = True
    else:
        print('그런 사람 없습니다')


while USER_ACTION_EXIT != user_action:
    print_menu()
    user_action = input_user_action()
    resolve_user_action(user_action)



