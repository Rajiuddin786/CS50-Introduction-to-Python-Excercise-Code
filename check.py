def element_pop(p):
    r=0
    list_hello=[]
    length=len(p)#Finding the length of the string
    #string to list
    for i in p:
         list_hello.append(i)

    if(list_hello[0]=='H'):
            r+=1
    elif(list_hello[1]=='e'):
              r+=1
    elif(list_hello[2]=='l'):
              r+=1
    elif(list_hello[3]=='l'):
             r+=1
    elif(list_hello[4]=='o'):
            r+=1
    print(r)

element_pop('hello')