def main():
    try:
        per = convert()

    except (ZeroDivisionError, ValueError):
        convert()


def convert():
    f = input('Fraction: ')
    x, y = f.split('/')
    x = int(x)
    y = int(y)
    p=gauge(x,y)
    if p <= 1:
        print('E')
    elif 99 <= p <= 100:
        print('F')
    elif p > 100:
        return 1 / 0
    else:
        print(f"{p}%")
    return p

def gauge(x,y):
    return (x/y)*100
    
if __name__=="__main__":
    main()