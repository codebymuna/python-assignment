# Write a program that asks the user how many dice to roll. 
# The program rolls all the dice once and prints out the sum
#  of the numbers. Use a for loop.

import random
roll=0
how_many=int (input("Enter how namy dice to roll: "))
for dice in range(0,how_many):
    roll=roll+ random.randint(1,6)

print("The sum is: ",roll)
