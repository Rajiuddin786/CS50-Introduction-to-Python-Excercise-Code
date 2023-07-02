def main():
    name = input('Input: ')
    output = shorten(name)
    print('Output:',output)

def shorten(name):
    s = ''
    for i in name:
        if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u' and i != 'A' and 'E' and i != 'O' and i != 'I' and i != 'U':
            s = s + i
    return s

if __name__ == "__main__":
    main()