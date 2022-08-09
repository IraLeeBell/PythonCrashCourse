favorite_fruits = ['apples', 'bananas', 'strawberries']

fruit = 'bananas'
if fruit in favorite_fruits:
    print(f"\nYou really like {fruit}!")

fruit = 'apples'
if fruit in favorite_fruits:
    print(f"\nYou really like {fruit}!")

fruit = 'strawberries'
if fruit in favorite_fruits:
    print(f"\nYou really like {fruit}!")

fruit = 'grapefruits'
if fruit in favorite_fruits:
    print(f"\nYou really like {fruit}!")
else:
    print(f"\n{fruit.title()} aren't something you like.")

fruit = 'pears'
if fruit in favorite_fruits:
    print(f"\nYou really like {fruit}!")
else:
    print(f"\n{fruit.title()} aren't a fruit you typically like.")

