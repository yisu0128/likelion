'''터미널 꼭꼭 cd 써서 제대로 된 위치 찾아가기'''
'''
turn = 10
role = "아기 사자"
name = "신이수"

print(str(turn) + "기 " + role + " "+name)

name = "이수"
age = 25

print("안녕하세요. 제 이름은 {}이고, {}살이에요.".format(name, age))  # 순서대로 넣어야함.
print("안녕하세요. 제 이름은 %s이고, %d살이에요" % (name, age))

grade = int(input("점수를 입력하세요: "))
if (grade >= 90):
    print("A학점입니다")
elif (grade >= 70):
    print("B학점입니다")
    print("분발하세요~!")
else:
    print("재수강에 당첨되었습니다")
'''
'''
a = int(input("숫자 a를 입력해주세요 :"))
b = int(input("숫자 b를 입력해주세요 :"))
if int(input("a*b의 값은? :")) == a*b:
    print("정답입니다!")
else:
    print("다시 한 번 생각해보세요.")

babylion = ["김다은", "허윤", "곽은진", "조현영"]
print(babylion[0:2])

color = ["yello", "blue", "white"]
color.append("orange")
print(color)

color.insert(2, "gray")  # 인덱스, 들어갈원소
print(color)

del color[1]
print(color)
x = color.pop()
print(color)
color.remove("yello")
print(color)
'''
likelion10 = {"다윤": "컴공", "도연": "컴공", "혜빈": "사복"}
likelion10["이수"] = "중문"
print(likelion10)

for i in likelion10:
    print(i)
print("끝")
