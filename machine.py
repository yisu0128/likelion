a = int(input("금액을 넣어주세요: "))


# menu = {1: "콜라": 500, 2: "커피": 400, 3: "사이다": 300, 4: "율무차": 200}
# menu = {1: 500, 2: 400, 3: 300, 4: 200}

while True:  # 실행이 되는 동안 그냥 실행됨
    menu = {"콜라": 500, "커피": 400, "사이다": 300, "율무차": 200}
    goods = list(menu.keys())
    prices = list(menu.values())

    print("[이화네 음료수]")
    print("현재 금액: " + str(a) + "원")

    for i in range(len(goods)):
        print(i+1, ". ", goods[i], " - ", price[i], "원")

    choice = int(input('음료를 선택해주세요: ')) - 1

    exchange


'''
print(menu)
b = int(input("음료를 선택해주세요: "))
c = int(menu[b])

if a > c:
    e = a-c
    print("잔액은"+" " + "e"+"원" + "입니다.")
    d = input("추가로 구매하시겠습니까?(Y/N) : ")

    if d == "Y":
        a = e


elif a == c:
    print("잔액은 0원 입니다. 이용해주셔서 감사합니다.")

else:
    print("금액이 부족합니다")
'''
