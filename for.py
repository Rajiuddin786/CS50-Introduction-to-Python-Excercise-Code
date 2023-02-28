def main():
    o=get()
    meow(o)


def get():
    while True:
        n=int(input("What is the number "))
        if n>0:
            return n

def meow(n):
    for i in range(n):
        print("Meow");

main()