# ############ class 생성 ############
class Puppy:
    def __init__(self, name, age, color):
        self.name   = name  # radder.name   = name  / nepa.name   = name  --> 이런 의미라고 생각하면 된다.
        self.age    = age   # radder.age    = age   / nepa.age    = age   --> 이런 의미라고 생각하면 된다.
        self.color  = color # radder.color  = color / nepa.color  = color --> 이런 의미라고 생각하면 된다.

    # java의 toString() method 같은 역할
    # return(출력) 하고 싶은 문자를 작성해주면 된다.
    def __str__(self): # 모든 method 의 첫 번째 argument 는 self 여야 한다.
        return f"__str__ : {self.name}, {self.age}, {self.color}"

# ############ instance 생성 및 초기화 ############
radder  = Puppy("Radder", 11, "brown & black")  # self = radder
nepa    = Puppy("Nepa"  ,  9, "brown & white")  # self = nepa
# 아래와 같은 식으로도 instance 생성 가능
# 이렇게 하면 굳이 argument 순서를 지킬 필요가 없다.
wendy   = Puppy(
    age   = 12,
    color = "snow",
    name  = "Wendy"
)

# ############ instance 속성 출력 ############
print(f"radder  : {radder.name}, {radder.age}, {radder.color}")
print(f"nepa    : {nepa.name}, {nepa.age}, {nepa.color}")
print(f"wendy   : {wendy.name}, {wendy.age}, {wendy.color}")

# ############# __str__ #############
# instance 전체를 출력하려고 할 때 자동으로 __str__ method 가 호출된다.
# 따로 __str__ method 를 호출할 필요가 없다.
print(radder)
print(nepa)
print(wendy)