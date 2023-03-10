name = input('Input: ')
s = ''
for i in name:
    if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u' and i != 'A' and 'E' and i != 'O' and i != 'I' and i != 'U':
        s = s + i

print('Output:', s)