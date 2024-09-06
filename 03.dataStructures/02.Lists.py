# dynamic typing 이기에 아무 타입의 값이나 list 에 집어 넣을 수 있다.
list = ["Mon", "Tue", "Wed", "Thur", "Fri", True, 123, [11, 22, 33]]

# length
print(len(list))        # 보통 len() 함수를 많이 사용
print(list.__len__())   # len() 함수가 내부적으로 호출하는 메서드

# element 접근
print(list[0], list[3])
print(list[len(list) - 1])
print(list[len(list) - 1][2])

# element 추가
list.append("Sat")
print(list)
list.append("Sun")
print(list)
list.append(999)
print(list)

# element 삭제
list.remove(999)
print(list)
list.remove("Sun")
print(list)

# list에 해당 element가 몇 개 있는지 return
print(list.count("Fri"))
print(list.count("金"))

# list 거꾸로 뒤집기
list.reverse()
print(list)

# list 속 element 전체 비우기
list.clear()
print(list)