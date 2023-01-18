def ground_shipping(weight):
    if weight <= 2:
        cost_per_weight = 1.5

    elif weight > 2 and weight <= 6:
        cost_per_weight = 3

    elif weight > 6 and weight <= 10:
        cost_per_weight = 4

    elif weight > 10:
        cost_per_weight = 4.75

    cost = cost_per_weight * weight + 20
    return cost

def drone_shipping(weight):
    if weight <= 2:
        cost = weight * 4.5
    elif weight > 2 and weight <= 6:
        cost = weight * 9
    elif weight > 6 and weight <=10:
        cost = weight * 12
    elif weight > 10:
        cost = weight * 14.25
    return cost


def cheapest_shipping(weight):
    ground = ground_shipping(weight)
    drone = drone_shipping(weight)
    premium = 125

    if ground < drone and ground < premium:
        cheapest = "Ground Shipping"
        cost = ground
    elif drone < ground and drone < premium:
        cheapest = "Drone Shipping"
        cost = drone
    elif premium < ground and premium < drone:
        cheapest = "Premium Ground Shipping"
        cost = premium

    return ("The cheapest shipping is " + str(cheapest) + ". The cost is $" + str(cost) + "\n")

price_ground = str(ground_shipping(8.4)) + "\n"
price_drone = str(drone_shipping(1.5)) + "\n"
package_1 = cheapest_shipping(4.8)
package_2 = cheapest_shipping(41.5)

print(price_ground, price_drone, package_1, package_2)

