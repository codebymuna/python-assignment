import random 
from car import Car

cars=[]
# for loop
for i in range(10):
    max_speed= random.randint(100,200) 
    reg_num= f"ABC-{i+1}"     # As it begins through ABC-1 to ABC-10
    car=Car(reg_num,max_speed)
    cars.append(car)  #Add information to the list cars.

race_on=True
while race_on:
    for car in cars:
        car.accelerate(random.randint(-10,15))
        car.drive(1)

    for car in cars:
        if car.travelled_distance>1000:
            race_on=False
            break
print(f"The winner is: {cars[0].reg_num}") # TO display winner.

# Inorder to print the data in tabular form:
print(f"{'Registration number':<20}{'Max Speed':<12}{'Current speed':<15}{'Distance:<12'}") 
for car in cars:
    print(f"{car.reg_num:<20}{car.max_speed:<12}{car.current_speed:<15}{car.travelled_distance:<12.1f}") #.1f is used to print the float value.




