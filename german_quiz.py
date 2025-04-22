score = 0

german_words = {
    "Apfel": "사과",
    "Buch": "책",
    "Haus": "집",
    "Katze": "고양이",
    "Hund": "개",
    "Auto": "자동차",
    "Tisch": "책상",
    "Stuhl": "의자",
    "Fenster": "창문",
    "Tür": "문"}

print("독일어 단어 퀴즈에 오신 것을 환영합니다!")
print("각 독일어 단어의 한국어 뜻을 맞춰보세요.")

# 단어를 정렬하여 퀴즈 진행
for word in sorted(german_words.keys()):
    answer = input(f"'{word}'는 한국어로 하면 무슨 뜻일까요? ")
    if answer == german_words[word]:
        score += 1
        print("정답입니다!")
    else:
        print(f"틀렸습니다. '{word}'의 한국어 뜻은 '{german_words[word]}'입니다.")
print(f"퀴즈가 끝났습니다. 당신의 점수는 {score}점입니다.")