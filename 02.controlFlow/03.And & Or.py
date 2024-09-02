# ===== 아래 3개 함수는 모두 Python 내장 함수 =====
# 1. input() 함수
    # 사용자로부터 입력을 받을 때 사용되는 함수
    # 사용자가 입력한 값을 항상 '문자열로 반환'한다.
    # '오직 1개'의 argument만 받는다.(필수 X)
        # 사용자에게 입력을 유도하기 위해 출력되는 문자열
        # argument는 화면에만 표시될 뿐 아무런 영향을 미치지 않는다.

# 2. type() 함수(Python 내장 함수)
    # 객체의 데이터 타입(자료형)을 확인할 때 사용하는 내장 함수
print(type(10))         # 출력 : <class 'int'>
print(type(3.14))       # 출력 : <class 'float'>
print(type("Hello"))    # 출력 : <class 'str'>
print(type([1, 2, 3]))  # 출력 : <class 'list'>

# 3. int()
    # Integer 타입으로 형변환

age = int(input("your age? ")) # 사용자 입력값(return 값)이 age 변수에 할당
print(f"my age is {age}")
print(type(age))

if age < 18:
    print("You can't drink")
elif age >= 18 and age <= 35: # and = &&
    print("You drink beer")
elif age == 60 or age == 70:  # or = ||
    print("Birthday party")
else:
    print("Go ahead")