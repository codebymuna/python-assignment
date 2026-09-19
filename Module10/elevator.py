class Elevator:
    def __init__(self, bottom_floors,top_floors):
         self.bottom_floors  = bottom_floors
         self.top_floors= top_floors
         self.current_floor= bottom_floors

    def floor_up(self):
         if self.current_floor< self.top_floors:
              self.current_floor+=1
              print(f"Elevator is at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor> self.bottom_floors:
             self.current_floor-=1
             print(f"Elevator is at floor {self.current_floor}")

    def go_to_floor(self, target_floor):
         while self.current_floor< target_floor:
              self.floor_up()
         while self.current_floor> target_floor: 
              self.floor_down()


#Its same as task one, I separated it so that
# It could easily import the class and make changes with elevator.py 
# if needed.