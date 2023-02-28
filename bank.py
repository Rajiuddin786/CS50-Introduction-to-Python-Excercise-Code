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
    length=len(p)#Finding the length of the string
    list_hello=list(p)
    for i in range(length):
        element=[list_hello.pop(i)]
        if(element[i]==H):
            r+=1
        elif(element[i]!=e):
            r+=1
        elif(element[i]!=l):
            r+=1
        elif(element[i]!=l):
            r+=1
        elif(element[i]!=o):
              r+=1
        else:
            return 1
main()

