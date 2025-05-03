import subprocess

file_nickname = {
    "구구단": "구구단.py",
    "독일어퀴즈": "german_quiz.py",
    "던전 어드벤처": "DungeonAdventure.py",
    "99병의 맥주": "99_bottles_of_beer.py",
    "링딩동": "lingdingdong.py",
    "전투": "battle.py",
    "영영사전": "dictionary.py",
    "가챠": "gacha.py",
    "로그인": "login_version2.py",
    "편의점관리": "store_manage.py",} # 파일 별명과 파일 이름 매핑

while True:
    print("\n파일 목록:")
    for nickname in sorted(file_nickname.keys()):
        print(f"'{nickname}' : {file_nickname[nickname]}")
    todo = input("\n실행할 파일의 별명을 입력하세요 (종료: 'exit'): ")
    if todo == "exit":
        break
    elif todo in file_nickname:
        file_name = file_nickname[todo]
        try:
            # subprocess.run([sys.executable, file_name], check=True)
            subprocess.run(["python", file_name], check=True)
        except subprocess.CalledProcessError as e:
            print(f"파일 실행 중 오류 발생: {e}")
    else:
        print("잘못된 별명입니다. 다시 시도하세요.")
