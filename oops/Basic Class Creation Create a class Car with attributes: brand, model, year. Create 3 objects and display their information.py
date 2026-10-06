class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
first_car=Car("Honda","Accord",2026)
print(first_car.brand,first_car.model,first_car.year)
Second_car=Car("GMC","Acadia",2026)
print(Second_car.brand,Second_car.model,Second_car.year)
Third_car=Car('Hyundai',"Creta",2020)
print(Third_car.brand,Third_car.model,Third_car.year)