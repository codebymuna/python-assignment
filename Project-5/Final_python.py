
def add_item(inventory):
    item = input("Enter the item to add: ")
    inventory.append(item)
    print("Congrats! You have added", item)


def remove_item(inventory):
    item = input("Enter the item you want to remove: ")

    if item in inventory:
        inventory.remove(item)
        print(item, "has been removed from the inventory.")
    else:
        print("Please enter a valid item.")


def show_item(inventory):
    if len(inventory) == 0:
        print("The inventory is empty.")
    else:
        print("Current inventory:")
        for thing in inventory:
            print("-", thing)


# Read the introduction from intro.txt
def show_intro():
    try:
        with open("intro.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("Welcome to the game!")


# Read the instructions from instructions.txt
def show_instructions():
    try:
        with open("instructions.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("Instructions file not found.")


# Save the game
def save_game(name, age, inventory):
    with open("savegame.txt", "w") as file:
        file.write(name + "\n")
        file.write(str(age) + "\n")

        for item in inventory:
            file.write(item + "\n")

    print("Game saved successfully!")


# Load a saved game
def load_game():
    try:
        with open("savegame.txt", "r") as file:
            lines = file.read().splitlines()

        if len(lines) < 2:
            return None

        name = lines[0]
        age = int(lines[1])
        inventory = lines[2:]

        return name, age, inventory

    except FileNotFoundError:
        return None


#                -- MAIN PROGRAM --

show_intro()

choice = input("Do you want to continue a saved game? (yes/no): ")

if choice.lower() == "yes":
    saved_game = load_game()

    if saved_game is not None:
        name, age, inventory = saved_game
        print("Saved game loaded successfully!")
        print("Welcome back,", name)
    else:
        print("No saved game was found.")
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        inventory = []
else:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    inventory = []


print(f"The name of the player is: {name}")
print(f"And the age is: {age}")

if age < 12:
    print("You are a minor, so turn off the game.")

else:
    show_instructions()

    print("Hello! This is the menu.")
    value = input("Enter your command: ")

    while value != "lopeta":

        if value == "help":
            print("Please contact our page.")

        elif value == "Details":
            print(f"Name is: {name}, Age: {age}")

        elif value == "joke":
            print("Be careful Coder, You are using Python!!")

        elif value == "add":
            add_item(inventory)

        elif value == "remove":
            remove_item(inventory)

        elif value == "show":
            show_item(inventory)

        elif value == "save":
            save_game(name, age, inventory)

        else:
            print("Invalid command.")

        print("Hello! This is the menu.")
        value = input("Enter your next command: ")

    # Save automatically when the player exits
    save_game(name, age, inventory)
    print("See you!")
