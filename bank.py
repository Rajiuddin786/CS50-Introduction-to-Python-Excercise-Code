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
        element=list_hello.pop(i)
        check_hello(element)


def check_hello(collect):
    r=0
    if(collect=='H'):
        r+=1
    elif(collect=='e'):
        r+=1
    elif(collect=='l'):
        r+=1
    elif(collect=='l'):
        r+=1
    elif(collect=='o'):
        r+=1
    elif(collect==' '):
        
