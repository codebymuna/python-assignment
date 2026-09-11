# WAP for fetching and storing airport data.

airports={}
while True:
    print("1. Enter a new airport.")
    print("2. Fetch the information of an existing airport.")
    print("3. Quit!.")
    choice= int(input("Choose an option."))
    if choice==1:
        icao_code=input("Enter the IOCD code of the airport.")
        name= input("Enter the airport name.")
        airports[icao_code]=name
        print(name,"has been saved with the given ICAO code.")
    elif choice==2:
        icao_code=input("Enter the IOCD code of the another airport.")
        if icao_code in airports:
            print("Airport name;",airports[icao_code])
        else:
            print("No airport is found with that ICAO code.")
    elif choice==3:
        print("See you again:)")
        break
    else:
        print("Invalid choice, Try again.")

