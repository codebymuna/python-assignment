class Player:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.items = []
        self.location = location

    def move(self, destination):
        self.location = destination

    def collect_item(self):
        if self.location.item is None:
            print("There is no item in this room.")
        else:
            item = self.location.item
            self.items.append(item)
            self.location.item = None
            print("You collected", item.name)