exp = input('Expression: ').strip()
y = 0
s = ''
x = 0
t = 0
u = 0
for i in exp:
    if i == '+' or i == '-' or i == '*' or i == '/' or i == '%':
        s = i
        break

for j in exp:
    if j == '+' or j == '-' or j == '*' or j == '/' or j == '%' or j == ' ':
        continue
    else:
        if s == '+':
            y = y + float(j)
        elif s == '-':
            if y == 0:
                y = y + float(j)
            else:
                y = y - float(j)
        elif s == '*':
            if y == 0:
                y = 1
            y = y * float(j)
        elif s == '/':
            if y == 0:
                y = 1
                t = 1
                y = y * float(j)
                continue
            if j == '0':
                if x == 0:
                    y = y * 10
                    x = 1
                    continue
                else:
                    t = t * 10
                    y = y / t
                    t = t * float(j)
                    u = 1

            if u == 0:
                t = t * float(j)
                y = y / t



        elif s == '%':
            if y == 0:
                y = 1
                y = y * float(j)
                continue
            if j == '0':
                if x == 0:
                    y = y * 10
                    x = 1
                    continue
                else:
                    t = t * 10

            y = y % float(j)
            t = t * float(j)
        else:
            print('Invalid Expression')
            break

print(y, end='')