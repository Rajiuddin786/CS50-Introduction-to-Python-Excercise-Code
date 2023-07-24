import re
import sys

def main():
    print(check(input("Email: ")))

def check(s):
    if email := re.search('^[^@]\w+@[^@]\w+\.[a-z]+$',s,re.IGNORECASE):
        return ("Valid")
    else:
        return ("Invalid")


if __name__ == "__main__":
    main()