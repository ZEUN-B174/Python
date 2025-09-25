# 요리 시스템을 담당하는 모듈입니다.
from dataclasses import dataclass

@dataclass
class Food:
    name: str
    recipe: dict # 레시피에 들어가는 최대 재료 가짓수는 4개입니다.
    effects: dict
    quantity: int = 0
    price: int = 0 # 상점에 판매할 시 가격입니다.

@dataclass
class Ingredient:
    name: str
    quantity: int = 0
    price: int = 0 # 상점에서 판매하는 재료만 가격을 추가하세요.

def cook(food: Food, ingredients: dict) -> bool:
    """
    주어진 재료로 음식을 요리합니다.
    재료가 충분하지 않으면 False를 반환합니다.
    """
    for ing_name, req_qty in food.recipe.items():
        if ing_name not in ingredients or ingredients[ing_name].quantity < req_qty:
            return False
    
    for ing_name, req_qty in food.recipe.items():
        ingredients[ing_name].quantity -= req_qty
    
    food.quantity += 1
    return True

def eat(food: Food) -> dict:
    """
    음식을 먹고 효과를 반환합니다.
    음식이 없으면 빈 딕셔너리를 반환합니다.
    """
    if food.quantity <= 0:
        return {}
    
    food.quantity -= 1
    return food.effects

def sell(item, amount: int) -> int:
    """
    아이템(음식 또는 재료)을 판매하고 총 가격을 반환합니다.
    """
    if item.quantity < amount:
        amount = item.quantity
    
    total_price = item.price * amount
    item.quantity -= amount
    return total_price

# 테스트 코드
