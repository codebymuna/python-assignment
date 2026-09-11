# Write a main program that asks for a volume in gallons from the user 
# and converts the value to liters

def gas_in_galons (gallons):
    liter= volume_gal*3.79
    return liter
# main program
volume_gal=float (input("Enter volume in gallons:"))

while volume_gal>=0:
    liter=gas_in_galons (volume_gal)
    print("The volume in litre is: ",liter)
    volume_gal=float (input("Enter volume in gallons:"))