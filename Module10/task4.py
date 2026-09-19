import random
from car import Car   # It requires the data from the class Car of module-9.

class Race:
    def __init__(self, name, distance,cars ):
        self.name=name
        self.distance=distance
        self.cars=cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10,15))
            car.drive(1)

    def print_status(self):
        print(f"\n{self.name} ({self.distance} km)")
        print(f"{'Registration':<14}{'Max speed':>10}{'Speed':>8}{'Distance:>12'}")
        print("-"*44)
        for car in self.cars:
           print(f"{car.reg_num:<14}"
                  f"{car.max_speed:>10}"
                  f"{car.current_speed:>8}"
                  f"{car.travelled_distance:>12}")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False


# main program
cars = []
for i in range(1, 11):
    cars.append(Car(f"ABC-{i}", random.randint(100, 200)))

race = Race("Grand Demolition Derby", 8000, cars)

hours = 0
while not race.race_finished():
    hours += 1
    race.hour_passes()
    if hours % 10 == 0:
        print(f"\nAfter {hours} hours:", end="")
        race.print_status()

# final status 
if hours % 10 != 0:
    print(f"\nRace finished after {hours} hours:", end="")
    race.print_status()
                  

                  

