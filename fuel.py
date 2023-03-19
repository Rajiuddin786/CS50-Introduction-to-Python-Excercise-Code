def main():
    try:
        per = check()

    except (ZeroDivisionError, ValueError):
        check()


def check():
    f = input('Fraction: ')
    x, y = f.split('/')
    x = int(x)
    y = int(y)
    p = (x / y) * 100
    if p <= 1:
        print('E')
    elif 99 <= p <= 100:
        print('F')
    elif p > 100:
        return 1 / 0
    else:
        print(f"{p}%")
    return p


main()