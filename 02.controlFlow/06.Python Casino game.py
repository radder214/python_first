from random import randint

print("Welcome to Python Casino")

# 컴퓨터 군이 1 ~ 50 중 하나를 선택
pc_choice = randint(1, 50)

# user가 이길 때까지 while 문 반복
# cf) 이진탐색 기법으로 숫자를 입력해가면 빨리 맞출 수 있다.
playing = True
while playing:
    user_choice = int(input("Choose number : "))
    if(user_choice == pc_choice):
        print("User won!")
        playing = False
    elif(user_choice > pc_choice):
        print("Lower!")
    elif(user_choice < pc_choice):
        print("Higher!")