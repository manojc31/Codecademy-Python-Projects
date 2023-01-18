alien_colors = ['green', 'blue', 'red', 'brown', 'purple', 'white', 'yellow']

if 'green' in alien_colors:
    price = 25
    print("You earned 25 points")

if 'blue' in alien_colors:
    price_1 = 20
    print("You earned 20 points")

if 'red' in alien_colors:
    price_2 = 1
    print("You earned 1 point")

if 'brown' in alien_colors:
    price_3 = 18
    print("You earned 18 points")

if 'purple' in alien_colors:
    price_4 = 16
    print("You earned 16 points")

if 'white' in alien_colors:
    price_5 = 15
    print("You earned 15 points")

if 'yellow' in alien_colors:
    price_6 = 10
    print("You earned 10 points")

total = price + price_1 + price_2 + price_3 +price_4 + price_5 + price_6
print("\nCongrats you got" + str(total) + "points")
print("\nAlien game is over")