# 요리 시스템을 담당하는 모듈입니다.
from dataclasses import dataclass

# 기본적인 요리 게임을 위한 데이터 구조입니다.
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

# 여기부터는 RPG를 겸한 요리 게임을 위한 데이터 구조입니다.
@dataclass
class Monster:
    name: str
    health: int
    attack: int
    defense: int
    speed: int
    experience: int
    loot: dict # 몬스터가 드랍하는 아이템과 확률입니다.

@dataclass
class Player:
    name: str
    health: int
    attack: int
    defense: int
    speed: int
    experience: int
    level: int
    inventory: dict
    gold: int = 0