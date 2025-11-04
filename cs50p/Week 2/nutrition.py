fruits = [
    {"apple":130},
    {"avocado":50},
    {"banana":110},
    {"grapefruit":60},
    {"cantaloupe":50},
    {"grapes":90},
    {"honeydew melon": 50},
    {"kiwifruit": 90},
    {"lemon":15},
    {"nectarine":60},
    {"lime":20},
    {"orange":80},
    {"peach":60},
    {"pineapple":50},
    {"pear":100},
    {"plums":70},
    {"strawberries":50},
    {"sweet cherries":100},
    {"tangerine":50},
    {"watermelon":80}

]

inp = input("Item: ").lower()
for fruit in fruits:
    if inp in fruit:
        print(f"Calories: {fruit[inp]}")
