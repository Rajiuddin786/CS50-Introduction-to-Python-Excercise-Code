def main():
    t = input('What time is it? ').strip()
    ho=convert(t)

    if 7 <= ho <= 8:
        print('breakfast time', end='')
    elif 12 <= ho <= 14:
        print('lunch time', end='')
    elif 18 <= ho <= 21:
        print('dinner time', end='')
    else:
        print('', end='')


def convert(time):
    h , m = time.split(':')

    mi = int(m) / 60
    hor = int(h) + mi
    return hor


if __name__=="__main__":
    main()
