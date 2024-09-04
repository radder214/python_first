# random module 중 randint 함수 import
from random import randint
# random module 중 randint, random 함수 import
from random import randint, random
# random module 전체 import
from random import *

# ====== PC가 고른 숫자를 user가 맞춰야 하는 게임 ======
# int(): Integer로 형변환
user_choice = int(input("Choose number : "))
# 1 ~ 50 까지의 숫자 중 하나를 random 선택
pc_choice = randint(1, 50)

if(user_choice == pc_choice):
    print("User won!")
elif(user_choice > pc_choice):
    print("choose Lower Number!")
elif(user_choice < pc_choice):
    print("choose higher Number!")

def printNumbers():
    print(f"your choice is {user_choice}")
    print(f"PC choice is {pc_choice}")

printNumbers()