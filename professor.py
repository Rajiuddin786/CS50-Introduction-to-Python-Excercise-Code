import random

def get_level():
    while True:
        level = input('Level: ')
        if level in ['1','2','3']:
            return level

def generate_level(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError('Invalid Input')

def take_answer(a,b,c):
    while True:
        try:
            ans = int(input(f'{a} + {b} = '))
            if (a+b) == ans:
                return 1
            else:
                c+=1
                print('EEE')
                if c == 3:
                    return 0


        except ValueError:
            c+=1
            print('EEE')
            if c == 3:
                return 0


def main():
    score = 0
    level = int(get_level())

    for i in range(10):
        x = generate_level(level)
        y = generate_level(level)
        return_value = take_answer(x,y,0)
        if return_value == 0:
            print(f'{x} + {y} = {x+y}')
        else:
            score = score + return_value

    print(f'Score: {score}')

if __name__ == '__main__':
    main()