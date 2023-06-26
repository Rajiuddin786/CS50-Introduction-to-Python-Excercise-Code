import random

def get_level():
    while True:
        level = input("Level: ")
        if level in ['1', '2', '3']:
            return int(level)

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level. Level must be 1, 2, or 3.")

def solve_problem(problem):
    x, y = problem
    correct_answer = x + y
    tries = 0

    while tries < 3:
        answer = input(f"{x} + {y} = ")
        try:
            answer = int(answer)
            if answer == correct_answer:
                return True
            else:
                print("EEE")
                tries += 1
        except ValueError:
            print("EEE")
            tries += 1

    print(f"{x} + {y} = {correct_answer}")
    return False

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        problem = (x, y)

        if solve_problem(problem):
            score += 1

    print(f"Score: {score}")

if __name__ == "__main__":
    main()
