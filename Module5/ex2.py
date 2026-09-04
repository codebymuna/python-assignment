# Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.
value=int (input("Enter the value in inch: "))

while value>0:
    cm = value*2.54
    print(cm)
    value =value-1
else:
    print("value is negative")


