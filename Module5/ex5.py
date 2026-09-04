# Write a program that asks the user for a username and password. 
# If either or both are incorrect, the program ask the user to enter the username and password again.
# This continues until the login information is correct or wrong credentials have been entered five times. 
# If the information is correct, the program prints out Welcome. After five failed attempts the program prints out Access denied. 
# The correct username is python and password rules.

username= input("Enter the useraname: ")
password=input("Enter your password: ")
while username !="python" or password !="rules":
    # print("Enter the username and password again.")
    for i in range (0,5):
        if username!="python" and password!="rules":
             break
        else:
             print("Please enter your username and password: ")
             print("Welcome!")
             
    else:
      print("Access denied.")


