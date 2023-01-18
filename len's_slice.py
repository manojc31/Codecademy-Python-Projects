from datetime import date
today = date.today()
print(str(today))

toppings = ['pepperoni','pineapple', 'cheese', 'sausage','olives', 'anchories', 'mushrooms']
prices = [2,6,1,3,2,7,2]
pizza = zip(toppings, prices)

length=len(toppings)

print("we sell " + str(length) + " different kinds of pizza")
prices.sort()
print(list(pizza))

cheapest_pizza = (prices[0],toppings[0])
print(cheapest_pizza)

expensice_pizza = (prices[6], toppings[6])
print(expensice_pizza)

three_cheapest = (prices[:3], toppings[:3])
combine = zip(prices[:3], toppings[:3])
print(list(combine))

num_two = prices.count(2)
print(num_two)
