'''
import random
import time


while True:
    print(random.choice(["된장찌개", "치킨", "라면", "감자튀김"]))
    time.sleep(1)
    break

lunch = random.choice(["된장찌개", "치킨", "라면", "감자튀김"])
print(lunch)

information = {'고향': '수원', '취미': '영화관람', '좋아하는 음식': '국수'}
print(information)

print(information.get("취미"))

# 특기 피아노 사는곳 서울

info1 = {'특기': '피아노', '사는 곳': '서울'}
print(info1.get('특기'))
print(info1.get('사는 곳'))
'''

information = {'고향': '수원', '취미': '영화관람', '좋아하는 음식': '국수'}
foods = ['된장찌개', '피자', '제육볶음']

# 딕셔너리
print(information.get('취미'))
information['특기'] = '피아노'
information['사는곳'] = '서울'
print(information)
del information["좋아하는 음식"]
print(information)
print(len(information))
information.clear()
print(information)

# 리스트
print(foods[1])
print(foods[-1])
foods.append('김밥')
del foods[1]
print(foods)
