import sys
import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if macthes := re.search(r"^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$",ip):
        number = ip.split('.')
        if all(0 <= int(digit) <= 255 for digit in number):
            return(True)
        else:
            return(False)
    else:
        return(False)

if __name__ == "__main__":
    main()