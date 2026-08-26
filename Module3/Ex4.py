# program to add,multiply and find average of 3 integers given by user
import math
num1= int(input("Enter 1st number: "))
num2= int(input("Enter 2nd number: "))
num3= int(input("Enter 3rd number: "))
add = num1+num2+num3
product = num1*num2*num3
average = int (add)/3
print(f"Addition of 3 integers is: {add}")
print(f"product of 3 integers is: {product}")
print(f"Average of 3 ntegers is: {average}")