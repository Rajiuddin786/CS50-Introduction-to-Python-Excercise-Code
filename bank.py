def main():
    hello = input("Greeting: ").strip().title()
    j = check(hello)
    if j == 1:
        print('$0', end='')
    elif j == 0:
        print('$20', end='')
    elif j == -1:
        print('$100', end='')


def check(hello):
    my_list = list(hello)
    lenght = len(my_list)
    r = 0
    h = 0
    for i in range(lenght):
        if i == 0:
            if my_list[0] == 'H':
                r += 1
                h += 1
        elif i == 1:
            if my_list[1] == 'e':
                r += 1
                h += 1
        elif i == 2:
            if my_list[2] == 'l':
                r += 1
                h += 1
        elif i == 3:
            if my_list[3] == 'l':
                r += 1
                h += 1
        elif i == 4:
            if my_list[4] == 'o':
                r += 1
                h += 1
        if i > 5:
            break
    if r == 5:
        return 1
    if r != 5 and h==1:
        return 0
    else:
        return -1

if __name__ == "__main__":
    main()
