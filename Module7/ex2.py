import random
def dice_roll(sides):  #function
    return random.randint(1,sides)
# main program
max_sides= int(input("Enter the number of sides on the dice:"))
roll= dice_roll(max_sides)   # function call
print("The roll is:", roll)
while roll!=max_sides:
    roll=dice_roll(max_sides)
    # num= dice_roll()
    print("The roll is:", roll)

