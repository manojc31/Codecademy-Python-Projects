train_mass = 22680
train_acceleration = 10
train_distance = 100
f_temp = 100
bomb_mass = 1


def f_to_c(f_temp):
    return int((f_temp - 32) * 5 / 9)


f100_in_celsius = (f_to_c(100))


def c_to_f(c_temp):
    return int((c_temp * (9 / 5)) + 32)


f0_in_fahrenheit = (c_to_f(0))


def get_force(mass, acceleration):
    return int(mass * acceleration)


train_force = get_force(train_mass, train_acceleration)


def get_energy(mass, c=3 * 10 ** 8):
    return int(mass * c ** 2)


bomb_energy = get_energy(bomb_mass)


def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    return int(force * distance)


train_work = get_work(train_mass, train_acceleration, train_distance)

print(str(f100_in_celsius) + " C")
print(str(f0_in_fahrenheit) + " F")
print(str(train_force) + " N")
print(str(bomb_energy) + " J")
print(str(train_work) + " J")

print("The train supplies " + str(train_force) + " Newtons of force.")
print("A 1kg bomb supplies " + str(bomb_energy) + " joules.")
print("The train does " + str(train_work) + " joules of work over " + str(train_distance) + " meters")