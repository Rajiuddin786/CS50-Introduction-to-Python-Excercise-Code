exp = input('Expression: ').strip()
y = 0
s = ''
x = 0
l = 0
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
                l = 1
                y = y * float(j)
                continue
            if j == '0':
                if x == 0:
                    y = y * 10
                    x = 1
                    continue
                else:
                    l = l * 10

            y = y / l
            l = l * float(j)

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
                    l = l * 10

            y = y % float(j)
            l = l * float(j)
        else:
            print('Invalid Expression')
            break

print(y, end='')