# create a program that asks for the players name and age and stores in variables and print it.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"The name of the player is: {name}")
print(f"And the age is: {age}")
if  age<12:
    print("You are minor and so turn off")
else:
    print("Hello! This is the menu:")

    value= input("Enter your command:")
    while value != "lopeta":
        
        if value=="help":
            print("Please contact our page")
        elif value=="Details":
            print(f"name is: {name}, Age: {age}")
        elif value=="joke":
            print("Be careful Coder, You are using python!!")
        print("Hello! This is the menu")
        value= input("Enter your next command: ")
    else:
        print("See you")

    
