# create a program that asks for the players name and age and stores in variables and print it.
# project2: Add commands and modified
# Project3: Add inventory , at least three functions 

def add_item(inventory):                 #function inorder to add items to the inventory.
    item=input("Enter the item to add: ")
    inventory.append(item)
    print("Congrats! You have added",item )

def remove_item(inventory):               #function inorder to remove items from the inventory.
    item=input("Enter the item you want to remove: ")
    if item in inventory:
        inventory.remove(item)
        print(item,"has been removed from the inventory.")
    else:
        print("Please enter valid item.")

def show_item(inventory):                  #function inorder to display the available items in the inventory.
    if len(inventory)==0:
        print("The inventory is empty.")
    else:
        print("Current inventory:")
        for thing in inventory:
            print("-", thing)

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"The name of the player is: {name}")
print(f"And the age is: {age}")
if  age<12:
    print("You are minor and so turn off")
else:
    print("Hello! This is the menu:")
    inventory=[]
    value= input("Enter your command:")
    while value != "lopeta":
       
        if value=="help":
            print("Please contact our page")
        elif value=="Details":
            print(f"name is: {name}, Age: {age}")
        elif value=="joke":
            print("Be careful Coder, You are using python!!")
        elif value=="add":
            add_item(inventory)
        elif value=="remove":
            remove_item(inventory)
        elif value=="show":
            show_item(inventory)
        else:
            ("Invalid command.")

        print("Hello! This is the menu")
        value= input("Enter your next command: ")
    else:
        print("See you")

    
