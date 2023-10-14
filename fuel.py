def main():
    f = input('Fraction: ')
    x,y = convert(f)
    p=gauge(x,y)
    if p <= 1:
        print('E')
    elif 99 <= p <=100:
        print('F')
    else:
        print(f"{int(p)}%")

def convert(f):
    try:
        x, y = f.split('/')
        x = int(x)
        y = int(y)
        return x,y
    except ValueError:
        main()


def gauge(x,y):
    try:
        p=(x/y)*100
        return p;

    except (ZeroDivisionError,TypeError):
        main()

if __name__=="__main__":
    main()