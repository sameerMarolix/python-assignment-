
class Car :
    def __init__(self,carName,brand,mileage,colour,gearSystem,noOfSeats):
        self.carName = carName
        self.brand = brand
        self.mileage = mileage
        self.colour = colour
        self.gearSystem = gearSystem
        self.noOfSeats = noOfSeats
    def display_car_details(self):
        return f'Care name {self.carName}.\n Brand is {self.brand}.\n maileage {self.mileage}km/ph.\n Gear system - {self.gearSystem}.\n No of seats are {self.noOfSeats}'
    
car1 = Car('Swift Dzir','Suziki', 24,"Red", "Manual",5)
car2 = Car("Ertiga","Maruti",20,"Gray",'Automatic',7)
print(car1.display_car_details())
print(car2.display_car_details())