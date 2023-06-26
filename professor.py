import random

def take_level():
    while True:
        try:
            level = int(input('Level: '))
            if level == 0 or level == 4:
                take_level()
            return level
        except ValueError:
            take_level()


def check_answer(a,b,an):
    try:
        ans = int(an)
        if (a+b) ==  ans:
            return 1
        else:
            return 0
    except ValueError:
        return -1

def calculator(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    count = 0
    while True:
        count+=1
        answer = input(f'{x} + {y} = ')
        check = check_answer(x,y,answer)
        if check == 1:
            return 1
        elif check == -1 or check == 0:
            print('EEE')
        if count == 3:
            print(f'{x} + {y} = ',(x+y))
            return 0


def main():
    score = 0
    try:
       level = take_level()
       if level > 0:
        raise ValueError
    except ValueError:
        exit()

    for i in range(9):
        score = score + calculator(level)
    print('Score: ',score)

main()