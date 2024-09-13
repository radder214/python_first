"""
# class 생성
class Puppy:
    pass # 그냥 지나가라는 의미

# instance 생성
radder = Puppy()

print(radder)
"""
# ======================================================
"""
class Puppy:
    def __init__():
        print("Puppy instance is born")

radder = Puppy()

print(radder)
"""
# ======================================================
class Puppy:
    def __init__(self):
        # class의 기본 값을 세팅하는 곳
        # instance의 데이터를 커스터마이징 할 수 있다. like Java Constructor
        self.name = "Miss You Radder"
        self.age = 12
        self.color = "brown & black"

radder = Puppy()

print(f"{radder.name}, {radder.age}, {radder.color}")