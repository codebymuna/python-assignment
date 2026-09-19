class Car:
    def __init__(self,reg_num,max_speed):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self,value): # An accelerate method is added for task-2
        self.current_speed += value
        if self.current_speed >  self.max_speed:
            self.current_speed = self.max_speed

        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self,hours):   # A new drive method is added for task-3
        self.travelled_distance += self.current_speed* hours
