from validator_collection import validators,checkers

def main():
    print(validate(input("What's your email: ")))

def validate(s):
    if checkers.is_email(s):
        return f"Valid"
    else:
        return f"Invalid"

if __name__ == "__main__":
    main()