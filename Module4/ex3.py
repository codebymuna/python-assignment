# Write a program that asks for the biological gender and hemoglobin value (g/l). 
# The program then notifies the user if the hemoglobin value is low, normal or high.
# A normal hemoglobin value for adult females is between 117-155 g/l.
# A normal hemoglobin value for adult males is between 134-167 g/l.
gender=input("Enter your biological gender: ")
hemo_value= int (input("Enter your hemoglobin value in g/l: "))
if gender=="female":
    if 117 <hemo_value<155:
        print("Your haemoglobin value is normal")
    elif hemo_value<117:
     print("Your hemoglobin value is low.")
    else:
     print("Your hemoglobin value is high.")
elif gender=="male":
    if 134< hemo_value< 167:
        print("Your haemoglobin value is normal.")
    elif hemo_value<134:
        print("Your haemoglobin value is low.")
    else:

        print("Youe haemoglobin value is high.")
else: 
    print("Invalid input.")
