fruit_input = input('Item: ').title()
fruit = {'Apple': 130, 'Avocado': 50, 'Banana': 110, 'Cantalope': 50, 'Grapes': 90, 'Grapefruit': 60,
         'Honeydew Melon': 50, 'Kiwifruit': 90, 'Lemon': 15, 'Lime': 20, 'Nectarine': 60, 'Orange': 80, 'Peach': 60,
         'Pear': 100, 'Pineapple': 70, 'Plumbs': 50, 'Sweet Cherries': 100, 'Tangerine': 50, 'Watermelon': 80}
for i in fruit:
    if i == fruit_input:
        print('Calories:', fruit[i])
        break