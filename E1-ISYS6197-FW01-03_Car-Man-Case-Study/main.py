from car import Car
from car import Truck
import random
import math

car = Car(0, "")
truck = Truck(0, "", 0)

name = ""
vehicle_type = ""
brand = ""

fuel = 0
weight = 0
speed = 0

while len(name) < 5 or len(name) > 25:
    name = input("Input your name [5-25 chars]: ")
    name.lower()

while vehicle_type.lower() != "car" and vehicle_type.lower() != "truck":
    vehicle_type = input("Input your vehicle ['Car' | 'Truck']: ")

while brand.lower() != "bmx" and brand.lower() != "toyoda" and brand.lower(
) != "pissan":
    brand = input("Input your car's brand ['BMX' | 'Toyoda' | 'Pissan']: ")

if (vehicle_type.lower() == 'car'):
    car.set_brand(brand)
else:
    truck.set_brand(brand)


def calculate_speed(start, stop, brand_length, weight):
    # Calculate speed for car
    return (random.randint(start, stop) +
            random.randint(0, brand_length)) - (0.02 * weight)


def drive(vehicle_type):
    distance = -1
    max_distance = -1
    speed = -1

    if (vehicle_type == "car"):
        max_distance = car.get_fuel() * 15
    else:
        max_distance = truck.get_fuel() * 10

    while int(distance) <= 0 or int(distance) > max_distance or distance == '':
        distance = input("Input distance [1-" + str(max_distance) + "]<km>: ")
        if distance == '':
            distance = -1

    if vehicle_type.lower() != "car":
        isCarrying = ""
        while isCarrying.lower() != "y" and isCarrying.lower() != "n":
            isCarrying = input("Do you want to carry items ?['Y' : 'N']: ")
            print(isCarrying)

        if isCarrying.lower() == "y":
            weight = 0
            while int(weight) <= 0 or int(weight) > 1500:
                weight = input(
                    "Input item weight to be carried [1 - 1500]<kg>: ")

        fuel_left = math.floor(
            calculate_speed(50, 100, len(truck.get_brand()),
                            truck.get_weight()) / 15)

        if fuel_left > truck.get_fuel():
            truck.set_fuel(0)
        else:
            truck.set_fuel(truck.get_fuel() - math.ceil(fuel_left))

    elif vehicle_type.lower() == "car":
        fuel_left = math.floor(
            calculate_speed(50, 100, len(car.get_brand()), 0) / 15)

        if fuel_left > car.get_fuel():
            car.set_fuel(0)
        else:
            car.set_fuel(car.get_fuel() - fuel_left)
            print(fuel_left)
            print(car.get_fuel())


while True:
    if vehicle_type.lower() == "car":
        fuel = car.get_fuel()

    else:
        fuel = truck.get_fuel()
        weight = truck.get_weight()

    choose = 9999
    while int(choose) > 5 or int(choose) < 1:
        print("1. Drive")
        print("2. Refill Gas")
        print("3. Check Vehicle")
        print("4. Change Vehicle")
        print("5. Exit")
        choose = input("Choose : ")

        if choose == '':
            choose = 0

        if int(choose) == 1:
            if (fuel > 0):
                drive(vehicle_type)
            else:
                print("Not Enough Fuel, Please Refil. . . ")

        if int(choose) == 2:
            if vehicle_type.lower() == 'car':
                if fuel == 20:
                    print('fuel is already full')
                else:
                    car.set_fuel(20)
            else:
                if fuel == 50:
                    print('fuel is already full')
                else:
                    truck.set_fuel(50)

        if int(choose) == 3:
            if (vehicle_type.lower() == "car"):
                print("Car Details")
                print("=" * 10)
                print("Brand" + (" " * 10) + ":" + car.get_brand())
                print("Fuel" + (" " * 10) + ":" + str(car.get_fuel()))
            else:
                print("Truck Details")
                print("=" * 10)
                print("Brand" + (" " * 10) + ":" + truck.get_brand())
                print("Fuel" + (" " * 10) + ":" + str(truck.get_fuel()))
