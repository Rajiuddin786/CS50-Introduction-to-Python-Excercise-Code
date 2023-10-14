def main():
    f = input('Fraction: ')
    x,y = convert(f)
    p=gauge(x,y)
    if p <= 1:
        print('E')
    if :
        print('F')

def convert(f):
    x, y = f.split('/')
    x = int(x)
    y = int(y)
    return x,y


def gauge(x,y):
    try:
        p=(x/y)*100
        return p;

    except (ZeroDivisionError,TypeError):
        convert()

if __name__=="__main__":
    main()