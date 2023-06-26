import random

def take_level():
    while True:
        try:
            level = int(input('Level: '))
            if level == 0 or level > 3:
                raise ValueError
            return level
        except ValueError:
            print("Invalid input. Please enter a valid level (1, 2, or 3).")

def check_answer(a, b, ans):
    try:
        answer = int(ans)
        if a + b == answer:
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
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    else:
        raise ValueError('Invalid Input')
    count = 0
    while True:
        count += 1
        answer = input(f'{x} + {y} = ')
        check = check_answer(x, y, answer)
        if check == 1:
            return 1
        elif check == -1 or check == 0:
            print('EEE')
        if count == 3:
            print(f'{x} + {y} = {(x + y)}')
            return 0

def main():
    score = 0
    level = take_level()
    for i in range(10):  # Changed the range from 9 to 10
        score += calculator(level)
    print('Score:', score)

main()

