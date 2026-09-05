# Write a program that asks the user for a username and password. 
# If either or both are incorrect, the program ask the user to enter the username and password again.
# This continues until the login information is correct or wrong credentials have been entered five times. 
# If the information is correct, the program prints out Welcome. After five failed attempts the program prints out Access denied. 
# The correct username is python and password rules.

username= "python"
password= "rules"
attempts=0
while attempts <5:
     given_username= input("Enter your username: ")
     given_password= input("Enter your password: ")
     if given_username == username  and given_password ==password:
          print("Welcome")
          break
     else:
          attempts= attempts +1
          print("Incorrect username and password. Try again:") 
else:
     print("Access denied.")


