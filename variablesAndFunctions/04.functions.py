# function을 만들 때 맨 앞에 'def' 라는 키워드 사용
# 애초에 function 이라는 키워드 자체가 없다.

def say_hello():                # 마지막에 콜론(:)이 반드시 붙어야한다.
    print("hello I'm function") # 반드시 들여쓰기를 해야한다. 안하면 오류 발생
                                # 들여쓰기 --> say_hello 함수의 block(범위) 안에 print("hello I'm function") 이 들어있다.
                                # {중괄호}는 없어도 된다.
say_hello()