import random as 랜덤
import string as 문자열

파일 = open("countrynum.txt", "r", encoding='utf_8')

참 = True

국가_코드 = {}
성별_리스트 = ['남자', '여자', '논바이너리']
데이터 = 파일.read().splitlines()

for 나 in 데이터:
    나라, 숫자 = 나.split(': ')
    국가_코드[나라] = 숫자
파일.close()

def 새로운_국가코드_입력():
    global 국가_코드
    대답 = input("\n등록할 나라 입력 (ㄴ(취소))\n▶ ")
    if 대답 == 'ㄴ':
        return
    elif 대답 in 국가_코드.keys():
        print("그거 이미 있음 ㅋ")
        return
    넣을나라 = 대답
    대답 = input("\n등록할 나라 코드 입력\n▶ ")
    숫자 = 대답
    파일 = open("countrynum.txt", "w", encoding='utf_8')
    국가_코드[넣을나라] = 숫자
    for 나라, 숫자 in 국가_코드.items():
        파일.write(f"{나라}: {숫자}\n")
    파일.close()

def 등록번호_만들기():
    while 참:
        대답 = input("\n캐릭터 등록번호를 만들까요? (ㅇ(예), ㄴ(아니오))\n▶ ")
        if 대답 == 'ㄴ':
            break

        대답 = input("캐릭터의 국적을 입력하세요 (힌트점(국가 코드 보기))\n▶ ")
        if 대답 == '힌트점' or 대답 == 'ㅎㅌㅈ':
            print(국가_코드)
            continue
        elif 대답 not in 국가_코드.keys():
            print("젠장 잘못 입력했잖아")
            continue
        else:
            쓸나라 = 대답

        대답 = input("캐릭터의 성별을 입력하세요 (남자, 여자, 논바이너리)\n▶ ")
        if 대답 not in 성별_리스트:
            print("젠장 잘못 입력했잖아")
            continue 
        성별 = 대답

        등록번호 = 국가_코드[쓸나라] + str(성별_리스트.index(성별) + 1) + "-"

        for 나 in range(6):
            등록번호 += str(랜덤.choice(문자열.ascii_uppercase + 문자열.digits))

        print(f"\n결과: {등록번호}")

while 참:
    대답 = input("\n할 일을 고르세요(1: 등록번호 만들기, 2: 국가 코드 추가하기, 3: 종료): ")
    if 대답 == '1':
        등록번호_만들기()
    elif 대답 == '2':
        print("버그있어서 일단 숙청함")
    elif 대답 == '3':
        break
    else:
        print("젠장 잘못 입력했잖아")
