#set
data=set()
# name=input("Enter your name: ")
name=input("Enter your name or press enter to stop.")
while name!="":
    if name in data:
        print("Existing name.")
    else:
        print("New name.")
        data.add(name)
    name=input("Enter your name or press enter to stop.")
print(data)
    

        
