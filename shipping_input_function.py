weight = input("Please enter weight")
type_of_shipping = input("Please enter type of shipping")

def ground_shipping(weight):
    flat_charge = 20
    if weight <= 2:
        return flat_charge + (weight * 1.50)
    elif weight > 2 and weight <= 6:
        return flat_charge + (weight * 3)
    elif weight > 6 and weight <= 10:
        return flat_charge + (weight * 4)
    elif weight > 10:
        return flat_charge + (weight * 4.75)


def ground_premium_shipping(weight):
    flat_charge = 20
    premium_shipping = 125
    if weight <= 2:
        return flat_charge + (weight * 1.50) + premium_shipping
    elif weight > 2 and weight <= 6:
        return flat_charge + (weight * 3) + premium_shipping
    elif weight > 6 and weight <= 10:
        return flat_charge + (weight * 4) + premium_shipping
    elif weight > 10:
        return flat_charge + (weight * 4.75) + premium_shipping


def drone_shipping(weight):
    if weight <= 2:
        return (weight * 4.50)
    elif weight > 2 and weight <= 6:
        return (weight * 9)
    elif weight > 6 and weight <= 10:
        return (weight * 12)
    elif weight > 10:
        return (weight * 14.25)


print("Ground Shipping")
print("$" + str(round(ground_shipping(4.8))))
print("\n")
print("Premium Ground Shipping")
print("$" + str(round(ground_premium_shipping(4.8))))
print("\n")
print("Drone Shipping")
print("$" + str(round(drone_shipping(4.8))))