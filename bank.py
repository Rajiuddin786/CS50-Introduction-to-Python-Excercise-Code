def main():
    h=input("Greeting: ").strip().title()
    check=poping(h)
    if(check==1):
        print("0$")
    elif(check==0):
        print("20$")
    else:
        print("100$")

def poping(p):
    r=0
    length=len(p)#Finding the length of the string
    list_hello=list(p)
    for i in range(length-1):
        element=[list_hello.pop(i)]
        if(element[0]==H):
            r+=1
        elif(element[1]==e):
            r+=1
        elif(element[2]==l):
            r+=1
        elif(element[3]==l):
            r+=1
        elif(element[4]==o):
              r+=1

    if(r==5):
        return 1
    elif(r<5):
        return 0
    else:
        return -1

main()