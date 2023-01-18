toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]

num_pizza = len(toppings)
print("we sell " + str(num_pizza) + " different kinds of pizza!")

pizza = zip(prices, toppings)
prices.sort()
print(list(pizza))
cheapest_pizza =  (prices[0],toppings[0])
priciest_pizza = (prices[-1],toppings[0])
three_cheapest = (prices[:3],toppings[:3])
num_two_dollar_slices = prices.count(2)

print(cheapest_pizza)
print(priciest_pizza)
print(three_cheapest)
print(num_two_dollar_slices)
