# >>>>>>>>>>>>>>> 부모 class
class Dog:
    def __init__(self, name, color, age):
        self.name   = name
        self.color  = color
        self.age    = age

    def __str__(self):
        return f"Dog : {self.name}, {self.color}, {self.age}"
    
    def sleep(self):
        print(f"{self.name} is sleeping...zzz...")

# >>>>>>>>>>>>>>> 자식 class, (Dog) --> Dog class를 상속 받는다.
class GuardDog(Dog):
    def __init__(self, name, color, age):
        super().__init__(name, color, age) # 부모 class의 생성자 호출

    def rrrrr(self):
        print("stay away...")

# >>>>>>>>>>>>>>> 자식 class, (Dog) --> Dog class를 상속 받는다.
class Puppy(Dog):
    def __init__(self, name, color, age):
        super().__init__(name, color, age) # 부모 class의 생성자 호출

    def wolf(self):
        print("wolf wolf!!!")

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

# ################### instance 출력 ###################
print(radder)
radder.rrrrr()
radder.sleep()

print(nepa)
nepa.wolf()
nepa.sleep()