# 홍창우
# class를 사용한 출석부


class Attendee:
    name = ""
    status = False

    def __init__(self, name):
        self.name = name

    def attend(self, status):
        self.status = status


class Attendance:
    # 상수 정의
    USER_ACTION_PRINT = 1
    USER_ACTION_ATTEND = 2
    USER_ACTION_EXIT = 3

    _user_action = 0
    attendance = []

    def __init__(self):
        self.attendance.append(Attendee('박근일'))
        self.attendance.append(Attendee('홍창우'))
        self.attendance.append(Attendee('김수석'))
        self.attendance.append(Attendee('홍태환'))
        self.attendance.append(Attendee('차경묵'))

    @staticmethod
    def print_menu():
        print('=================')
        print('다음 중 선택해 주세요')
        print('1: 출석부 보기')
        print('2: 출석 처리')
        print('3: 끝내기')
        print('=================')

    def input_user_action(self):
        try:
            self._user_action = int(input())
        except TypeError:
            return -1
        except ValueError:
            return -1

    def resolve_user_action(self, action):
        if self.USER_ACTION_PRINT == action:
            self.print_attendance()
        elif self.USER_ACTION_ATTEND == action:
            self.attend()
        elif self.USER_ACTION_EXIT == action:
            pass
        else:
            print('제대로 입력해 주세요!!')

    def print_attendance(self):
        for attendee in self.attendance:
            status = '결석'
            if attendee.status:
                status = '출석'

            print('{name} : {status}'.format(name=attendee.name, status=status))

    def attend(self):
        print('이름을 입력하세요')
        name = input()
        is_valid_attendee = False
        for attendee in self.attendance:
            if name == attendee.name:
                attendee.attend(status=True)
                is_valid_attendee = True

        if not is_valid_attendee:
            print('그런 사람 없습니다')

    def get_user_action(self):
        return self._user_action


attendance = Attendance()
while Attendance.USER_ACTION_EXIT != attendance.get_user_action():
    Attendance.print_menu()
    attendance.input_user_action()
    attendance.resolve_user_action(action=attendance.get_user_action())



