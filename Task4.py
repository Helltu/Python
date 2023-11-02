class Car():
    car_count = 0
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        if(Car.is_valid_year(self)):
            Car.car_count += 1
        else:
            print(f"{self.year} не является подходящим годом для машины")
            print(f"Год машины {self.get_info()} установлен на стандартное значение - 2020")
            self.year = 2020
        
    def get_info(self):
        return f"{self.year} {self.make} {self.model}"
    
    @staticmethod
    def is_valid_year(car):
        return car.year >= 1900 and car.year <=2023
    
    @classmethod
    def get_total_car_count(cls):
        return cls.car_count
    
car1 = Car("Toyota", "Camry", 123)
car2 = Car ("Honda", "Civic", 2022)

print(car1.get_info())
print(car2.get_info())
print("Общее количество машин:", Car.get_total_car_count())

