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

print('snake_case: ',v)