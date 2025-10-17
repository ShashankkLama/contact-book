class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model= model
        self.year= year
        
    def display_info(self):
        print (f"{self.brand} {self.model} {self.year}")
           

car1= Car("Toyota", "Corolla", 2002)
car1.display_info()

class ElectricCar(Car):   # class names usually start with capital letter
    def __init__(self, brand, model, year, battery):
        super().__init__(brand, model, year)
        self.battery = battery
        
    def battery_info(self):
        print(f"Battery Capacity: {self.battery} kWh")


# Create objects OUTSIDE the class definitions
car1 = Car("Toyota", "Corolla", 2002)
car1.display_info()

tesla = ElectricCar("Tesla", "Model S", 2023, 100)
tesla.display_info()
tesla.battery_info()