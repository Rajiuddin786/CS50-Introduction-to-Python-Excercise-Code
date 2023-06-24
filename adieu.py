store = []
try:
    while True:
        name = input('Name: ')
        store = store + [name]

except EOFError:
    c = len(store)
    for i in range(c):
        if c != 1:
            if i == 0:
                print('Adieu, adieu, to',store[0],end=', ')
            elif i == (c-1):
                print('and',store[c-1])

            else:
                print(store[i],end=', ')

        else:
            print('Adieu, adieu, to',store[0])


