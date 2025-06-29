import keyboard
import time

print("가져올 파일의 이름을 입력하세요 (예: example.txt): ")
file_name = input().strip()

try:
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
except FileNotFoundError:
    print(f"파일 '{file_name}'을(를) 찾을 수 없습니다.")
    exit()
print("파일 내용이 성공적으로 읽혔습니다. 자동 입력을 시작합니다...")

for i in range(5, 0, -1):
    print(f"{i}초 뒤 자동으로 입력됩니다...")
    time.sleep(1)
keyboard.write(content, delay=0.05)  # delay는 각 글자 사이의 시간 간격을 조정합니다.
print("자동 입력이 완료되었습니다.")