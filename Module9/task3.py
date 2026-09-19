from car import Car
car = Car( "ABC-123",140)
print(
     f"Registration number: {car.reg_num},maximum speed: {car.max_speed}"
)

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)

print(f"Current speed: {car.current_speed}")
car.accelerate(-200)
print(f"Current speed: {car.current_speed}")

car.drive(1.5)     #method call car.drive
print(f"Travelled distance: {car.travelled_distance}")
