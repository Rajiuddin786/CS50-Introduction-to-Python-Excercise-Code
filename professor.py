import random

def take_level():
    while True:
        try:
            level = int(input('Level: '))
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

def calculator():

    x = random.randint(1, 10)
    y = random.randint(1, 10)
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
       if level != 1 or level != 2 or level != 3:
        raise ValueError
    except ValueError:
        exit()

    for i in range(9):
        score = score + calculator()
    print('Score: ',score)

main()