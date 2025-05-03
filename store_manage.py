item_list = { "커피": 7, "펜": 3, "종이컵": 2, "우유": 1, "콜라": 4, "책": 5 }
item = ''

def get_item_name(): # 아이템 이름 입력 함수
    global item
    item = ''
    while item not in item_list.keys():
        item = input("\n물건의 이름을 입력하세요(0: 물건 리스트 보기, q: 취소): ")
        if item == 'q':
            break
        elif item == '0':
            print(item_list.keys())
        elif item not in item_list.keys():
            print("존재하지 않는 상품입니다. 다시 입력해 주세요.")

# 메인
while True:
    menu = input("\n할 일을 고르세요.\n(1: 재고확인, 2: 제품 입고, 3: 제품 출고, 4: 새 물건 추가, 5: 물건 삭제, q: 종료): ")

    # 1: 물건 재고 확인
    if menu == '1':
        item = ''
        while item not in item_list.keys():
            item = input("\n물건의 이름을 입력하세요(0: 물건 리스트 보기, q: 취소, all: 전부 보기): ")
            if item == 'q' or item == 'all':
                break
            elif item == '0':
                print(item_list.keys())
            elif item not in item_list.keys():
                print("존재하지 않는 상품입니다. 다시 입력해 주세요.")

        if item == 'q':
            continue
        elif item == 'all':
            print(item_list)
        else:
            print(item + '의 재고는 ' + str(item_list[item]) + '개 입니다.')

    # 2: 물건 입고하기
    elif menu == '2':
        get_item_name()

        if item == 'q':
            continue
        else:
            amount = int(input(f"입고할 {item}의 수량을 입력하세요: "))
            item_list[item] += amount
            print(item + '의 재고는 ' + str(item_list[item]) + '개 입니다.')

    # 3: 물건 출고하기
    elif menu == '3':
        get_item_name()

        if item == 'q':
            continue
        else:
            amount = input(f"출고할 {item}의 수량을 입력하세요(all: 전부 출고): ")
            if amount =='all':
                item_list[item] = 0
            else:
                amount = int(amount)
                item_list[item] = max(item_list[item] - amount, 0)
            print(item + '의 재고는 ' + str(item_list[item]) + '개 입니다.')

    # 4: 물건 새로 들여오기
    elif menu == '4':
        item = input("새로 들여올 물건의 이름을 입력하세요(q: 취소): ")

        if item == 'q':
            continue

        elif item in item_list.keys():
            while item in item_list.keys():
                item = input("이미 입고된 제품입니다. 다시 입력해 주세요(q: 취소): ")
                if item == 'q':
                    break
        
        if item == 'q':
            continue

        else:
            amount = int(input("몇 개를 입고하시겠습니까: "))
            item_list[item] = amount
            print(item + '의 재고는 ' + str(item_list[item]) + '개 입니다.')

    # 5: 물건 그만 들여오기
    elif menu == '5':
        item = input("그만 들여올 물건의 이름을 입력하세요(q: 취소): ")

        if item == 'q':
            continue

        elif item not in item_list.keys():
            while item not in item_list.keys():
                item = input("존재하지 않는 상품입니다. 다시 입력해 주세요(q: 취소): ")
                if item == 'q':
                    break
        
        if item == 'q':
            continue

        else:
            del item_list[item]
            print(item + '(을)를 재고에서 삭제했습니다.')

    # 종료하기
    elif menu == 'q':
        break

    # 오류 메시지
    else:
        print("1, 2, 3, 4, 5, q 중 하나의 문자로 다시 입력해주세요.")
        continue

print("\n편의점 재고관리 시스템을 종료합니다.")