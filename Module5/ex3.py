# Write a program that asks the user to enter numbers until they enter an empty string to quit.
# Finally, the program prints out the smallest and largest number from the numbers it received.

numbers=[]
while True:
    entry = (input("Enter a number"))
    if entry =="":
        break
    numbers.append(int (entry))
numbers.sort()
print(numbers)    
smallest_number= numbers[0]
largest_number= numbers[-1]
print("smallest:",smallest_number)
print("largest:",largest_number)


