from player import Player
from item import Item
from room import Room


key=Item("key",0.1)
book=Item("book",1)
coin=Item("coin",0.5)

entrance= Room("Entrance",key)
library= Room("Library",book)
treasure_room = Room("Treasure_room",coin)

rooms=[entrance,library,treasure_room]

name=input("Enter your name: ")
age = int (input("Enter your age: "))

player = Player(name, age, entrance)

value=input("Enter your command: ")
while value!="lopeta":
    if value=="help":
        print("Available commands:")
        print("details")
        print("move")
        print("collect")
        print("show")
        print("joke")
        print("lopeta")

    elif value=="details":
        print(f"Name: {player.name}")
        print(f"Age: {player.age}")
        print(f"Location: {player.location.name}")

    elif value == "joke":
        print("Be careful Coder, You are using Python!!")

    elif value == "collect":
        player.collect_item()

    elif value=="move":
        print("Available rooms: ")
        for number, room in enumerate(rooms, start=1):
            print(number, room.name)

        choice = int(input("Choose a room: "))

        if 1 <= choice <= len(rooms):
            destination = rooms[choice - 1]
            player.move(destination)
        else:
            print("Invalid room.")

    else:
        print("Invalid command.")

    value = input("Enter your next command: ")

print("See you!")

