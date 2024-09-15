# [부모 class]
class Dog:
    def __init__(self, name, color, age):
        self.name   = name
        self.color  = color
        self.age    = age

    def __str__(self):
        return f"Dog : {self.name}, {self.color}, {self.age}"

    def beforeSleep(self):
        print(f"{self.name} ready to sleep...")

    def sleep(self):
        self.beforeSleep() # 이런 식으로 class 내 다른 method 호출 가능
        print(f"{self.name} is sleeping...zzz...")

# [자식 class]
class GuardDog(Dog): # (Dog) --> Dog class 를 상속 받는다. Dog class가 가지고 있는 모든 property 를 상속 받는다.
    def __init__(self, name, color, age):
        # 부모 class의 __init__ method 호출(부모 class의 constructor 호출)
        # super : 부모 class를 의미(Dog class)
        super().__init__(name, color, age)

    def rrrrr(self):
        print("GuardDog bark! bark!")

# [자식 class]
class Puppy(Dog): # (Dog) --> Dog class 를 상속 받는다. Dog class가 가지고 있는 모든 property 를 상속 받는다.
    def __init__(self, name, color, age):
        # 부모 class의 __init__ method 호출(부모 class의 constructor 호출)
        # super : 부모 class를 의미(Dog class)
        super().__init__(name, color, age)

    def woof(self):
        print("Puppy bark! bark!")

# ################### instance 생성 ###################
radder = GuardDog(
    name  = "Radder",
    color = "black",
    age   = 11
)
nepa = Puppy(
    name  = "Nepa",
    color = "white",
    age   = 9
)

# ################### GuardDog instance 출력 ###################
print("=================================")
print(radder)
radder.rrrrr()
radder.sleep()
print("=================================")

# ################### Puppy instance 출력 ###################
print("=================================")
print(nepa)
nepa.woof()
nepa.sleep()
print("=================================")