
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
total = 0
while True:
    food = input("Item: ").title()
    h = ''
    for i in food_menu:
        if food == i:
            total = total + food_menu[i]
            print('Total:', total)
            h = i
            break
    if food == '' or h == '':
        break


