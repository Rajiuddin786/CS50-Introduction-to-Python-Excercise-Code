import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    short = re.search(r"^.+\"(https|http)://(?:www\.)?youtube\.com/embed(/\w+)(?:.+<.+>)$",s)
    if short:
        return_data = ("https://youtu.be"+short.group(2)).strip()
        return return_data

if __name__ == "__main__":
    main()