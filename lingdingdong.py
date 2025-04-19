import random
import time

upper = random.randrange(1,41)
multiple1 = random.randrange(2,10)
multiple2 = random.randrange(2,10)
result = ''
score = 100

print("링딩동 퀴즈에 오신 것을 환영합니다!")
time.sleep(2)
print("\n이름이 뭐 이러냐 하시는데 간단하게 설명드리자면,")
time.sleep(2)
print("각각 조건식 1, 2, 3이 있는데 아무 숫자나 넣어서 엔터를 누르면")
time.sleep(2)
print("조건식 1이 참이면 '링'을 출력, 조건식 2가 참이면 '딩'을 출력, 조건식 3이 참이면 '동'을 출력하게 됩니다!")
time.sleep(3)
print("최대한 빨리 '링딩동'을 완성하고 조건식의 숫자를 맞춰 추가 점수를 얻어보세요!")
time.sleep(2)
print("그럼, 지금부터 시작!")
time.sleep(1)

while True:
    ans = int(input("\n숫자를 입력하세요!\n▶ "))
    if ans > upper:
        result += '링'

    if ans%multiple1 == 0:
        result += '딩'

    if ans%multiple2 == 0:
        result += '동'

    print(result)
    time.sleep(1)
    if result == '링딩동':
        print("축하드립니다!")
        break
    else:
        result = ''
        score -= 1

time.sleep(2)
print("\n그럼 이제 추가 퀴즈의 시간입니다...")
time.sleep(2)
print("조건식에서 숫자만 맞추면 되니 그리 어렵진 않을 겁니다.")
time.sleep(2)
print("최대한 빨리 맞춰 최고점을 받아보세요!")
time.sleep(2)

while True:
    ans = int(input("\n조건식 1: 입력한 숫자는 n보다 커야 한다. 에서 n은? (1 ≤ n ≤ 40)\n▶ "))
    if ans == upper:
        print("정답입니다! 계속해서 맞춰보세요!")
        time.sleep(1)
        break
    elif ans > upper:
        print("오답입니다! 당신이 입력한 값은 정답보다 큽니다. 다시 맞춰보세요!")
        time.sleep(1)
        score -= 1
    else:
        print("오답입니다! 당신이 입력한 값은 정답보다 작습니다. 다시 맞춰보세요!")
        time.sleep(1)
        score -= 1

while True:
    ans = int(input("\n조건식 2: 입력한 숫자는 n의 배수여야 한다. 에서 n은? (2 ≤ n ≤ 9)\n▶ "))
    if ans == multiple1:
        print("정답입니다! 계속해서 맞춰보세요!")
        time.sleep(1)
        break
    else:
        print("오답입니다! 다시 맞춰보세요!")
        time.sleep(1)
        score -= 1

while True:
    ans = int(input("\n조건식 3: 입력한 숫자는 n의 배수여야 한다. 에서 n은? (2 ≤ n ≤ 9)\n▶ "))
    if ans == multiple2:
        print("정답입니다! 마지막까지 맞추셨군요!")
        time.sleep(1)
        break
    else:
        print("오답입니다! 다시 맞춰보세요!")
        time.sleep(1)
        score -= 1

print("\n이제 모든 퀴즈가 끝이 났습니다!")
time.sleep(1)
print("당신의 점수는...")
time.sleep(2)
print(str(score) + "점! 어떤가요? 괜찮은 점수인가요?")
time.sleep(2)
print("링딩동 퀴즈를 즐겨주셔서 감사합니다!")
