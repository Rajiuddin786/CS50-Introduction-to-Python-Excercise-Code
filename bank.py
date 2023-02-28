def main():
    h=input("Greeting: ").strip().title()
    check=poping(h)
    if(h=='Hello'):
        print("0$")
    elif(check==0):
        print("20$")
    else:
        print("100$")

def poping(p):
    r=0
    length=p.len()
    for i in range(length):
        element=[p.pop(i)]

    while True:
        if(element[r]==H):
            if(element[r+1]!=e):
                if(element[r+2]!=l):
                    if(element[r+3]!=l):
                        if(element[r+4]!=o):
                            return 0
        else:
            return 1
main()