money = int(input("금액을 넣어주세요: "))

while True:
    menu = {"콜라": 500, "커피": 400, "사이다": 300, "율무차": 200}
    goods = list(menu.keys())
    prices = list(menu.values())

    print("[이화네 음료수]")
    print("현재 금액 :" + str(money) + "원")

    for i in range(len(goods)):
        # 이부분 identation 잘 맞추기 #+쓰지말기 / list[index number]꼭 기억하기
        print(i+1, ". ", goods[i], " - ", prices[i], "원")

    select = int(input("음료를 선택해주세요: ")) - 1
    change = money - prices[select]  # 인덱스설정!

    if change < 0:
        print("금액이 부족합니다")
        break
    elif change == 0:
        print("잔액은 0원입니다. 이용해주셔서 감사합니다.")
        break
    else:
        print("잔액은 ", change, "원입니다.")
        ask = input("추가로 구매하시겠습니까? (Y/N): ")

        if ask == 'Y' or ask == 'y':
            money = change  # 앞으로 초기화하기 위해서는 money 에 change 대입과정 필요
            continue
        else:
            break
