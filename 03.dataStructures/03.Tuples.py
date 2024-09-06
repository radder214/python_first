# tuple은 [대괄호] 대신 (소괄호)로 감싼다.
tuple = ("Mon", "Tue", "Wed", "Thur", "Fri")

# element 접근 방식은 list와 동일
print(tuple[0])
print(tuple[3])
print(tuple[len(tuple) - 1])
print("=======================")
print(tuple[-1])
print(tuple[-2])
print("=======================")

# length 구하는 방식도 동일
print(len(tuple))
print(tuple.__len__())