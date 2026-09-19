from elevator import Elevator
class Building:
    def __init__(self,bottom_floors, top_floors,elevator_count):
       self.bottom_floors  = bottom_floors
       self.top_floors= top_floors
       self.elevators= []
       for i in range(elevator_count):
           self.elevators.append(Elevator(bottom_floors,top_floors))

    def run_elevator(self,elevator_num,destination_floor):
        print(f"Elevator{elevator_num} going to floor {destination_floor}")
        self.elevators[elevator_num].go_to_floor(destination_floor)

b= Building(1,10,3)
b.run_elevator(0,4)
b.run_elevator(1,7)

        

