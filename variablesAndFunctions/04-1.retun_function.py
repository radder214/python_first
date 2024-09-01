# function을 return 하는 방법
# ======== [1] ========
def outer_function(x):
    def inner_function(y):
        return x + y        # inner_function 의 return 값
    return inner_function   # outer_function 의 return 값

result_function = outer_function(10) # inner_function 이 return 됐다.
result = result_function(7)

print(result) # 출력: 17

# ======== [2] ========
# Python에서 return 구문에 함수 자체를 작성하는 것은 불가능
# 하지만 lambda 를 사용해 간단한 익명 함수를 직접 반환할 수 있다.
def make_multiplier(n):
    return lambda x: x * n

returnedFunction = make_multiplier(5) # lambda x: x * n 가 return 됐다.
print(returnedFunction(10)) # 출력: 50