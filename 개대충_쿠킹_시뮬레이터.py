from dataclasses import dataclass
import time

@dataclass
class Recipe:
    name: str
    ingredients: list
    discovered: bool = False

# 레시피에 들어가는 최대 재료 개수는 4개입니다. 아마도?
recipes = [
    Recipe("김치찌개", ["김치", "고기", "두부"]),
    Recipe("스파게티", ["밀가루", "토마토", "채소"]),
    Recipe("샐러드", ["채소", "토마토"]),
    Recipe("볶음밥", ["밥", "계란", "채소"]),
    Recipe("라멘", ["밀가루", "고기", "계란"]),
    Recipe("초밥", ["밥", "생선"]),
    Recipe("피자", ["밀가루", "토마토", "치즈", "고기"]),
    Recipe("칼국수", ["밀가루", "채소", "조개"]),
    Recipe("햄버거", ["밀가루", "고기", "채소", "치즈"]),
    Recipe("샌드위치", ["밀가루", "계란", "채소", "토마토"]),
    Recipe("두부김치", ["두부", "김치"]),
    Recipe("계란찜", ["계란", "채소"]),
    Recipe("오므라이스", ["밥", "계란", "채소", "고기"]),
    Recipe("제육볶음", ["고기", "채소", "양념"]),
    Recipe("두부부침", ["두부", "계란", "밀가루"]),
    Recipe("치즈돈가쓰", ["치즈", "고기", "밀가루", "계란"]),
    Recipe("해물파전", ["밀가루", "조개", "채소"]),
    Recipe("김밥", ["밥", "채소", "계란"]),
    Recipe("생선구이", ["생선"]),
]

ingredients = [
    "김치", "고기", "두부", "밀가루", "토마토", "채소", "밥", "계란", "생선", "치즈", "조개" "양념"
]

# 메인 함수
def main():
    print("개대충 쿠킹 시뮬레이터에 오신 것을 환영한다.")
    time.sleep(1)
    print("님의 목표는 레시피 전부를 알아내는 것임.")
    time.sleep(1)
    print(f"레시피 개수는 총 {len(recipes)}개고, 재료는 한번에 4개까지 넣을 수 있음. 행운을 빈다.")
    time.sleep(1)

    while not all(recipe.discovered for recipe in recipes):
        print("\n1. 진척도 확인\n2. 재료 확인하기\n3. 요리하기\n4. 때려치기")
        action = input("뭐할겨: ")
        if action == "1":
            check_progress()
        elif action == "2":
            show_ingredients()
        elif action == "3":
            cook()
        elif action == "4":
            print("아 안해")
            return
        else:
            print("뭐라는거임?")

    print("\n오? 클리어했네? ㅊㅋ")

def check_progress():
    print("\n현재 발견한 레시피:")
    for recipe in recipes:
        if recipe.discovered:
            print(f"- {recipe.name} (재료: {', '.join(recipe.ingredients)})")
        else:
            print(f"- (미발견)")

def show_ingredients():
    print("\n사용 가능한 재료:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

def cook():
    choice = input("\n그래서 뭐넣을거임: ")
    chosen_ingredients = [ing.strip() for ing in choice.split(",")]
    if any(ing not in ingredients for ing in chosen_ingredients):
        print("그런 재료가 어딨냐?")
        return
    elif len(chosen_ingredients) > 4:
        print("냄비가 넘쳐버렸다...")
        return
    else:
        found_any = False
        for recipe in recipes:
            if sorted(recipe.ingredients) == sorted(chosen_ingredients):
                if recipe.discovered:
                    print(f"{recipe.name}를 만들었다!")
                    return
                recipe.discovered = True
                found_any = True
                print(f"{recipe.name}를 처음으로 만들었다!")
        if not found_any:
            print("망한 요리를 만들어버렸다...")

if __name__ == "__main__":
    main()