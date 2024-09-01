def sayHello(name = "anonymous"): # name parameter에 기본값(anonymous) 설정
    print(f"My name is {name}")

sayHello("Park")
sayHello()

def sayAge(age = 60): # age parameter에 기본값(60) 설정
    print(f"Your age is {age}")

sayAge(20)
sayAge(30)
sayAge()