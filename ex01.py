from cookingsystem import *

foods = [Food("파스타", {"밀가루": 2, "토마토소스": 1}, {"체력": 10}, price=50),
         Food("샐러드", {"채소": 3, "올리브오일": 1}, {"체력": 5, "기력": 5}, price=30)]

ingredients = { "밀가루": Ingredient("밀가루", 5, price=10),
                "토마토소스": Ingredient("토마토소스", 2, price=15),
                "채소": Ingredient("채소", 6, price=8),
                "올리브오일": Ingredient("올리브오일", 1, price=12)}

# 요리 시도
print("요리 시도:")
for food in foods:
    if cook(food, ingredients):
        print(f"{food.name} 요리 성공! 현재 수량: {food.quantity}")
    else:
        print(f"{food.name} 요리 실패! 재료 부족.")

# 음식 먹기
print("\n음식 먹기:")
for food in foods:
    effects = eat(food)
    if effects:
        print(f"{food.name} 먹음! 효과: {effects}, 남은 수량: {food.quantity}")
    else:
        print(f"{food.name} 먹기 실패! 음식 없음.")

# 아이템 판매
print("\n아이템 판매:")
for food in foods:
    total_price = sell(food, 1)
    print(f"{food.name} 판매! 총 가격: {total_price}, 남은 수량: {food.quantity}")