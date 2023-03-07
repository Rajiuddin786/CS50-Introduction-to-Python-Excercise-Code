name = input("camelCase: ").strip()
h = ''
s = name
v = ''
c = 0
leng = len(name)
for k in name:
    if k.isupper():
        h = k
        p, m = s.split(h)
        v = p + '_' + h.lower() + m
        s = v
    else:
        c += 1

if c == leng:
    print(name,end='')
else:
    print('snake_case: ',v)
