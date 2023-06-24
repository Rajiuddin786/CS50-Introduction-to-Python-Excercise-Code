import random
import sys

def take_level():
    try:
        level = int(input('Level: '))
        return level

    except ValueError:
        return -1

def take_guess():
    try:
        guess = int(input('Guess: '))
        return guess

    except ValueError:
        return -1

def check_result(gues,ra):
    while True:
        if gues != ra:
            if gues > ra:
                print('Too Large!')
                return 0
            else:
                print('Too Small!')
                return 0
        else:
            return 1


def main():
    while True:
        level = take_level()
        if level > 0:
            break
    ran = random.randint(1, level)
    while True:
        guess = take_guess()
        if guess > 0:
            break

    while True:
        result = check_result(guess, ran)
        if result == 1:
            break
        else:
            while True:
                guess = take_guess()
                if guess > 0:
                    break


    if result == 1:
        sys.exit('Just Right!')


main()