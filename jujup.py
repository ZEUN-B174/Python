print("개 쓸데없는 주접문을 만들어 드립니다.")

while 1:
    ans = input("\n여기서 뭐 할지 골라주세요. (1. 캐릭터 주접문 만들기 2, 종료하기) ")
    
    if ans == "2":
        break
    name = input("\n캐릭터의 이름은..? ")
    country = input("그리고 캐릭터의 국적/출신은..? ")
    addition = input("마지막으로 캐릭터의 직업/애칭(ex 귀요미)은..? ")

    print(f"\n혹시 그거 아나요..? {name}(은)는 정말 사랑스러운 {country}의 {addition}(이)라는 사실을요...")