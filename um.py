import re
import sys

def main():
    print(count(input('Text: ')))

def count(s):
    count = 0
    count_um = re.findall('\(um)',s,re.IGNORECASE)
    for _ in count_um:
        count+=1
    return count

if __name__ == "__main__":
    main()