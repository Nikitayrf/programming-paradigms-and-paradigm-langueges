class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

class Car(Vehicle):
    def start_engine(self):
        print(f"{self.color} автомобиль {self.brand} завел двигатель.")

    def stop_engine(self):
        print(f"{self.color} автомобиль {self.brand} заглушил двигатель.")
        