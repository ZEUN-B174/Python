from dataclasses import dataclass

# dataclass로 User 클래스를 정의합니다.
@dataclass
class User:
    username: str
    password: str
    name: str
    email: str

login_status = False  # 로그인 상태를 저장하는 변수

def register(users: list):
    """사용자 등록 함수"""
    username = input("사용자 이름을 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")
    name = input("이름을 입력하세요: ")
    email = input("이메일을 입력하세요: ")

    # User 객체를 생성하고 리스트에 추가합니다.
    user = User(username, password, name, email)
    users.append(user)
    print(f"등록 완료: {user}")

def login(users: list):
    """사용자 로그인 함수"""
    username = input("사용자 이름을 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")

    # 사용자 리스트에서 사용자 정보를 검색합니다.
    for user in users:
        if user.username == username and user.password == password:
            print(f"로그인 성공: {user.name}")
            global login_status
            login_status = True
            return user

    print("로그인 실패: 사용자 이름 또는 비밀번호가 잘못되었습니다.")
    return None

def logout(user: User):
    """사용자 로그아웃 함수"""
    global login_status
    if login_status:
        print(f"{user.name}님, 로그아웃되었습니다.")
        login_status = False
    else:
        print("로그인 상태가 아닙니다.")

def account_info(user: User):
    """사용자 정보 출력 함수"""
    if login_status:
        print(f"사용자 이름: {user.username}")
        print(f"이름: {user.name}")
        print(f"이메일: {user.email}")
    else:
        print("로그인 상태가 아닙니다.")

def main():
    """메인 함수"""
    users = []  # 사용자 정보를 저장할 리스트
    while True:
        print("\n1. 사용자 등록")
        print("2. 로그인")
        print("3. 로그아웃")
        print("4. 사용자 정보")
        print("5. 종료")
        choice = input("원하는 작업을 선택하세요: ")

        if choice == '1':
            register(users)
        elif choice == '2':
            user = login(users)
        elif choice == '3':
            if 'user' in locals():
                logout(user)
            else:
                print("로그인 상태가 아닙니다.")
        elif choice == '4':
            if 'user' in locals():
                account_info(user)
            else:
                print("로그인 상태가 아닙니다.")
        elif choice == '5':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")


if __name__ == "__main__":
    main()