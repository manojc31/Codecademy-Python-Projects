import random
num = random.randint(1,10)
money = 100
from datetime import date
today = date.today()
print("Today's date:"+ str(today))
print(str(today))

def coin_flip(bet,wage):
    side = random.randint(1,10)
    if bet == "Heads" and side ==1:
        new_total = money + wage
        print(int(wage))
        print("Heads! You won! Your total is now " + str(new_total) + ".")
        return new_total
    elif bet == "Tails" and side ==2:
        new_total = money + wage
        print(int(wage))
        print("Tails! You won! Your total is now " + str(new_total) + ".")
        return new_total
    else:
        new_total = money - wage
        print(int(wage))
        print("You lost! Your total is now " + str(new_total) + ".")
        return new_total

print(coin_flip("Heads", 20))
print(coin_flip("Tails", 20))
print(coin_flip("Tails", 20))
