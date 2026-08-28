# Write a program that asks a fisher the length of a zander in centimeters.
# If the zander does not fulfill the size limit, the program instructs to release the fish back into the lake and 
# notifies the user of how many centimeters below the size limit the caught fish was.
# A zander must be 42 centimeters or longer to meet the size limit. 

length = float(input("Enter the length of a zander in cm: "))
if length< 42:
    print("Then release the fish back into the lake.")
    req_length= 42-length
    print(f"The fish was {req_length} cm below the size limit")
