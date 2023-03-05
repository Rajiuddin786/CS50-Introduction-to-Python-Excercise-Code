exp = input('Expression: ').strip()
y = 0
s = ''
for i in exp:
    if i == '+' or i == '-' or i == '*' or i == '/' or i == '%':
        s = i
        break

for j in exp:
    if j == '+' or j == '-' or j == '*' or j == '/' or j == '%' or j==' ':
        continue
    else:
        if s == '+':
            y = y + float(j)
        elif s == '-':
            if y == 0:
                y=y+float(j)
            else:
                y=y-float(j)
        elif s == '*':
            y = 1
            y = y * float(j)
        elif s == '/':
            if y == 0:
                y = 1
                y = y * float(j)
                continue
            y = y / float(j)

        elif s == '%':
            if y == 0:
                y = 1
                y = y * float(j)
                continue
            y = y % float(j)
        else:
            print('Invalid Expression')
            break

print(y, end='')