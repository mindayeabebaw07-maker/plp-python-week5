class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery

    def charge(self):
        self.battery = 100
        return f"{self.model} charged to 100%"

    def use(self, amount):
        self.battery -= amount
        return f"Battery left: {self.battery}%"

phone1 = Smartphone("Samsung", "Galaxy", 80)
phone2 = Smartphone("Tecno", "Spark", 50)

print(phone1.brand, phone1.model)
print(phone1.use(20))
print(phone1.charge())
print(phone2.brand, phone2.model)
print(phone2.use(10))

# Polymorphism
class Car:
    def move(self):
        return "Driving 🚗"

class Plane:
    def move(self):
        return "Flying ✈️"

class Boat:
    def move(self):
        return "Sailing [STRIPPED 3 bytes] boat"

for vehicle in [Car(), Plane(), Boat()]:
    print(vehicle.move())
