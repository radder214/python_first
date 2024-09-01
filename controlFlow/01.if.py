if (10 > 5): # (괄호)가 반드시 있을 필요는 없다.
    print('Correct1!')

if (10 >= 9):
    print('Correct2!')

if (10 == 10):
    print('Correct3!')

if 10 == 9 or 2 >= 1:
    print('Correct4!')

if 10 == 9 and 2 >= 1:
    print('Correct5!') # and 조건을 만족 못 했기에 출력 안 됨

num = 9
if num == 9:
    print('Correct6!')

name = "fire"
if name == "water":
    print('Correct7!')
else:
    print('Error!')