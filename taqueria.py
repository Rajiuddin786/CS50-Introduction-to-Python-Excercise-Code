def main():
    food_menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00}

    try:
        fo = error_hand(food_menu)

    except EOFError:
        pass


def error_hand(f):
    total = 0
    while True:
        food = input("Item: ").title()
        if food == "":
            break
        for i in f:
            if food == i:
                total = total + f[i]
                print(f"${total}",sep='')
                break

    return food


main()


