def main():
    x,y = convert()
    p=gauge(x,y)
    if p <= 1:
        print('E')
    else:
        print('F')

def convert():
    f = input('Fraction: ')
    x, y = f.split('/')
    x = int(x)
    y = int(y)
    return x,y


def gauge(x,y):
    try:
        p=(x/y)*100
        
    expect

if __name__=="__main__":
    main()