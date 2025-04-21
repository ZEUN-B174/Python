import random

CharacterList_4star = ["치욘", "글리치", "디리겐트", "만수르", "크로네", "데스데이", "졸리 로저", "디나",  "모노", "쿠르디", "히얍", "네로", "마키", "라메라"]
CharacterList_5star = ["그리즐리", "피안", "잔나", "오시리스", "루파나", "란디", "카와", "자포냐", "메루", "살라딘"]
CharacterList_6star = ["아비아", "레이븐", "올랭피아", "바흐람", "라하브", "람다", "이블리스", "클레오"]

while True:
    answer = int(input("몇번 뽑을까요?: "))
    
    for i in range(answer):
        dice = random.randint(1, 100)
        if dice == 51:
            Character = CharacterList_6star[random.randrange(len(CharacterList_6star))]
            print(f"★6 {Character}(을)를 뽑았습니다!")
        elif dice > 95:
            Character = CharacterList_5star[random.randrange(len(CharacterList_5star))]
            print(f"★5 {Character}(을)를 뽑았습니다!")
        elif dice <= 10:
            Character = CharacterList_4star[random.randrange(len(CharacterList_4star))]
            print(f"★4 {Character}(을)를 뽑았습니다.")
        else:
            Character = "무기"
            print(f"★3 {Character}(을)를 뽑았습니다.")

    answer = input("계속할까요?: ")
    if answer == "quit":
        break