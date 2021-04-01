import sys


def is_natural_number(s):
    try:
        int(float(s))
    except ValueError:
        return False
    else:
        if int(float(s)) <= 0:
            return False
        else:
            return True


args = sys.argv

if len(args) == 1:
    print('第一引数に入れた数字の数までFizzBuzzを判定するスクリプト')
    sys.exit()

if len(args) != 2:
    print('引数が不正です')
    sys.exit()

if (not is_natural_number(args[1])):
    print('引数が自然数ではありません')
    sys.exit()

rng = int(float(args[1]))

for i in range(1, rng+1):
    if i % 15 == 0:
        print('Fizz Buzz!!!')
    elif i % 5 == 0:
        print('Buzz!')
    elif i % 3 == 0:
        print('Fizz!')
    else:
        print(i)
