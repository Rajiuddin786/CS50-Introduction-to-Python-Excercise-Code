name = input("camelCase: ").strip()
h = ''
s = name
v = ''
for k in name:
    if k.isupper():
        h = k
        p, m = s.split(h)
        v = p + '_' + h.lower() + m
        s = v

for o in name:
    if o.islower():
        print(name,end='')
        break
    else:
        print('snake_case: ',v)
        break
    

