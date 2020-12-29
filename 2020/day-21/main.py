
import re

#with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-21//example.txt') as f:
with open('c:/Users/josip.grgic/source/repos/AdventOfCode2020/day-21//input.txt') as f:
    lines = [line.rstrip() for line in f]

ingredient_in_food_lookup = {}
allergens_lookup = {}
resolved_ingredients = {}
resolved_allergens = {}
ingredients_set = set() 


for line in lines:
    [ingredients_str, allergens_str] = re.match(r"(.*) \(contains (.*)\)", line).groups()
    ingredients = ingredients_str.split(' ')
    allergens = allergens_str.split(', ')

    for allergen in allergens:
        if allergen not in allergens_lookup:
            allergens_lookup[allergen] = []

        allergens_lookup[allergen].append(ingredients)

    for i in ingredients:
        ingredients_set.add(i)

        if i not in ingredient_in_food_lookup:
            ingredient_in_food_lookup[i] = 1
        else:
            ingredient_in_food_lookup[i] += 1

print (allergens_lookup)

def part_one():
    changed = True
    while changed:
        changed = False

        for (allergen, possible_ingredients) in allergens_lookup.items():
            if allergen in resolved_allergens:
                continue

            new = []
            occurrance_dict = {}

            ingredients_survived = 0

            for single_food_possible_ingredients in possible_ingredients:
                for i in single_food_possible_ingredients:
                    if i not in occurrance_dict:
                        occurrance_dict[i] = 1
                    else:
                        occurrance_dict[i] += 1

            for single_food_possible_ingredients in possible_ingredients:
                arr = []
                for i in single_food_possible_ingredients:
                    # if ingredient not in every food
                    if occurrance_dict[i] < len(possible_ingredients):
                        changed = True
                        continue
                    # if ingredient already resolved
                    if i in resolved_ingredients:
                        changed = True
                        continue

                    ingredients_survived +=1
                    arr.append(i)

                new.append(arr)

            if ingredients_survived == len(possible_ingredients):
                changed = True
                ingredient = new[0][0]
                resolved_ingredients[ingredient] = allergen
                resolved_allergens[allergen] = ingredient

            allergens_lookup[allergen] = new

    resolved_or_possible_ingredients = set()
    
    for (allergen, possible_ingredients) in allergens_lookup.items():
        for single_food_possible_ingredients in possible_ingredients:
            for i in single_food_possible_ingredients:
                resolved_or_possible_ingredients.add(i)

    
    
    result = 0

    for i in ingredients_set:
        if i not in resolved_or_possible_ingredients:
            result += ingredient_in_food_lookup[i]

    print(result)

    allergens_keys = list(resolved_allergens.keys())
    allergens_keys.sort()

    ingredients_list = []

    for a in allergens_keys:
        ingredients_list.append(resolved_allergens[a])

    print(','.join(ingredients_list))

part_one()

def part_two():
    pass


