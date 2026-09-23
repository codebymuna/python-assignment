class Car:
    def __init__(self,reg_num,max_speed):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.kilometers_driven = 0


    def accelerate(self,value): # An accelerate method is added for task-2
        self.current_speed += value
        if self.current_speed >  self.max_speed:
            self.current_speed = self.max_speed

        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self,hours):   # A new drive method is added for task-3
         self.kilometers_driven += self.current_speed * hours

class ElectricCar(Car):
    def __init__(self, reg_num, max_speed, battery_capacity):
        super().__init__(reg_num, max_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, reg_num, max_speed, volume):
        super().__init__(reg_num, max_speed)
        self.volume= volume

        # Main program
electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)

electric_car.accelerate(100)
gasoline_car.accelerate(80)

electric_car.drive(3)
gasoline_car.drive(3)

print(f"Electric car kilometer counter: {electric_car.kilometers_driven} km")
print(f"Gasoline car kilometer counter: {gasoline_car.kilometers_driven} km")
