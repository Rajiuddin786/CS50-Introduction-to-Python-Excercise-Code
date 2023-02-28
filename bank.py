def main():
    my_input=input("Greeting: ").strip().title()
    check=element_pop(my_input)
    if(check==1):
        print("100$")
    elif(check==0):
        print("20$")
    else:
        print("0$")

def element_pop(p):
    r=0
    h=0
    list_hello=[]
    for i in p:
         list_hello.append(i)

    for i in range(len(list_hello)):
        if(list_hello[0]=='H'):
            h=1
        if(list_hello[0]!='H'):
            r=r+1
        elif(list_hello[1]!='e'):
            r=r+1
        elif(list_hello[2]!='l'):
            r==r+1
        elif(list_hello[3]!='l'):
            r=r+1
        elif(list_hello[4]!='o'):
            r=r+1
        else:
            break
    if(r==5):
        return 1
    if(r<5 and h==1):
        return 0
    if(r==0 and h==0):
        return -1



main()