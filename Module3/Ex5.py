# program that ask user's mass in diff units and converts the input to full kg and g and display the results.

mass1 = float (input("Enter your mass in talents: "))
mass2= float (input("Enter your mass in pounds: "))
mass3 = float(input("Enter your mass in lots: "))
total_lots= mass1*20*32+ mass2*32+ mass3
total_grams= total_lots*13.3
kg= total_grams //1000
grams= total_grams % 1000
print(f"Value in kilogram is :{kg}, grams:{grams}")