class car:
    def __init__(self,reg_num,max_speed):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

car = car( "ABC-123",140)
print(
     f"Registration number: {car.reg_num},maximum speed: {car.max_speed}"
)



    