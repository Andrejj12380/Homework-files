import os
from pprint import pprint

FILE_NAME = 'recipes.txt'
FILE_PATH = os.path.join(os.getcwd(), FILE_NAME)

cook_book = {}


def book():
    with open(FILE_PATH, encoding='utf-8') as file:
        for line in file:
            ingredients = []
            cook_book[line.strip()] = ingredients
            number_of_ingredients = int(file.readline().strip())
            for i in range(number_of_ingredients):
                ingredients_dict = {}
                ingredients.append(ingredients_dict)
                ingredient = file.readline().strip().split('|')
                ingredients_dict.setdefault('ingredient_name', ingredient[0])
                ingredients_dict.setdefault('quantity', ingredient[1])
                ingredients_dict.setdefault('measure', ingredient[2])
            file.readline().strip()
    return cook_book


book()
pprint(cook_book)


ingredients_dict = {}


def necessary_ingredients(dishes_name, person_number):
    for dish in dishes_name:
        dish = str(dish).lower()
        if dish in str(cook_book.keys()).lower():
            for i in range(len(cook_book[dish.capitalize()])):
                quantity = int(cook_book[dish.capitalize()][i]['quantity']) * person_number
                if cook_book[dish.capitalize()][i]['ingredient_name'].strip() in ingredients_dict.keys():
                    ingredients_dict[cook_book[dish.capitalize()][i]['ingredient_name'].strip()] = \
                        {'measure': cook_book[dish.capitalize()][i]['measure'],
                         'quantity': quantity + ingredients_dict[cook_book[dish.\
                             capitalize()][i]['ingredient_name'].strip()]['quantity']}
                else:
                    ingredients_dict[cook_book[dish.capitalize()][i]['ingredient_name'].strip()] = \
                        {'measure': cook_book[dish.capitalize()][i]['measure'].strip(),
                         'quantity': quantity}

        else:
            return print('Такого блюда нет в книге')
    return ingredients_dict


necessary_ingredients(['Омлет', 'блины'], 2)
pprint(ingredients_dict)
