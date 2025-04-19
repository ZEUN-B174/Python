import time
import random

lantern = 0
dice = 0

def GameOver():
    time.sleep(1)
    ans = input("\n처음부터 다시 시작할까요?\n▶ ")
    if ans == "예":
        print("\n프로그래머의 능지 이슈로 다시 실행하기를 만들지 못했습니다...")
        time.sleep(1)
        print("어쩔 수 없이 프로세스를 종료합니다...")
        time.sleep(1)
        quit()
    else:
        quit()

def NextScreen():
    for i in range(3):
        print(".")
        time.sleep(0.2)
    time.sleep(0.8)
    print("\n--------------------------------------------------------")

print("던전 어드벤처에 오신 것을 환영합니다!")
time.sleep(1)

ans = input("\n시작할까요?(예/아니오)\n▶ ")
if ans == "예":
    print("\n그럼 시작하겠습니다...\n")
    time.sleep(1)
else:
    print("\n아니그럴거면왜실행한")
    time.sleep(0.2)
    quit()

print("당신은 의뢰를 받아 어느 폐허가 된 성을 둘러보고 있었습니다.")
time.sleep(1)
print("별 볼일 없는 물건들만 있었기에 당신은 그냥 돌아가려고 했죠.")
time.sleep(1)
print("그 때 당신이 어떤 상자를 치우자 숨겨진 다락문을 발견했습니다!")
time.sleep(1)

ans = input("\n이 문으로 바로 들어갈까요?\n▶ ")
if ans == "예":
    dice = random.randrange(1,11)
    if dice >= 5:
        print("\n당신은 어두운 다락문 안으로 들어가자마자 깊은 바닥에 떨어져 사망했습니다...")
        time.sleep(1)
        print("당신은 50%의 확률로 안좋은 결말에 도달했습니다.")
        GameOver()
    else:
        print("당신은 다락문을 자세히 살펴 사다리가 있는 것을 발견하고 사다리를 따라 내려갔습니다.")
        time.sleep(1)
else:
    print("\n당신은 다락문 안쪽을 제대로 살피기 위해 주변에서 쓸만한 물건을 찾기로 했습니다.")
    time.sleep(1)
    print("...")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("\n근처에서 쓸만한 랜턴 1개를 챙겼습니다!")
    lantern += 1
    time.sleep(1)
    print("어서 다락문으로 다시 가보죠!")
    time.sleep(1)

NextScreen()
print("\n다락문으로 가 보니 사다리가 있었습니다.")
time.sleep(1)
print("당신은 그 사다리를 타고 안전하게 지하로 내려갑니다.")
time.sleep(1)

NextScreen()
print("\n사다리를 타고 안전하게 내려간 당신은 한 지하도에 다다랐습니다.")
time.sleep(1)
print("걷다보니 3개의 갈림길이 보이는군요.")
time.sleep(1)
print("첫번째 갈림길은 매우 어둡습니다. 랜턴이 없다면 한 발짝도 못 디딜 것 같군요.")
time.sleep(1)
print("두번째 길에서는 약간 비릿한 냄새가 나는 듯 합니다.")
time.sleep(1)
print("세번째 길은 그나마 밝아서 안전해 보입니다.")
time.sleep(1)

ans = input("\n몇번쨰 길로 가겠습니까?(숫자만 쓰세요)\n▶ ")
dice = random.randrange(1,11)
if ans == "1" and lantern == 0:
    print("\n랜턴 없이 첫번쨰 길로 가던 당신은 앞이 하나도 안 보여 결국 원점으로 돌아왔습니다.")
    time.sleep(1)
    
    ans = input("\n몇번쨰 길로 가겠습니까?(숫자만 쓰세요)\n▶ ")
    if ans == "2":
        if dice >= 8:
            print("\n두번째 길로 가던 중 불운하게도 맹수와 마주쳐 사망했습니다...")
            time.sleep(1)
            print("당신은 30%의 확률로 안좋은 결말에 도달했습니다.")
            GameOver()
        else:
            print("\n두번째 길로 가던 중 맹수의 소리가 들리는 듯 했지만 다행히 아무 일도 일어나지 않았습니다.")
            time.sleep(1)
    else:
        if dice >= 3:
            print("\n세번째 길로 가던 당신은 방심한 틈에 함정에 걸려 사망했습니다...")
            time.sleep(1)
            print("당신은 80%의 확률로 안좋은 결말에 도달했습니다.")
            GameOver()
        else:
            print("\n세번째 길로 가던 당신은 길을 따라 걷다 다행히 함정을 제 때 발견해 피해갔습니다.")
            time.sleep(1)
        
elif ans == "1":
    print("\n랜턴을 들고 가던 당신은 무사히 갈림길의 끝에 도착했습니다.")
    time.sleep(1)
    
elif ans == "2":
    if dice >= 8:
        print("\n불운하게도 맹수와 마주친 당신은 사망했습니다...")
        time.sleep(1)
        print("당신은 30%의 확률로 안좋은 결말에 도달했습니다.")
        GameOver()
    else:
        print("\n맹수의 소리가 들리는 듯 했지만 다행히 아무 일도 일어나지 않았습니다.")
        time.sleep(1)
else:
    if dice >= 3:
        print("\n당신은 방심한 틈에 함정에 걸려 사망했습니다...")
        time.sleep(1)
        print("당신은 80%의 확률로 안좋은 결말에 도달했습니다.")
        GameOver()
        
    else:
        print("\n당신은 길을 따라 걷다 다행히 함정을 제 때 발견해 피해갔습니다.")
        time.sleep(1)

NextScreen()
print("\n갈림길에서 무사히 빠져나간 당신.")
time.sleep(1)
print("언뜻 보면 평범해 보이는 어느 방에 도착했습니다.")
time.sleep(1)
print("왜인지 아무도 여기에 없는 듯 합니다.")
time.sleep(1)
print("대충 둘러보니 이곳은 경비병의 방 같은데 말이죠...")
time.sleep(2)

ans = input("\n쓸만한 아이템을 얻을지도 모르니 한번 살펴볼까요?\n▶ ")
if ans == "예":
    print("\n당신은 책장을 살피기 시작했습니다.\n")
    time.sleep(1)
else:
    print("\n당신은 바로 밖으로 나가기로 했습니다.")
    time.sleep(1)
    print("약간 아쉽지만, 혹시 모를 함정을 피하기 위해서요.")
    time.sleep(1)
    quit()
