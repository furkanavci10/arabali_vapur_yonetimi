class Vehicle:
    def __init__(self, brand, model, year, vehicle_type):
        self.brand = brand
        self.model = model
        self.year = year
        self.vehicle_type = vehicle_type

class Car(Vehicle):
    def __init__(self, brand, model, year, vehicle_type, number_plate):
        self.number_plate = number_plate
        super().__init__(brand, model, year, vehicle_type)

class Truck(Vehicle):
    def __init__(self, brand, model, year, vehicle_type, number_plate):
        self.number_plate = number_plate
        super().__init__(brand, model, year, vehicle_type)        
        
class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, vehicle_type, number_plate):
        self.number_plate = number_plate
        super().__init__(brand, model, year, vehicle_type)