import sys
import random
from pyfiglet import Figlet

def get_random():
    f = Figlet()
    fonts = f.getFonts()
    return random.choice(fonts)

def font_input():
    text = input('Input: ')
    return text

def output_font(t,fonts):
    f = Figlet(font=fonts)
    print(f.renderText(t))


def main():
    f = Figlet()
    c = 0
    if len(sys.argv) == 1:
        fonts = get_random()
    elif sys.argv[1] == '-f' or sys.argv[1] == '--font':
        for i in f.getFonts():
            if i == sys.argv[2]:
                fonts = i
                c = 1
                break
    if c == 0:
        sys.exit("Not a Valid Font")

    text = font_input()
    output_font(text,fonts)


main()