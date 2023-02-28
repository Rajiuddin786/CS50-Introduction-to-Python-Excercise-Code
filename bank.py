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
    list_hello=[]
    for i in p:
         list_hello.append(i)

    for i in range(len(list_hello)):
          if(list_hello[0]=='H'):
               r=r+1
          elif(list_hello[1]=='e'):
               r=r+1
          elif(list_hello[2]=='l'):
               r==r+1
          elif(list_hello[3]=='l'):
               r=r+1
          elif(list_hello[4]=='o'):
               r=r+1
          else:
               break
    print(r)
    if(r==5):
        return 1
    elif(r<5):
        return 0
    else:
        return -1



main()