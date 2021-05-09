class Car:
    def __init__(self, fuel, brand):
        self.fuel = fuel
        self.brand = brand

    def set_fuel(self, nFuel):
        self.fuel = nFuel

    def get_fuel(self):
        return self.fuel

    def set_brand(self, nBrand):
        self.brand = nBrand

    def get_brand(self):
        return self.brand


class Truck(Car):
    def __init__(self, fuel, brand, weight):
        super().__init__(fuel, brand)
        self.weight = weight

    def set_weight(self, nWeight):
        self.weight = nWeight

    def get_weight(self):
        return self.weight
