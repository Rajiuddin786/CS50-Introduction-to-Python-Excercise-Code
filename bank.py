def main():
    my_input=input("Greeting: ").strip().title()
    check=element_pop(my_input)
    if(check==1):
        print("0$")
    elif(check==0):
        print("20$")
    else:
        print("100$")

def element_pop(p):
    r=0
    length=len(p)#Finding the length of the string
    list_hello=list(p)#string to list
    for i in range(length-1):
        element[l]=list_hello.pop(i)
    if(element[0]=='H'):
            r+=1
    elif(element[1]=='e'):
              r+=1
    elif(element[2]=='l'):
              r+=1
    elif(element[3]=='l'):
             r+=1
    elif(element[4]=='o'):
              r+=1

    if(r==5):
        return 1
    elif(r<5):
        return 0
    else:
        return -1


main()