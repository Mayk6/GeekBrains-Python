class Car:
    def __init__(self, color, year, max_speed):
        self.color = color
        self.year = year
        self.max_speed = max_speed

    def __add__(self, other):
        return self.max_speed + other.max_speed

    def __radd__(self, other):
        return self.max_speed + other


bmw = Car('black', 2019, 250)
audi = Car('black', 2019, 250)
moskvich = Car('black', 2019, 250)
volvo = Car('black', 2019, 250)
print(bmw + volvo + audi)
