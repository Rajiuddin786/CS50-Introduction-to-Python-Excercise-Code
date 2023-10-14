def main():
    hello = input("Greeting: ").strip().title()
    print(f"{check(hello)}")

def value(hello):
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
        return f"$0"
    if r != 5 and h==1:
        return f"$20"
    else:
        return f"$0"

if __name__ == "__main__":
    main()
